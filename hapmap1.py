#hapmap1.py
#simple script to choose 10k random hapmap lines from a larger file
#by tkent feb 2014

def main():
	
    import random
    #specify the file to open
    file1="/home/tyler/Centromere_Drive/Ames_beagle/ameschr10f"
    infile=open(file1,"r")
    linelist=infile.readlines()

    file2="/home/tyler/Centromere_Drive/Ames_beagle/chr10frand"
    store=open(file2,"w")
    #write header to new file
    store.write(str(linelist[0]))
            
    used=[]
    #run loop size range(x)
    for i in range(25):
            number=random.randint(1,len(linelist)) #pick random number btwn 1 and #lines
            if number not in used: #only use unique numbers
                    store.write(str(linelist[number])) #write line number to file
            while number in used:
                    number=random.randint(1,len(linelist)) #keep picking new number until find unique num
                    if number not in used:
                            store.write(str(linelist[number]))
            used.append(number) #keep list of used numbers

    infile.close()
    store.close()

main()
