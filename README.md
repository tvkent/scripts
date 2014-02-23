scripts
=======

mostly python scripts

SNPsearch.py

    Python 2.7 script to search Beagle fibd outputs for individuals IBD at a SNP in question.  
    Make sure to have a file with a list of SNPs.
    won't work for the last SNP in the file > need to fix
  
10indiv_format.py

    Formats Ames hapmap file into Beagle format with only a certain amount of random individuals (here 10)
  
10indiv_otherchr.py

    Formats ames hapmap into beagle format for the same random individuals generated in 10indiv_format.py
    Run 10indiv_format.py first

BeagleFormat_AMES.py

    Formats full AMES hapmap file for use in Beagle
    note: very slow > may edit to run on farm
  
SNPlist.py

    Makes file of all SNP names in beagle input for use in other scripts
  
SNPsearch.py

    Python 2.7 script to search Beagle fibd outputs for individuals IBD at a SNP in question.  
    Make sure to have a file with a list of SNPs.
    won't work for the last SNP in the file > need to fix
  
randomizer.py

    Chooses random lines from hapmap file
  
indivnames.py

    Makes file of individual's names for use in other scripts
    
samplebashbeagle

    sample input for running beagle on farm
    make sure to specify CPUs with -c X where here, X is 10
    -Djava option changes temp directory to one with plenty of space
