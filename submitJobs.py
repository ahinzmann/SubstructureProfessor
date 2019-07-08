
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
	   ("default",2),
	   ]
	   
runJobs=False
doYoda=False
analyseOutput=True

version=""
weights="weightsQCD"
#weights="weightsSelected"

if runJobs:
  print "sed -i -e 's/2.5.2-njopjo\"/2.5.2\"/g' /afs/cern.ch/user/h/hinzmann/stable_13TeV/Rivet/CMSSW_9_2_6/config/toolbox/slc6_amd64_gcc530/tools/selected/rivet.xml"
  print "scram setup rivet"
  for tune,number in scenarios:
    name=tune+version
    if name=="FSR" or "All" in name:
      scan=""
    else:
      scan="--scan"
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
    print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q 1nw --directory mcruns_"+name+"/mc -c FlatQCD-TuneCP5-Pythia8-8000GeV_cfg_"+tune+".py"
    print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q 1nw --directory mcruns_"+name+"/mc -c FlatQCD-TuneCP5-Pythia8-7000GeV_cfg_"+tune+".py"
    print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q 1nw --directory mcruns_"+name+"/mc -c FlatQCD-TuneCP5-Pythia8-13000GeV_cfg_"+tune+".py"
    #print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q 1nw --directory mcruns_"+name+"/mc -c WJets-TuneCP5-Pythia8-7000GeV_cfg_"+tune+".py"
    #print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q 1nw --directory mcruns_"+name+"/mc -c ZJets-TuneCP5-Pythia8-7000GeV_cfg_"+tune+".py"
    print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q 1nw --directory mcruns_"+name+"/mc -c TTbar-TuneCP5-Pythia8-7000GeV_cfg_"+tune+".py"
    print "python submit_mcpoint_checkifexist_lxplus.py --runs 0-"+str(number-1)+" -q 1nw --directory mcruns_"+name+"/mc -c TTbar-TuneCP5-Pythia8-13000GeV_cfg_"+tune+".py"

if doYoda:
  print "sed -i -e 's/2.5.2\"/2.5.2-njopjo\"/g' /afs/cern.ch/user/h/hinzmann/stable_13TeV/Rivet/CMSSW_9_2_6/config/toolbox/slc6_amd64_gcc530/tools/selected/rivet.xml"
  print "scram setup rivet"
  print "ln -s ../GeneratorInterface/RivetInterface/data ref"
  for tune,number in scenarios:
    name=tune+version
    print "./YodaConvert.sh mcruns_"+name
    print "rm mcruns_"+name+"/mc/*/*.yoda"
    print "prof-runcombs --mc mcruns_"+name+"/mc -c 0:1 -o runcombs_"+name+".dat --weights "+weights
 
