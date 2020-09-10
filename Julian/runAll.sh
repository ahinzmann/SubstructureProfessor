## Sherpa gridpack preparation
./MakeSherpaLibs.sh -p DY -o LBCR -v -m mpirun -M '-n 4'
./MakeSherpaLibs.sh -p QCD -o LBCR -v -m mpirun -M '-n 4' 

./PrepareSherpaLibs.sh -p DY &
./PrepareSherpaLibs.sh -p QCD

cp *MASTER.tgz /afs/desy.de/user/h/hinzmann/public/

## Generation
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py -c DY-Pythia8-CP5-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py -c DY-Herwig7-CH3-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py -c DY-Sherpa-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py -c QCD-Pythia8-CP5-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py -c QCD-Herwig7-CH3-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py -c QCD-Sherpa-13TeV.conf &

yodamerge -o batch_yoda_files/DY_Pythia8_CP5_Sep10/DY_Pythia8_CP5_Sep10.yoda batch_yoda_files/DY_Pythia8_CP5_Sep10/job_* &
yodamerge -o batch_yoda_files/DY_Herwig7_CH3_Sep10/DY_Herwig7_CH3_Sep10.yoda batch_yoda_files/DY_Herwig7_CH3_Sep10/job_* &
yodamerge -o batch_yoda_files/DY_Sherpa_Sep10/DY_Sherpa_Sep10.yoda batch_yoda_files/DY_Sherpa_Sep10/job_* &
yodamerge -o batch_yoda_files/QCD_Pythia8_CP5_Sep10/QCD_Pythia8_CP5_Sep10.yoda batch_yoda_files/QCD_Pythia8_CP5_Sep10/job_* &
yodamerge -o batch_yoda_files/QCD_Herwig7_CH3_Sep10/QCD_Herwig7_CH3_Sep10.yoda batch_yoda_files/QCD_Herwig7_CH3_Sep10/job_* &
yodamerge -o batch_yoda_files/QCD_Sherpa_Sep10/QCD_Sherpa_Sep10.yoda batch_yoda_files/QCD_Sherpa_Sep10/job_*

## Plotting
./comparePlotsDY.sh &
./comparePlotsQCD.sh
