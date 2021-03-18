#!/bin/bash

function comparePlots {
FILENAME1=DY_Sherpa_LO_Mar16
FILENAME2=DY_Sherpa_LOM_Mar16
FILENAME3=DY_Sherpa_NLO_Mar16
#FILENAME4=P8_CP5_DIJET_AlphaS_0118_Gregory_mmdt_Sep8
#FILENAME5=P8_CR0_DIJET_AlphaS_0136
./rivet-mkhtml -o rivet_plots_all/ZPJ_Mar16sherpa -c ../../Rivet/SMP/data/CMS_2018_PAS_SMP_18_QGX_ZPJ.plot \
`## 2016 data, selection/trigger similar to the analysis` \
../../Rivet/SMP/data/CMS_2018_PAS_SMP_18_QGX_ZPJ.yoda:'Title=Unfolded data':'ErrorBands=1' \
`## MY ANALYSIS` \
yoda_files/$FILENAME1.yoda:'Title=Sherpa 2.2.10 LO':'ErrorBars=1' \
yoda_files/$FILENAME2.yoda:'Title=Sherpa 2.2.10 LO+jet':'ErrorBars=1' \
yoda_files/$FILENAME3.yoda:'Title=Sherpa 2.2.10 NLO':'ErrorBars=1' \
`## $FILENAME4.yoda:'Title=P8 mMDT (E for thrust, WTA else)':'ErrorBars=1'` \
`## $FILENAME5.yoda:'Title=P8 CR0 DIJET $\alpha_{S}=0.136$':'ErrorBars=1'`
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
