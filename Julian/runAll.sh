## Sherpa gridpack preparation
./MakeSherpaLibs.sh -p DY -o LBCR -v -m mpirun -M '-n 4'
./MakeSherpaLibs.sh -p DYLO -o LBCR -v -m mpirun -M '-n 4'
./MakeSherpaLibs.sh -p DYNLO -o LBCR -v -m mpirun -M '-n 4'
./MakeSherpaLibs.sh -p DYNLOM -o LBCR -v -m mpirun -M '-n 4'
./MakeSherpaLibs.sh -p QCD -o LBCR -v -m mpirun -M '-n 4' 
./MakeSherpaLibs.sh -p QCDLO -o LBCR -v -m mpirun -M '-n 4' 
./MakeSherpaLibs.sh -p QCDNLO -o LBCR -v -m mpirun -M '-n 4' 
./MakeSherpaLibs.sh -p QCDNLOM -o LBCR -v -m mpirun -M '-n 4' 

./PrepareSherpaLibs.sh -p DY
./PrepareSherpaLibs.sh -p DYLO
./PrepareSherpaLibs.sh -p DYNLO
./PrepareSherpaLibs.sh -p DYNLOM
./PrepareSherpaLibs.sh -p QCD
./PrepareSherpaLibs.sh -p QCDLO
./PrepareSherpaLibs.sh -p QCDNLO
./PrepareSherpaLibs.sh -p QCDNLOM

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
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py DY-Sherpa-LO-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py DY-Sherpa-NLO-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py DY-Sherpa-NLOM-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py QCD-Sherpa-LO-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py QCD-Sherpa-NLO-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py QCD-Sherpa-NLOM-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py DY-Pythia8-CP2-13TeV.conf &
/afs/desy.de/user/h/hinzmann/grid-control/grid-control/go.py QCD-Pythia8-CP2-13TeV.conf &

mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Pythia8_CP5_Nov26/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Herwig7_Nov26/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Sherpa_Nov26/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Pythia8_CP5_Nov26/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Herwig7_Nov26/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Sherpa_Nov26/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Herwig7_CH3_Nov26/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Herwig7_CH3_Nov26/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Sherpa_LO_Nov26/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Sherpa_NLO_Nov26/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Sherpa_NLOM_Nov26/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Sherpa_LO_Nov26/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Sherpa_NLO_Nov26/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Sherpa_NLOM_Nov26/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Pythia8_CP2_Nov26/ &
mkdir /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Pythia8_CP2_Nov26/ &

mv batch_yoda_files/DY_Pythia8_CP5_Nov26/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Pythia8_CP5_Nov26/ &
mv batch_yoda_files/DY_Herwig7_Nov26/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Herwig7_Nov26/ &
mv batch_yoda_files/DY_Sherpa_Nov26/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Sherpa_Nov26/ &
mv batch_yoda_files/QCD_Pythia8_CP5_Nov26/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Pythia8_CP5_Nov26/ &
mv batch_yoda_files/QCD_Herwig7_Nov26/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Herwig7_Nov26/ &
mv batch_yoda_files/QCD_Sherpa_Nov26/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Sherpa_Nov26/ &
mv batch_yoda_files/DY_Herwig7_CH3_Nov26/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Herwig7_CH3_Nov26/ &
mv batch_yoda_files/QCD_Herwig7_CH3_Nov26/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Herwig7_CH3_Nov26/ &
mv batch_yoda_files/DY_Sherpa_LO_Nov26/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Sherpa_LO_Nov26/ &
mv batch_yoda_files/DY_Sherpa_NLO_Nov26/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Sherpa_NLO_Nov26/ &
mv batch_yoda_files/DY_Sherpa_NLOM_Nov26/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Sherpa_NLOM_Nov26/ &
mv batch_yoda_files/QCD_Sherpa_LO_Nov26/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Sherpa_LO_Nov26/ &
mv batch_yoda_files/QCD_Sherpa_NLO_Nov26/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Sherpa_NLO_Nov26/ &
mv batch_yoda_files/QCD_Sherpa_NLOM_Nov26/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Sherpa_NLOM_Nov26/ &
mv batch_yoda_files/DY_Pythia8_CP2_Nov26/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Pythia8_CP2_Nov26/ &
mv batch_yoda_files/QCD_Pythia8_CP2_Nov26/* /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Pythia8_CP2_Nov26/ &

yodamerge -o yoda_files/DY_Pythia8_CP5_Nov26.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Pythia8_CP5_Nov26/job_* &
yodamerge -o yoda_files/DY_Herwig7_Nov26.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Herwig7_Nov26/job_* &
yodamerge -o yoda_files/DY_Sherpa_Nov26.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Sherpa_Nov26/job_* &
yodamerge -o yoda_files/QCD_Pythia8_CP5_Nov26.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Pythia8_CP5_Nov26/job_* &
yodamerge -o yoda_files/QCD_Herwig7_Nov26.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Herwig7_Nov26/job_* &
yodamerge -o yoda_files/QCD_Sherpa_Nov26.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Sherpa_Nov26/job_* &
yodamerge -o yoda_files/DY_Herwig7_CH3_Nov26.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Herwig7_CH3_Nov26/job_* &
yodamerge -o yoda_files/QCD_Herwig7_CH3_Nov26.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Herwig7_CH3_Nov26/job_* &
yodamerge -o yoda_files/DY_Sherpa_LO_Nov26.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Sherpa_LO_Nov26/job_* &
yodamerge -o yoda_files/DY_Sherpa_NLO_Nov26.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Sherpa_NLO_Nov26/job_* &
yodamerge -o yoda_files/DY_Sherpa_NLOM_Nov26.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Sherpa_NLOM_Nov26/job_* &
yodamerge -o yoda_files/QCD_Sherpa_LO_Nov26.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Sherpa_LO_Nov26/job_* &
yodamerge -o yoda_files/QCD_Sherpa_NLO_Nov26.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Sherpa_NLO_Nov26/job_* &
yodamerge -o yoda_files/QCD_Sherpa_NLOM_Nov26.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Sherpa_NLOM_Nov26/job_* &
yodamerge -o yoda_files/DY_Pythia8_CP2_Nov26.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/DY_Pythia8_CP2_Nov26/job_* &
yodamerge -o yoda_files/QCD_Pythia8_CP2_Nov26.yoda /nfs/dust/cms/user/hinzmann/batch_yoda_files/QCD_Pythia8_CP2_Nov26/job_* &

## Plotting
./comparePlotsDY.sh &
./comparePlotsQCD.sh
