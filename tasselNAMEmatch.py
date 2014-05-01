#checks to see if names of individuals in the jiao and ames sets are really the same or not
#probably needs a shit ton of memory
#Tyler Kent 1May2014


def Header(jiao,ames):
    jiaoheader=jiao[0].split()
    amesheader=ames[0].split()
    matches={}
    nonmatches=[]
    matcheskeys=[]
    j=0
    for entry in jiaoheader:
        a=0
        for column in amesheader:
            if ':' in column: #only the names have : so skip the first few columns
                colsplit=column.split(':')
                colname=colsplit[3] #only the last bit seems to match 
                if entry==colname:
                    matches[entry]=column,j,a #dictionary w/ key as jiao name, values as ames name, jiao column, ames column
                    matcheskeys.append(entry) #list of keys
            a+=1
        j+=1
    for entry in jiaoheader:
        if entry not in matcheskeys:
            nonmatches.append(entry) #make list of jiao names not in ames set
    
    return(matches,matcheskeys,nonmatches)

def Percent(jiao,ames,matches,matcheskeys,nonmatches):
    outfile='namematch.txt'
    outfile=open(outfile,'w')
    for key in matcheskeys:
        values=matches.get(key) #use matcheskeys list to get values one at a time
        
        jiaocol=[]
        amescol=[]
        for line in jiao:
            if line!=jiao[0]: #skip the header, don't need to compare
                jsplit=line.split()
                jiaocol.append(jsplit[values[1]]) #haplotypes in match column
       
        for row in ames:
            if row!=ames[0]:
                asplit=row.split()
                amescol.append(asplit[values[2]]) #haplotypes in match column
        
        count=0
        top=0
        bottom=0
        for item in jiaocol:
            jiaohap=jiaocol[count] #one by one haplotype in match column
            jiaohap=jiaohap[0] #jiao set has genotype?
            
            if amescol[count]!='N': #don't need to compare missing data--->noisy
                bottom+=1
                if jiaohap==amescol[count]:
                    top+=1
            count+=1
        
        
        ratio=(str(top)+'/'+str(bottom)) #ratio of matches excluding missing data in ames
        outfile.write(str(key)+'\t'+str(values[0])+'\t'+str(ratio)+'\n')
    for item in nonmatches:
        outfile.write(item+'\n')
    outfile.close()
        
      
            

jiao='SNP_all_lines.hmp.txt' #file for donor creation
ames='AMES.hmp.txt' #file to be imputed
jiaofile=open(jiao,'r')
amesfile=open(ames,'r')
jiao=jiaofile.readlines() #create list of lines
ames=amesfile.readlines()
matches,matcheskeys,nonmatches=Header(jiao,ames)
Percent(jiao,ames,matches,matcheskeys,nonmatches)
jiaofile.close()
amesfile.close()
