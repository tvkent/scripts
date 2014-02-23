#use dictionaries to search beagle fibd for indivs IBD @ SNP
#Tyler Kent 19 feb 14

def Dict(SNP,pval):
    #decide which chromosome user inputted
    snpsplit=SNP.split('_') #split snp ID
    snp1=snpsplit[0] #only need first 'Schr' part
    chr=snp1.lstrip('S') #chr number is everything but 'S'
    
    file1='/home/tyler/Centromere_Drive/Ames_beagle/10indivBGL/SNPlistchr'+str(chr) #input file of SNP positions
    infile=open(file1,'r')
    lines=infile.readlines()
    i=0
    #make SNP dictionary
    SNPs={}
    for line in lines:
        Id=str(line).rstrip('\n') #key in dictionary is SNP name
        SNPs[Id]=i #value in dictionary is the line number starting at 0
        i+=1

    pvalsplit=pval.split('-') #split pvalue by '-'
    thres=pvalsplit[1] #threshold number is after '-'
    file2='/home/tyler/Centromere_Drive/Ames_beagle/10indivBGL/Pvale-'+str(thres)+'/chr'+str(chr)+'out-10.ameschr'+str(chr)+'_10indiv.fibd' #fibd input file
    infile2=open(file2,'r')
    lines2=infile2.readlines()
    #make range/indiv dictionary
    RANGE={}
    keys=[]
    for line in lines2:
        split=line.split()
        span=split[2] #lower bound of the IBD region, also key in dictionary
        keys.append(int(span)) #make list of lower bound for search
        indivs=split[3]+' '+split[0]+' '+split[1] #dictionary values are upper bound, indivs
        RANGE[span]=indivs

    infile.close()
    infile2.close()

    return SNPs, RANGE, keys, chr, thres

def SNP_num(snp,SNPs): #don't know why I made this a separate module
    #get line number corresponding to SNP
    number=SNPs.get(snp)

    return number

def Binary(snpnum, RANGE, SNP, keys):
    #sort RANGE keys numerically
    keys.sort()
    
    low=0 #set search region as key entries
    high=len(keys)-1
  
    indivs=[]
    while low<=high: #only search as long as there's search space left
        mid=(low+high)//2 #start search at middle entry
        item=keys[mid] #key at middle
        item2=keys[mid+1] #key one above middle
        if int(item)<=int(snpnum) and int(item2)>=int(snpnum): #searching for highest key still smaller than SNP #
            key=str(item) #get lower bound at found entry
            entries=RANGE.get(key) #get values for lower bound key
            entrylist=entries.split(' ') #make list of values
            if int(entrylist[0])>=snpnum: #only care about indivs if upper bound bigger than snp#
                indivs.append(entrylist[1]+'    '+entrylist[2]) #add indivs to indiv list
            mid=mid-1 #move down one entry to check next lower bound smaller than snp#
            stop=False
            while not stop: #keep moving down list of lower bounds
                if int(keys[mid])<=int(snpnum): #check to make sure lower bound smaller than snp#
                    key=str(keys[mid])
                    entries=RANGE.get(key)
                    entrylist=entries.split(' ')
                    if int(entrylist[0])>=snpnum: #only use if upper bound bigger than snp#
                        indivs.append(entrylist[1]+'    '+entrylist[2])
                if int(keys[mid])>int(snpnum): #if for some magic reason the lower bound is bigger, stop. will stop once reaches highest
                    stop=True
                mid=mid-1
            return indivs #pass list of indivs
        elif int(item)>int(snpnum): #if entry in search bigger than snp# check lower half
            high=mid-1
            
        elif int(item2)<int(snpnum): #if entry in search smaller than snp# check upper half
            low=mid+1
    return 'nada' #pass nothing if no indivs IBD at snp
                    
def Write_File(indivs, chr, thres, SNP):
    #file to write indivs, specific to chr and SNP
    print(thres)
    filename='/home/tyler/Centromere_Drive/Ames_beagle/10indivBGL/Pvale-'+str(thres)+'/chr'+str(chr)+'search_'+str(SNP)
    outfile=open(filename,'w')
    i=0
    for line in indivs:
        outfile.write(indivs[i]+'\n')
        i+=1
    outfile.close()


SNP=raw_input('Enter the SNP IDs separated by commas (e.g.: S1_8500,S10_80092): ') #get Snp ids
pval=raw_input('Enter the threshold level used in beagle (e.g.:1e-10): ') #get desired pvalue
import time
start_time = time.time()
SNPlist=SNP.split(',') #create list of inputted snps
i=0
for snp in SNPlist: #loop through entire program for each snp entered
    SNPs, RANGE, keys, chr, thres=Dict(SNPlist[i], pval)
    snpnum=SNP_num(snp, SNPs)
    indivs=Binary(snpnum, RANGE, SNPlist[i], keys)
    Write_File(indivs, chr, thres, SNPlist[i])
    i+=1

print time.time() - start_time, "seconds"


