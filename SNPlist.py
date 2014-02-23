#SNPlist
#makes list of SNPs in Beagle file
#Tyler Kent feb2014

def main():
    infile=raw_input("File for input (include full path): ")
    outfile=raw_input("File for output (include full path): ")
    infile=open(infile, 'r')
    linelist=infile.readlines()
    outfile=open(outfile,'w')

    a=1
    for line in linelist:
        if line==linelist[0]:
            a=1 #do nothing to first line in file (header)
        
        else:
            newline=str(linelist[a]).split() #split line at tabs
            entry=newline[1] #only take the snp name
            outfile.write(entry+'\n') #write to file
            a+=1
            
    infile.close()
    outfile.close()

main()
