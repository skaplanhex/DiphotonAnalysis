for lt in ("100K","2000","3000","3500","4000","4500","5000","6000"):
    for p in ("150-500","500-Inf"):
        cfi="ADDGravitontoGG_M1200_LambdaT%s_pTHat%s_cfi"%(lt,p)
        print "cmsRun diphotonanalyzer_cfg.py inputCfi=%s outfilename=plots_LambdaTStudy_LambdaT%s_pTHat%s.root"%(cfi,lt,p)