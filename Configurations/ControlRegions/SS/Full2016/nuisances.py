
# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py 

################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

nuisances['lumi']  = {
               'name'  : 'lumi_13TeV',
               'samples'  : {
                   'DY'       : '1.023',    
                   'top'      : '1.023',    
                   'WW'       : '1.023',    
                   'ggWW'     : '1.023',
                   'Vg'       : '1.023',
                   'VgS'      : '1.023',
                   'VZ'       : '1.023',
                   'VVV'      : '1.023',
                   'ggH_hww'  : '1.023',
                   'qqH_hww'  : '1.023',
                   'ZH_hww'   : '1.023',
                   'ggZH_hww' : '1.023',
                   'WH_hww'   : '1.023',
                   'bbH_hww'  : '1.023',
                   'H_htt'    : '1.023',
                   },
               'type'  : 'lnN',
              }

#### FAKES

if Nlep == '2' :
  # already divided by central values in formulas !
  fakeW_EleUp       = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp'
  fakeW_EleDown     = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown'
  fakeW_MuUp        = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp'
  fakeW_MuDown      = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown'
  fakeW_statEleUp   = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp'
  fakeW_statEleDown = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown'
  fakeW_statMuUp    = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp'
  fakeW_statMuDown  = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown'

else:
  fakeW_EleUp       = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lElUp       / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_EleDown     = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lElDown     / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_MuUp        = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lMuUp       / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_MuDown      = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lMuDown     / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_statEleUp   = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatElUp   / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_statEleDown = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatElDown / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_statMuUp    = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatMuUp   / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_statMuDown  = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatMuDown / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'

nuisances['fake_syst']  = {
               'name'  : 'fake_syst',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake' : '1.30',
                             },
}

nuisances['fake_ele']  = {
                'name'  : 'fake_ele_hww',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_EleUp , fakeW_EleDown ],
                             },
}

nuisances['fake_ele_stat']  = {
                'name'  : 'fake_ele_stat_hww',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'      : [ fakeW_statEleUp , fakeW_statEleDown ]
                             },
}

nuisances['fake_mu']  = {
                'name'  : 'fake_mu_hww',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_MuUp , fakeW_MuDown ],
                             },
}


nuisances['fake_mu_stat']  = {
                'name'  : 'fake_mu_stat_hww',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_statMuUp , fakeW_statMuDown ]
                             },
}

##### B-tagger

nuisances['btagbc']  = {
                'name'  : 'Full2016_btag_bc',
                'kind'  : 'weight',
               'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WW'      : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ggWW'    : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'VVV'     : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'VZ'      : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'top'     : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'Vg'      : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'VgS'     : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ggH_hww' : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'qqH_hww' : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WH_hww'  : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ZH_hww'  : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'H_htt'   : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'bbH_hww' : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                }
}

nuisances['btagudsg']  = {
                'name'  : 'Full2016_btag_udsg',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'VVV'     : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'VZ'      : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WW'      : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ggWW'    : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'top'     : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'Vg'      : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'VgS'     : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ggH_hww' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'qqH_hww' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WH_hww'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ZH_hww'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'bbH_hww' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'H_htt'   : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                }
}

##### Trigger Efficiency

if   Nlep == '2' : trig_syst = ['(effTrigW_Up)/(effTrigW)', '(effTrigW_Down)/(effTrigW)']
elif Nlep == '3' : trig_syst = ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)']
# !!!!! We don't have the trigger formula implemented for 4l !!!! -> Use 3l but not correct
elif Nlep == '4' : trig_syst = ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)']

nuisances['trigg']  = {
                'name'  : 'trigger',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : trig_syst ,
                   'VVV'     : trig_syst ,
                   'VZ'      : trig_syst ,
                   'ggWW'    : trig_syst ,
                   'WW'      : trig_syst ,
                   'top'     : trig_syst ,
                   'Vg'      : trig_syst ,
                   'VgS'     : trig_syst ,
                   'ggH_hww' : trig_syst ,
                   'qqH_hww' : trig_syst ,
                   'WH_hww'  : trig_syst ,
                   'ZH_hww'  : trig_syst ,
                   'ggZH_hww': trig_syst ,
                   'bbH_hww' : trig_syst ,
                   'H_htt'   : trig_syst ,
                },
}

##### Electron Efficiency and energy scale

id_syst_ele = [ 'LepSF'+Nlep+'l__ele_'+eleWP+'__Up' , 'LepSF'+Nlep+'l__ele_'+eleWP+'__Do' ]

