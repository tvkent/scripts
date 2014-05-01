def main():
    infile1='AMES1.hmp.txt'
    infile2='AMES2.hmp.txt'
    infile3='AMES3.hmp.txt'
    infile4='AMES4.hmp.txt'
    infile5='AMES5.hmp.txt'
    infile6='AMES6.hmp.txt'
    infile7='AMES7.hmp.txt'
    infile8='AMES8.hmp.txt'
    infile9='AMES9.hmp.txt'
    infile10='AMES10.hmp.txt'
    infile1=open(infile1,'r')
    infile2=open(infile2,'r')
    infile3=open(infile3,'r')
    infile4=open(infile4,'r')
    infile5=open(infile5,'r')
    infile6=open(infile6,'r')
    infile7=open(infile7,'r')
    infile8=open(infile8,'r')
    infile9=open(infile9,'r')
    infile10=open(infile10,'r')
    infile1=infile1.readlines()
    infile2=infile2.readlines()
    infile3=infile3.readlines()
    infile4=infile4.readlines()
    infile5=infile5.readlines()
    infile6=infile6.readlines()
    infile7=infile7.readlines()
    infile8=infile8.readlines()
    infile9=infile9.readlines()
    infile10=infile10.readlines()
    outfile='AMES.hmp.txt'
    outfile.open(outfile,'w')
    for line in infile1:
        outfile.write(line)
    for line in infile2:
        outfile.write(line)
    for line in infile3
        outfile.write(line)
    for line in infile4:
        outfile.write(line)
    for line in infile5:
        outfile.write(line)
    for line in infile6:
        outfile.write(line)
    for line in infile7:
        outfile.write(line)
    for line in infile8:
        outfile.write(line)
    for line in infile9:
        outfile.write(line)
    for line in infile10:
        outfile.write(line)
    outfile.close()

main()
    
    
