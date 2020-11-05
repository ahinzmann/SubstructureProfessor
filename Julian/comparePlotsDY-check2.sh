#!/bin/bash

function comparePlots {
FILENAME1=DY_Pythia8_CP5_Oct29
FILENAME2=DY_Pythia8_CP5_Oct27
#FILENAME3=DY_Pythia8_CP5_Oct22
#FILENAME4=DY_Pythia8_CP5_Sep10
#FILENAME5=DY_Pythia8_CP5_Oct1
rivet-mkhtml -o rivet_plots_all/ZPJ_Oct29check -c ../../Rivet/SMP/data/CMS_2018_PAS_SMP_18_QGX_ZPJ.plot \
`## 2016 data, selection/trigger similar to the analysis` \
`##../../Rivet/SMP/data/CMS_2018_PAS_SMP_18_QGX_ZPJ.yoda:'Title=Unfolded data':'ErrorBands=1'` \
`## MY ANALYSIS` \
yoda_files/$FILENAME1.yoda:'Title=P8 CP5 cluster charged':'ErrorBars=1' \
yoda_files/$FILENAME2.yoda:'Title=P8 CP5 ':'ErrorBars=1' \
`##yoda_files/$FILENAME3.yoda:'Title=P8 CP5 n>=2':'ErrorBars=1'` \
`##yoda_files/$FILENAME4.yoda:'Title=P8 CP5 2jet':'ErrorBars=1'` \
`##yoda_files/$FILENAME5.yoda:'Title=P8 CP5':'ErrorBars=1'`
}

YELLOW='\033[1;33m'
RED='\033[1;31m'
NORMAL='\033[0m'

comparePlots 2>&1 | {
while IFS= read -r line
do
    if [[ $line == M*ing* ]]
    then echo $line
    elif [[ $line == *remaining* ]]
    then echo $line
    elif [[ $line == *Rivet.AnalysisLoader* ]]
    then echo -e $YELLOW $line $NORMAL
    elif [[ $line == *[eE][rR][rR][oO][rR]* ]]
    then echo -e $RED $line $NORMAL
    fi
done
}
