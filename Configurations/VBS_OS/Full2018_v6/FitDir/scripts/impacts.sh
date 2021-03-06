#!/bin/bash

## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/m/mlizzo/work/CMSSW_10_2_13
eval `scramv1 runtime -sh`
cd -

## FIXME this is your work directory
workdir=/afs/cern.ch/work/m/mlizzo/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_OS/Full2018_v6/FitDir
workspaceDir=workspaces

combineTool.py -M Impacts -d ${workspaceDir}/mjj.root -m 125 -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --X-rtd MINIMIZER_analytic --doInitialFit
combineTool.py -M Impacts -d ${workspaceDir}/mjj.root -m 125 -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --X-rtd MINIMIZER_analytic --doFits
combineTool.py -M Impacts -d ${workspaceDir}/mjj.root -m 125 -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs --X-rtd MINIMIZER_analytic -o ${workspaceDir}/impacts_2018_mjj.json 

plotImpacts.py -i ${workspaceDir}/impacts_2018_mjj.json -o ${workspaceDir}/impacts_2018_mjj

cd $workdir
