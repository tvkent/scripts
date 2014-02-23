#formatting for beagle from ames data

#12feb2014
#tyler kent

def double(inputt, output):

    #specify files to open

    infile=open(inputt, "r")
    linelist=infile.readlines()
    outfile=open(output, "w")

    a=0
    for line in linelist:
        #make list of each word in line
        list=str(linelist[a]).split() 
        #add marker & rs# to new line
        newline=list[0]+"\t"+list[1]+"\t"

        x=2
        for i in range(len(list)-2):
            #for each entry from 2 till the end, add 2 copies to newline
            newline=newline+"\t"+list[x]+"\t"+list[x] 
            x+=1
        #write each new line to the output file
        outfile.write((newline)+"\n")
        a+=1

    infile.close()
    outfile.close()

def ten(inter):

    infile=open(inter, 'r')
    linelist=infile.readlines()
    #reference from 10indiv program to use same indivs for every chr
    reference=open("/home/tyler/Centromere_Drive/Ames_beagle/10indivBGL/ameschr10_10indiv", 'r')
    reflist=reference.readlines()
    refline=reflist[0].split() #list of entries in header of reference
    outfile=open(inter, 'w')

    list=linelist[0].split()
    collist=[] #make list of columns based on header entries
    s=0
    for entry in list:
        if entry in refline: #check entries in new file header for matches to reference
            collist.append(s)
        s+=1

    a=0
    for line in linelist:
        newline=""
        list=linelist[a].split()
        
        for column in collist:
            newline=newline+list[int(column)]+'\t' #add each correct column from list above to new line in file
        outfile.write(newline+'\n')
        a+=1

    infile.close()
    outfile.close()
        
        
def markers(inputt, inter):
    
     #specify files to open
    infile=open(inputt, "r")
    linelist=infile.readlines()

    outfile=open(inter,"w")

    #add 'I' to first line
    line="I\t"+str(linelist[0])
    outfile.write(line)

    #add 'M' to remaining lines
    x=1
    for i in range(len(linelist)-1):
        line="M\t"+str(linelist[x])
        outfile.write(line)
        x+=1

    infile.close()
    outfile.close()

  
infile=raw_input("File for input (include full path): ")
inter=raw_input("File for intermediate (include full path): ")
outfile=raw_input("File for output (include full path): ")
markers(infile, inter)
ten(inter)
double(inter, outfile)