if analyseOutput:
  for tune,number in scenarios:
    name=tune+version
    outname=tune+version+weights.replace("weights","")
    print "rm -r out_"+outname
    print "prof-envelopes --mcdir mcruns_"+name+"/mc/ --datadir . --cl 100 --weights "+weights+" --runs runcombs_"+name+".dat --outdir=out_"+outname
    print "./make-plots --png out_"+outname+"/envelopes/*.dat"
  
  for tune,number in scenarios:
    name=tune+version
    outname=tune+version+weights.replace("weights","")
    method=""
    if number<=2:
      method="--ipol=linear"
    elif number>50:
      method="--ipol=cubic"
    else:
      method="--ipol=quadratic"
    print "prof-interpolate --mcdir mcruns_"+name+"/mc/ --datadir . --weights "+weights+" --runs runcombs_"+name+".dat "+method+" --outdir=out_"+outname
    print "prof-tune --datadir . --runs runcombs_"+name+".dat --mcdir mcruns_"+name+"/mc --weights "+weights+" "+method+" --ipoldir=out_"+outname+"/ipol/ --outdir=out_"+outname

  print "prof-ipolhistos --datadir . --runs runcombs_CP1.dat --mcdir mcruns_CP1/mc --weights "+weights+" --ipol=linear --ipoldir=out_CP1"+weights.replace("weights","")+"/ipol/ --outdir=out_CP1"+weights.replace("weights","")+" --params=ColourReconnection:mode=0"
  print "prof-ipolhistos --datadir . --runs runcombs_CP5.dat --mcdir mcruns_CP5/mc --weights "+weights+" --ipol=linear --ipoldir=out_CP5"+weights.replace("weights","")+"/ipol/ --outdir=out_CP5"+weights.replace("weights","")+" --params=ColourReconnection:mode=0"
  print "prof-ipolhistos --datadir . --runs runcombs_CP5-CR1.dat --mcdir mcruns_CP5-CR1/mc --weights "+weights+" --ipol=linear --ipoldir=out_CP5-CR1"+weights.replace("weights","")+"/ipol/ --outdir=out_CP5-CR1"+weights.replace("weights","")+" --params=ColourReconnection:mode=1"
  print "prof-ipolhistos --datadir . --runs runcombs_CP5-CR2o.dat --mcdir mcruns_CP5-CR2o/mc --weights "+weights+" --ipol=linear --ipoldir=out_CP5-CR2o"+weights.replace("weights","")+"/ipol/ --outdir=out_CP5-CR2o"+weights.replace("weights","")+" --params=ColourReconnection:mode=2"
  print "prof-ipolhistos --datadir . --runs runcombs_CUETP8M1.dat --mcdir mcruns_CUETP8M1/mc --weights "+weights+" --ipol=linear --ipoldir=out_CUETP8M1"+weights.replace("weights","")+"/ipol/ --outdir=out_CUETP8M1"+weights.replace("weights","")+" --params=ColourReconnection:mode=0"
  print "prof-ipolhistos --datadir . --runs runcombs_A14.dat --mcdir mcruns_A14/mc --weights "+weights+" --ipol=linear --ipoldir=out_A14"+weights.replace("weights","")+"/ipol/ --outdir=out_A14"+weights.replace("weights","")+" --params=ColourReconnection:mode=0"
  print "prof-ipolhistos --datadir . --runs runcombs_A14-CR1.dat --mcdir mcruns_A14-CR1/mc --weights "+weights+" --ipol=linear --ipoldir=out_A14-CR1"+weights.replace("weights","")+"/ipol/ --outdir=out_A14-CR1"+weights.replace("weights","")+" --params=ColourReconnection:mode=1"
  print "prof-ipolhistos --datadir . --runs runcombs_A14-CR2.dat --mcdir mcruns_A14-CR2/mc --weights "+weights+" --ipol=linear --ipoldir=out_A14-CR2"+weights.replace("weights","")+"/ipol/ --outdir=out_A14-CR2"+weights.replace("weights","")+" --params=ColourReconnection:mode=2"
  print "prof-ipolhistos --datadir . --runs runcombs_default.dat --mcdir mcruns_default/mc --weights "+weights+" --ipol=linear --ipoldir=out_default"+weights.replace("weights","")+"/ipol/ --outdir=out_default"+weights.replace("weights","")+" --params=ColourReconnection:mode=0"
  print "export RIVET_DATA_PATH=/afs/cern.ch/user/h/hinzmann/stable_13TeV/Rivet/CMSSW_9_2_6/src/Professor/ref"
  print "python renormalize.py out_CP1"+weights.replace("weights","")+"/ipolhistos/000/histo-000.yoda"
  print "python renormalize.py out_CP5"+weights.replace("weights","")+"/ipolhistos/000/histo-000.yoda"
  print "python renormalize.py out_CP5-CR1"+weights.replace("weights","")+"/ipolhistos/000/histo-000.yoda"
  print "python renormalize.py out_CP5-CR2o"+weights.replace("weights","")+"/ipolhistos/000/histo-000.yoda"
  print "python renormalize.py out_CUETP8M1"+weights.replace("weights","")+"/ipolhistos/000/histo-000.yoda"
  print "python renormalize.py out_A14"+weights.replace("weights","")+"/ipolhistos/000/histo-000.yoda"
  print "python renormalize.py out_A14-CR1"+weights.replace("weights","")+"/ipolhistos/000/histo-000.yoda"
  print "python renormalize.py out_A14-CR2"+weights.replace("weights","")+"/ipolhistos/000/histo-000.yoda"
  print "python renormalize.py out_default"+weights.replace("weights","")+"/ipolhistos/000/histo-000.yoda"
  for name in ["ISRalphaS","FSRpTmin","FSRalphaS","FSR"]:
    print "python renormalize.py out_"+name+weights.replace("weights","")+"/tunes/tune-"+weights+"-000/ipolhistos/tune-"+weights+"-000-0.yoda"

  print "rm -r out_gen_comparison"+weights.replace("weights","")
  p="rivet-cmphistos --rel-ratio -o out_gen_comparison"+weights.replace("weights","")
  p+=" out_CUETP8M1"+weights.replace("weights","")+"/ipolhistos/000/histo-000-norm.yoda:'Title=CUETP8M1'"
  p+=" out_A14"+weights.replace("weights","")+"/ipolhistos/000/histo-000-norm.yoda:'Title=A14'"
  p+=" out_CP5"+weights.replace("weights","")+"/ipolhistos/000/histo-000-norm.yoda:'Title=CP5'"
  p+=" out_default"+weights.replace("weights","")+"/ipolhistos/000/histo-000-norm.yoda:'Title=H7'"
  print p
  print "./make-plots --png out_gen_comparison"+weights.replace("weights","")+"/*.dat"
  
  print "rm -r out_tune_comparison"+weights.replace("weights","")
  p="rivet-cmphistos --rel-ratio -o out_tune_comparison"+weights.replace("weights","")
  p+=" out_CUETP8M1"+weights.replace("weights","")+"/ipolhistos/000/histo-000-norm.yoda:'Title=CUETP8M1'"
  p+=" out_A14"+weights.replace("weights","")+"/ipolhistos/000/histo-000-norm.yoda:'Title=A14'"
  p+=" out_CP5"+weights.replace("weights","")+"/ipolhistos/000/histo-000-norm.yoda:'Title=CP5'"
  p+=" out_CP1"+weights.replace("weights","")+"/ipolhistos/000/histo-000-norm.yoda:'Title=CP1'"
  for name in ["ISRalphaS","FSRpTmin","FSRalphaS"]:#,"FSR","ISRalphaS","FSRpTmin",
    p+=" out_"+name+weights.replace("weights","")+"/tunes/tune-"+weights+"-000/ipolhistos/tune-"+weights+"-000-0-norm.yoda:'Title="+name+"'"
  print p
  print "./make-plots --png out_tune_comparison"+weights.replace("weights","")+"/*.dat"
  
  print "rm -r out_cr_comparison"+weights.replace("weights","")
  p="rivet-cmphistos --rel-ratio -o out_cr_comparison"+weights.replace("weights","")
  p+=" out_A14"+weights.replace("weights","")+"/ipolhistos/000/histo-000-norm.yoda:'Title=A14'"
  p+=" out_A14-CR1"+weights.replace("weights","")+"/ipolhistos/000/histo-000-norm.yoda:'Title=A14-CR1'"
  p+=" out_A14-CR2"+weights.replace("weights","")+"/ipolhistos/000/histo-000-norm.yoda:'Title=A14-CR2'"
  p+=" out_CP5"+weights.replace("weights","")+"/ipolhistos/000/histo-000-norm.yoda:'Title=CP5'"
  p+=" out_CP5-CR1"+weights.replace("weights","")+"/ipolhistos/000/histo-000-norm.yoda:'Title=CP5-CR1'"
  p+=" out_CP5-CR2o"+weights.replace("weights","")+"/ipolhistos/000/histo-000-norm.yoda:'Title=CP5-CR2o'"
  print p
  print "./make-plots --png out_cr_comparison"+weights.replace("weights","")+"/*.dat"
