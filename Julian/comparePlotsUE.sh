#!/bin/bash

function compareUEPlots {
FILENAME1=P8_CR0_UE_AlphaS_0123
FILENAME2=P8_CR1_UE_AlphaS_0123
FILENAME3=P8_CR2_UE_AlphaS_0123
##FILENAME4=P8_CR0_UE_all4AlphaS_0123
##FILENAME5=P8_CR0_UE_all4AlphaS_0136
rivet-mkhtml -o rivet_plots_all/P8_CRs_UE_AlphaS_0123 -s \
$FILENAME1.yoda:'Title=P8 CR0 $\alpha_{S} = 0.123$':'ErrorBars=1':'PolyMarker=' \
$FILENAME2.yoda:'Title=P8 CR1 $\alpha_{S} = 0.123$':'ErrorBars=1':'PolyMarker=' \
$FILENAME3.yoda:'Title=P8 CR2 $\alpha_{S} = 0.123$':'ErrorBars=1':'PolyMarker=' \
`##$FILENAME4.yoda:'Title=P8 CR0 $\alpha_{S,all} = 0.123$':'ErrorBars=1':'PolyMarker='` \
`##$FILENAME5.yoda:'Title=P8 CR0 $\alpha_{S,all} = 0.136$':'ErrorBars=1':'PolyMarker='`
}

YELLOW='\033[1;33m'
RED='\033[1;31m'
NORMAL='\033[0m'

compareUEPlots 2>&1 | {
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