nuisances['idiso_ele']  = {
                'name'  : 'idiso_ele',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : id_syst_ele ,
                   'VVV'     : id_syst_ele ,
                   'VZ'      : id_syst_ele ,
                   'ggWW'    : id_syst_ele ,
                   'WW'      : id_syst_ele ,
                   'top'     : id_syst_ele ,
                   'Vg'      : id_syst_ele ,
                   'VgS'     : id_syst_ele ,
                   'ggH_hww' : id_syst_ele ,
                   'qqH_hww' : id_syst_ele ,
                   'WH_hww'  : id_syst_ele ,
                   'ZH_hww'  : id_syst_ele ,
                   'ggZH_hww': id_syst_ele ,
                   'bbH_hww' : id_syst_ele ,
                   'H_htt'   : id_syst_ele ,
                },
}

nuisances['electronpt']  = {
                'name'  : 'scale_e',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'DY' :  ['1', '1'],
                   'ggWW' :['1', '1'],
                   'WW' :  ['1', '1'],
                   'top' : ['1', '1'],
                   'VZ' :  ['1', '1'],
                   'VVV' : ['1', '1'],
                   'Vg' : ['1', '1'],
                   'VgS': ['1', '1'],
                   'ggH_hww' : ['1', '1'],
                   'qqH_hww' : ['1', '1'],
                   'WH_hww'  :  ['1', '1'],
                   'ZH_hww'  :  ['1', '1'],
                   'ggZH_hww':  ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'H_htt'   : ['1', '1'],
                 },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__LepElepTup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__LepElepTdo'+skim,
}


##### Muon Efficiency and energy scale

id_syst_mu = [ 'LepSF'+Nlep+'l__mu_'+muWP+'__Up' , 'LepSF'+Nlep+'l__mu_'+muWP+'__Do' ]

nuisances['idiso_mu']  = {
                'name'  : 'idiso_mu',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : id_syst_mu ,
                   'VVV'     : id_syst_mu ,
                   'VZ'      : id_syst_mu ,
                   'ggWW'    : id_syst_mu ,
                   'WW'      : id_syst_mu ,
                   'top'     : id_syst_mu ,
                   'Vg'      : id_syst_mu ,
                   'VgS'     : id_syst_mu ,
                   'ggH_hww' : id_syst_mu ,
                   'qqH_hww' : id_syst_mu ,
                   'WH_hww'  : id_syst_mu ,
                   'ZH_hww'  : id_syst_mu ,
                   'ggZH_hww': id_syst_mu ,
                   'bbH_hww' : id_syst_mu ,
                   'H_htt'   : id_syst_mu ,
                },
}

nuisances['muonpt']  = {
                'name'  : 'scale_m',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'ggWW' :['1', '1'],
                   'WW' :  ['1', '1'],
                   'DY' :  ['1', '1'],
                   'top' : ['1', '1'],
                   'VZ' :  ['1', '1'],
                   'VVV' : ['1', '1'],
                   'Vg' : ['1', '1'],
                   'VgS': ['1', '1'],
                   'ggH_hww' : ['1', '1'],
                   'qqH_hww' : ['1', '1'],
                   'WH_hww' :  ['1', '1'],
                   'ZH_hww' :  ['1', '1'],
                   'ggZH_hww':  ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'H_htt' : ['1', '1'],
                },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__LepMupTup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__LepMupTdo'+skim,
}


##### Jet energy scale

nuisances['jes']  = {
                'name'  : 'scale_j',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'ggWW' :['1', '1'],
                   'WW' :  ['1', '1'],
                   'DY' :  ['1', '1'],
                   'top' : ['1', '1'],
                   'VZ' :  ['1', '1'],
                   'VVV' : ['1', '1'],
                   'Vg' : ['1', '1'],
                   'VgS': ['1', '1'],
                   'ggH_hww' : ['1', '1'],
                   'qqH_hww' : ['1', '1'],
                   'WH_hww' :  ['1', '1'],
                   'ZH_hww' :  ['1', '1'],
                   'ggZH_hww':  ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'H_htt' : ['1', '1'],
                },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__JESup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__JESdo'+skim,
}

##### MET energy scale

nuisances['met']  = {
                'name'  : 'scale_met',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'ggWW' :['1', '1'],
                   'WW' :  ['1', '1'],
                   'DY' :  ['1', '1'],
                   'top' : ['1', '1'],
                   'VZ' :  ['1', '1'],
                   'VVV' : ['1', '1'],
                   'Vg' : ['1', '1'],
                   'VgS': ['1', '1'],
                   'ggH_hww' : ['1', '1'],
                   'qqH_hww' : ['1', '1'],
                   'WH_hww' :  ['1', '1'],
                   'ZH_hww' :  ['1', '1'],
                   'ggZH_hww':  ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'H_htt' : ['1', '1'],
                },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__METup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__METdo'+skim,
}

