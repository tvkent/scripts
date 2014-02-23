#indivnames
#gives names of individuals in file for R script
#tyler kent 22 feb 2014

def names(inputt, output):

    #specify files to open

    infile=open(inputt, "r")
    linelist=infile.readlines()
    outfile=open(output, "w")


    list=str(linelist[0]).split() 
    x=11
    for i in range(len(list)-11):
        #for each entry from 11 till the end, add copy to newline
        newline=list[x]
        x+=1

    #write each new line to the output file
        outfile.write((newline)+"\n")

    infile.close()
    outfile.close()

infile=raw_input("File for input (include full path): ")
outfile=raw_input("File for output (include full path): ")
names(infile, outfile)
