READ ME

Files in this folder:

folders.py: 

This code automates the creation of the folders and files needed for my PAML analyses; it:
 -creates a new folder for each new analysis (STEP 1), with subfolders for each hypotesis tested (STEP 2)
 -creates new control files for codeml, asking user input for common parameters (model, NNsites, omega) (STEP 3)
 -creates subfolders for each gene, parting from a user-provided list of genes (STEP 4)
 -modifies and includes the necessary files (phylogeny, alignment, control), from the PhyloSuite result folder, into each gene folder (STEP 5)
     - MAKE SURE all (both nu and mt genes) alignments and phylogeny files are in the same folder
     - MAKE SURE names of the folders inside PhyloSuite are the same as in step 5 code
     
     
pamlcontrolfile_function.py:

This code contains a function used in folders.py. 
This function creates control file for paml, branch and branch-sites models.
