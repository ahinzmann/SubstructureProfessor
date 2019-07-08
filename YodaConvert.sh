#!/bin/sh

cd $1/mc/
for i in `ls` ; do
        cd ${i}
        echo ${i}
        /afs/cern.ch/user/h/hinzmann/stable_13TeV/Rivet/CMSSW_9_2_6/src/Professor/yoda2aida *.yoda
        cd ../
done;
cd ../../
