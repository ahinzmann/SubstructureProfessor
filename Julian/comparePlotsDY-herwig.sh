#!/bin/bash

function comparePlots {
FILENAME1=DY_Herwig7_Nov26
FILENAME2=DY_Herwig7_CH3_Nov26
FILENAME3=DY_Pythia8_CP5_Nov26
#FILENAME4=P8_CP5_DIJET_AlphaS_0118_Gregory_mmdt_Sep8
##FILENAME5=P8_CR0_DIJET_AlphaS_0136
rivet-mkhtml -o rivet_plots_all/ZPJ_Nov26herwig -c ../../Rivet/SMP/data/CMS_2018_PAS_SMP_18_QGX_ZPJ.plot \
`## 2016 data, selection/trigger similar to the analysis` \
../../Rivet/SMP/data/CMS_2018_PAS_SMP_18_QGX_ZPJ.yoda:'Title=Unfolded data':'ErrorBands=1' \
`## MY ANALYSIS` \
yoda_files/$FILENAME1.yoda:'Title=Herwig 7.20':'ErrorBars=1' \
yoda_files/$FILENAME2.yoda:'Title=Herwig 7.14 CH3':'ErrorBars=1' \
yoda_files/$FILENAME3.yoda:'Title=Pythia 8.243 CP5':'ErrorBars=1' \
`##$FILENAME4.yoda:'Title=P8 mMDT (E for thrust, WTA else)':'ErrorBars=1'` \
`##$FILENAME5.yoda:'Title=P8 CR0 DIJET $\alpha_{S}=0.136$':'ErrorBars=1'`
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
