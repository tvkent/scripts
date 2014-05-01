#CHRsplit.py
#split hmp file into separate files by chromosome to make my life easier
#I think
#could make it harder
#fuck it
#Tyler Kent 18APR2014

def split():
    infile='/home/tyler/SNP_all_lines.hmp.txt'
    infile=open(infile,'r')
    infile=infile.readlines()

    chr1='/home/tyler/Jiao_ch1.hmp.txt'
    chr2='/home/tyler/Jiao_ch2.hmp.txt'
    chr3='/home/tyler/Jiao_ch3.hmp.txt'
    chr4='/home/tyler/Jiao_ch4.hmp.txt'
    chr5='/home/tyler/Jiao_ch5.hmp.txt'
    chr6='/home/tyler/Jiao_ch6.hmp.txt'
    chr7='/home/tyler/Jiao_ch7.hmp.txt'
    chr8='/home/tyler/Jiao_ch8.hmp.txt'
    chr9='/home/tyler/Jiao_ch9.hmp.txt'
    chr10='/home/tyler/Jiao_ch10.hmp.txt'
    chr1=open(chr1,'w')
    chr2=open(chr2,'w')
    chr3=open(chr3,'w')
    chr4=open(chr4,'w')
    chr5=open(chr5,'w')
    chr6=open(chr6,'w')
    chr7=open(chr7,'w')
    chr8=open(chr8,'w')
    chr9=open(chr9,'w')
    chr10=open(chr10,'w')

    for line in infile:
        newline=line.split()
        if newline[2]=='chrom':
            chr1.write(line+'\n')
            chr2.write(line+'\n')
            chr3.write(line+'\n')
            chr4.write(line+'\n')
            chr5.write(line+'\n')
            chr6.write(line+'\n')
            chr7.write(line+'\n')
            chr8.write(line+'\n')
            chr9.write(line+'\n')
            chr10.write(line+'\n')
        elif newline[2]=='chr1':
            chr1.write(line+'\n')
        elif newline[2]=='chr2':
            chr2.write(line+'\n')
        elif newline[2]=='chr3':
            chr3.write(line+'\n')
        elif newline[2]=='chr4':
            chr4.write(line+'\n')
        elif newline[2]=='chr5':
            chr5.write(line+'\n')
        elif newline[2]=='chr6':
            chr6.write(line+'\n')
        elif newline[2]=='chr7':
            chr7.write(line+'\n')
        elif newline[2]=='chr8':
            chr8.write(line+'\n')
        elif newline[2]=='chr9':
            chr9.write(line+'\n')
        elif newline[2]=='chr10':
            chr10.write(line+'\n')

split()
