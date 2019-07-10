
scenarios=[("default",2),
	   ]
	   
version=""
weights="weightsSelected"

if True:
  for tune,number in scenarios:
    name=tune+version
    if name=="FSR" or "All" in name:
      scan=""
    else:
      scan="--scan"
    print "prof-sampleparams generatorH7"+tune+".ranges "+scan+" --include-corners --num-runs "+str(number)+" --seed 1 -o mcruns_"+name+\
      " -T FlatQCD-Herwig7-8000GeV_cfg_"+tune+".py"+\
      " -T FlatQCD-Herwig7-7000GeV_cfg_"+tune+".py"+\
      " -T FlatQCD-Herwig7-13000GeV_cfg_"+tune+".py"
  for tune,number in scenarios:
    name=tune+version
    print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q nextweek --directory mcruns_"+name+"/mc -c FlatQCD-Herwig7-8000GeV_cfg_"+tune+".py"
    print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q nextweek --directory mcruns_"+name+"/mc -c FlatQCD-Herwig7-7000GeV_cfg_"+tune+".py"
    print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q nextweek --directory mcruns_"+name+"/mc -c FlatQCD-Herwig7-13000GeV_cfg_"+tune+".py"
