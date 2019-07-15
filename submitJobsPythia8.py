
scenarios=[#("CP1",2),
	   ("CP5",2),
	   #("CP5-CR1",2),
	   #("CP5-CR2o",2),
	   ("CUETP8M1",2),
	   ("A14",2),
	   #("A14-CR1",2),
	   #("A14-CR2",2),
	   #("FSRalphaS",15),
           #("FSRpTmin",15),
	   #("ISRalphaS",15),
	   #("FSR",100),
	   ]
	   

version=""

if True:
  #print "sed -i -e 's/2.5.2-njopjo\"/2.5.2\"/g' /afs/cern.ch/user/h/hinzmann/stable_13TeV/Rivet/CMSSW_9_2_6/config/toolbox/slc6_amd64_gcc530/tools/selected/rivet.xml"
  #print "scram setup rivet"
  for tune,number in scenarios:
    name=tune+version
    if number>2:
      scan="" # Sample the phase space of parameters
    else:
      scan="--scan" # Compute parameter on/off
    print "prof-sampleparams generatorP8"+tune+".ranges "+scan+" --include-corners --num-runs "+str(number)+" --seed 1 -o mcruns_"+name+\
      " -T FlatQCD-TuneCP5-Pythia8-8000GeV_cfg_"+tune+".py"+\
      " -T FlatQCD-TuneCP5-Pythia8-7000GeV_cfg_"+tune+".py"+\
      " -T FlatQCD-TuneCP5-Pythia8-13000GeV_cfg_"+tune+".py"+\
      " -T TTbar-TuneCP5-Pythia8-7000GeV_cfg_"+tune+".py"+\
      " -T TTbar-TuneCP5-Pythia8-13000GeV_cfg_"+tune+".py"
      # -T WJets-TuneCP5-Pythia8-7000GeV_cfg_"+tune+".py"+
      #" -T ZJets-TuneCP5-Pythia8-7000GeV_cfg_"+tune+".py"
  for tune,number in scenarios:
    name=tune+version
    print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q nextweek --directory mcruns_"+name+"/mc -c FlatQCD-TuneCP5-Pythia8-8000GeV_cfg_"+tune+".py"
    print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q nextweek --directory mcruns_"+name+"/mc -c FlatQCD-TuneCP5-Pythia8-7000GeV_cfg_"+tune+".py"
    print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q nextweek --directory mcruns_"+name+"/mc -c FlatQCD-TuneCP5-Pythia8-13000GeV_cfg_"+tune+".py"
    print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q nextweek --directory mcruns_"+name+"/mc -c TTbar-TuneCP5-Pythia8-7000GeV_cfg_"+tune+".py"
    print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q nextweek --directory mcruns_"+name+"/mc -c TTbar-TuneCP5-Pythia8-13000GeV_cfg_"+tune+".py"
    #print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q nextweek --directory mcruns_"+name+"/mc -c WJets-TuneCP5-Pythia8-7000GeV_cfg_"+tune+".py"
    #print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q nextweek --directory mcruns_"+name+"/mc -c ZJets-TuneCP5-Pythia8-7000GeV_cfg_"+tune+".py"
