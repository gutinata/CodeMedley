#This code automates the creation of the folders and files needed for my PAML analyses; it:
# -creates a new folder for each new analysis (STEP 1), with subfolders for each hypotesis tested (STEP 2)
# -creates new control files for codeml, asking user input for common parameters (model, NNsites, omega) (STEP 3)
# -creates subfolders for each gene, parting from a user-provided list of genes (STEP 4)
# -modifies and includes the necessary files (phylogeny, alignment, control), from the PhyloSuite result folder, into each gene folder (STEP 5)
#     - MAKE SURE all (both nu and mt genes) alignments and phylogeny files are in the same folder
#     - MAKE SURE names of the folders inside PhyloSuite are the same as in step 5 code

#Import modules
import os
import shutil
import re

# detect the current working directory and print it
path = os.getcwd()
print ("Current working directory is:", path)

############
## STEP 1 ##

#ask the user to define where the folders will be created
#Current working directory is: /Users/ngp/Documents/UNL/THESIS/Chapter_2_oxphos_phyllotis/try_automated_analyses/
wd = input ("Enter the path to the folder you wish to work at: ")

#change working directory to the one chosen in the previous step
os.chdir(wd)
path = os.getcwd()
print ("Current working directory is:", path)

#create main analysis folder, ask user for name
maindr = input ("Enter the name of the new directory (don't include spaces): ")
os.mkdir (maindr)

############
## STEP 2 ##

#create two more folders for HA and H0 inside maindr
os.chdir(maindr)
path = os.getcwd()
print ("Current working directory is:", path)
os.mkdir("HA")
os.mkdir("H0")

############
## STEP 3 ##

#use of previously created function to make the paml control file
from pamlcontrolfile_function import paml_control_file

#obtain the list of subdirectories in the newly created directory (maindr)
hypotheses_folders = os.listdir ()
print (hypotheses_folders)

#loop through subdirectories and create a paml control file inside each of them 
for x in hypotheses_folders:
    print("Enter the model parameters for %s" % x)
    os.chdir("%s/" % x)
    paml_control_file()
    print ("Control file created at %s" % x) 
    os.chdir("..")

############
## STEP 4 ##

#ask user to give the list of gene names to create folders with these names.
#line.rstrip(gets rid of the new line at the end of each line)
#store these names in a list and inform the user of what just happened.
genelist_path = input ("Enter the path to the gene list file (txt): ")
with open (genelist_path) as file:
    gene_list = [line.rstrip() for line in file]

print ("List of %s genes created: \n" % len(gene_list), gene_list)

#create gene folders inside HA and H0
for x in hypotheses_folders:
    os.chdir("%s/" % x)
    for y in gene_list:
        os.mkdir(y)
    print ("%s folders created at %s" % (len(gene_list), x))
    os.chdir("..")

############
## STEP 5 ##

#ask user for location of PhyloSuite outfiles
phylosuite_folder_path = input ("Enter the path to the folder with PhyloSuite results: ")

#5a copy alignment files inte each gene folder created in step 4
for a in gene_list:
    for b in hypotheses_folders:
        shutil.copy2("%s/alineamientos_PHY/%s_mafft.phy" % (phylosuite_folder_path,a), "%s/%s/%s/" % (path,b,a))
        print ("Phylogeny files copied to %s" % b)

#5b copy phylogeny and add #1 to foreground branch
foreground = input ("Enter name of foreground branch: ")

for a in gene_list:
    for b in hypotheses_folders:
        #copies the oroginal phylogeny file into the new folder
        shutil.copy2("%s/IQtree_results/%s_mafft/%s_mafft.phy.treefile" % (phylosuite_folder_path,a,a), "%s/%s/%s/%s.tre" % (path,b,a,a))
        print ("Phylogeny files copied to %s" % a)
        
        #adds a #1 to the foreground branch
        phy = open ("%s/%s/%s/%s.tre" % (path,b,a,a), "r")
        l = phy.read()
        phy.close()
        my_regex = re.compile(re.escape(foreground) + r':0\.\d{10}')
        initial = my_regex.findall(l)[0]
        replacement = initial + " #1"
        final = l.replace (initial, replacement)
        print ("Text successfully replaced in %s.tre" % a)

        #creates new phylogeny file with marked foreground branch
        output_file = open("%s/%s/%s/%s_rep.tre" % (path,b,a,a), "w")
        output_file.write(final)
        output_file.close()
        print ("%s_rep.tre successfully created" % a)

        #PENDING see if it's worth it to delete the original phylogeny file

#5c copies the control file (codeml.ctl) into each gene folder and modifies it to use the names of the other files already in that folder
for a in gene_list:
    for b in hypotheses_folders:

        controlfile = open ("%s/%s/codeml.ctl" % (path,b), "r")
        ll = controlfile.readlines()
        controlfile.close()

        output_file = open("%s/%s/%s/codeml.ctl" % (path,b,a), "a+")
        cc = 0
        for i in ll:
            if "genename" in i:
                rep2 = i.replace("genename", "%s" % a)
                output_file.write(rep2)
                cc += 1
            else:
                output_file.write(i)
                cc += 1

        output_file.close()
        print ("Control file successfully created at %s" % a)


