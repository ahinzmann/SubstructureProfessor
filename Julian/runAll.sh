## Sherpa gridpack preparation
./MakeSherpaLibs.sh -p DY -o LBCR -v -m mpirun -M '-n 4'
./MakeSherpaLibs.sh -p QCD -o LBCR -v -m mpirun -M '-n 4' 

./PrepareSherpaLibs.sh -p DY
./PrepareSherpaLibs.sh -p QCD

cp *MASTER.tgz /afs/desy.de/user/h/hinzmann/public/

## Generation
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py DY-Pythia8-CP5-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py DY-Herwig7-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py DY-Sherpa-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py QCD-Pythia8-CP5-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py QCD-Herwig7-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py QCD-Sherpa-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py DY-Herwig7-CH3-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py QCD-Herwig7-CH3-13TeV.conf &

mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Pythia8_CP5_Oct22/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Herwig7_Oct22/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Sherpa_Oct22/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Pythia8_CP5_Oct22/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Herwig7_Oct22/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Sherpa_Oct22/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Herwig7_CH3_Oct22/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Herwig7_CH3_Oct22/ &

mv batch_yoda_files/DY_Pythia8_CP5_Oct22/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Pythia8_CP5_Oct22/ &
mv batch_yoda_files/DY_Herwig7_Oct22/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Herwig7_Oct22/ &
mv batch_yoda_files/DY_Sherpa_Oct22/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Sherpa_Oct22/ &
mv batch_yoda_files/QCD_Pythia8_CP5_Oct22/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Pythia8_CP5_Oct22/ &
mv batch_yoda_files/QCD_Herwig7_Oct22/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Herwig7_Oct22/ &
mv batch_yoda_files/QCD_Sherpa_Oct22/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Sherpa_Oct22/ &
mv batch_yoda_files/DY_Herwig7_CH3_Oct22/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Herwig7_CH3_Oct22/ &
mv batch_yoda_files/QCD_Herwig7_CH3_Oct22/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Herwig7_CH3_Oct22/ &

yodamerge -o yoda_files/DY_Pythia8_CP5_Oct22.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Pythia8_CP5_Oct22/job_* &
yodamerge -o yoda_files/DY_Herwig7_Oct22.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Herwig7_Oct22/job_* &
yodamerge -o yoda_files/DY_Sherpa_Oct22.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Sherpa_Oct22/job_* &
yodamerge -o yoda_files/QCD_Pythia8_CP5_Oct22.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Pythia8_CP5_Oct22/job_* &
yodamerge -o yoda_files/QCD_Herwig7_Oct22.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Herwig7_Oct22/job_* &
yodamerge -o yoda_files/QCD_Sherpa_Oct22.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Sherpa_Oct22/job_* &
yodamerge -o yoda_files/DY_Herwig7_CH3_Oct22.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Herwig7_CH3_Oct22/job_* &
yodamerge -o yoda_files/QCD_Herwig7_CH3_Oct22.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Herwig7_CH3_Oct22/job_* &

## Plotting
./comparePlotsDY.sh &
./comparePlotsQCD.sh
