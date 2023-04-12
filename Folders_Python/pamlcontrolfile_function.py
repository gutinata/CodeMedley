#create control file for paml, branch and branch-sites models
def paml_control_file ():

    codeml_ctl = open ("codeml.ctl", "x")
    model = input ("Enter model: ")
    NSsites = input ("Enter NSsites: ")
    omega = input ("Enter omega: ")
    fix_omega = input ("Enter fix_omega: ")
    codeml_ctl_text = [
    "      seqfile = genename_mafft.phy\n",
    "     treefile = genename_rep.tre\n",
    "      outfile = genename_paml\n",
    "\n",
    "        noisy = 3   * 0,1,2,3,9: how much rubbish on the screen\n",
    "      verbose = 1   * 1: detailed output, 0: concise output\n",
    "      runmode = 0   * 0: user tree;  1: semi-automatic;  2: automatic\n",
    "                    * 3: StepwiseAddition; (4,5):PerturbationNNI\n",
    "\n",
    "      seqtype = 1   * 1:codons; 2:AAs; 3:codons-->AAs\n",
    "        clock = 0   * 0: no clock, unrooted tree, 1: clock, rooted tree\n",
    "        model = ", model, "\n",
    "                    * models for codons:\n",
    "                        * 0:one, 1:b, 2:2 or more dN/dS ratios for branches\n",
    "\n",
    "      NSsites = ", NSsites, "   * dN/dS among sites. 0:no variation, 1:neutral, 2:positive\n",
    "        icode = 0   * 0:standard genetic code; 1:mammalian mt; 2-10:see below\n",
    "\n",
    "    fix_kappa = 0   * 1: kappa fixed, 0: kappa to be estimated\n",
    "        kappa = 2   * initial or fixed kappa\n",
    "    fix_omega = ", fix_omega, "   * 1: omega or omega_1 fixed, 0: estimate \n",
    "        omega = ", omega, "   * initial or fixed omega, for codons or codon-transltd AAs\n",
    "\n",
    "    fix_alpha = 1   * 0: estimate gamma shape parameter; 1: fix it at alpha\n",
    "        alpha = .0  * initial or fixed alpha, 0:infinity (constant rate)\n",
    "       Malpha = 0   * different alphas for genes\n",
    "        ncatG = 4   * # of categories in the dG or AdG models of rates\n",
    "\n",
    "        getSE = 0   * 0: don't want them, 1: want S.E.s of estimates\n",
    " RateAncestor = 1   * (1/0): rates (alpha>0) or anc2estral states (alpha=0)\n",
    "\n",
    "  fix_blength = 1  * 0: ignore, -1: random, 1: initial, 2: fixed\n",
    "       method = 0   * 0: simultaneous; 1: one branch at a time\n",
    "\n",
    "* Specifications for duplicating results for the small data set in table 1\n",
    "* of Yang (1998 MBE 15:568-573).\n",
    "* see the tree file lysozyme.trees for specification of node (branch) labels\n",
    ]
    codeml_ctl.writelines (codeml_ctl_text)
    codeml_ctl.close()
