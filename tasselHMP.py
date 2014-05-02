#tasselHMP.py
#using dictionaries to fill in missing data from Jiao to Ames
#Tyler Kent 17APR2014

def Dict(jiao, ames):
    Jiao={}
    jiaokeys=[]
    for line in jiao:
        newline=line.split() #split line by tabs to make list
        try:
            jiaokeys.append(int(newline[3])) #add snp pos to growing list
        except ValueError:
            #do nothing--->don't need the header
            b=0
        Jiao[newline[3]]=newline #create dictionary w/ snp pos as key and whole line as list as value

    Ames={}
    ameskeys=[]
    for line in ames:
        newline=line.split()
        try:
            ameskeys.append(int(newline[3]))
        except ValueError:
            b=0
        Ames[newline[3]]=newline
    jiaokeys.sort()
    ameskeys.sort()
    return(Jiao, Ames, jiaokeys, ameskeys)

def Key_Gen(Jiao, Ames, jiaokeys, ameskeys):
    finalkeys=[]
    for key in ameskeys:
        finalkeys.append(key) #add all snp pos from ames to total snp list
    for key in jiaokeys:
        if key not in finalkeys:
            finalkeys.append(key) #add missing snp pos in ames from jiao to total snp list
    finalkeys.sort() #sort keys numerically so file is in order of chromosome position

    return(finalkeys)

def Insert_Line(jiao,ames,Jiao,Ames,jiaokeys,ameskeys,finalkeys):
    outfile='AMES10.hmp.txt' #final file for tassel use
    outfile=open(outfile,'w')
    newline=ames[0].split() #split header 
    newline='\t'.join(newline) #and tab delimit for consistancy 
    outfile.write(newline+'\n')
    for key in finalkeys:
        if key in ameskeys: #add data from ames for positions in ames data set
            entries=Ames.get(str(key))
            line='\t'.join(entries) #tab delimit
            outfile.write(line+'\n')
        if key not in ameskeys: #add missing data for positions not in ames data set
            length=ames[0].split()
#add correct number of N
            outfile.write('S10_'+str(key)+'\t'+'NA\t'+'10\t'+str(key)+'\t'+'+\t'+'NA\t'+'NA\t'+'NA\t'+'NA\t'+'NA\t'+'NA\t')
            for i in range(len(length)-11):
                outfile.write('N\t')
            outfile.write('\n')
        if key in jiaokeys:
            entries=Jiao.get(str(key))
            line='\t'.join(entries)
            outfile2.write(line+'\n')
        if key not in jiaokeys:
            length=jiao[0].split()
            outfile2.write('ZMLCHR10N\t'+'NA\t'+'10\t'+str(key)+'\t'+'+\t'+'NA\t'+'NA\t'+'NA\t'+'NA\t$
            for i in range(len(length)-11):
                outfile2.write('NN\t')
            outfile2.write('\n')

jiao='Jiao_ch10.hmp.txt' #file for donor creation
ames='AmesUSInbreds_AllZeaGBSv1.0_imputed-130508/AmesUSInbreds_AllZeaGBSv1.0_imputed_20130508_chr10.hmp.txt' #file to be imputed
jiao=open(jiao,'r')
ames=open(ames,'r')
jiao=jiao.readlines() #create list of lines
ames=ames.readlines()
Jiao, Ames, jiaokeys, ameskeys=Dict(jiao,ames)
finalkeys=Key_Gen(Jiao, Ames, jiaokeys, ameskeys)
Insert_Line(jiao,ames,Jiao,Ames,jiaokeys,ameskeys,finalkeys)
