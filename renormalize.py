import sys
files=[sys.argv[1]]
for f in files:
 outf=open(f.replace(".yoda","-norm.yoda"),"w")
 inf=open(f)
 correct=False
 for l in inf.readlines():
   split=l.split("	")
   if "YODA_SCATTER2D" in l: correct=False
   if "CMS_2018_SMP_16_010" in l: correct=True
   if len(split)==6 and not "val" in l and correct:
     #if "5.000000e-01	5.000000e-01	5.000000e-01" in l: continue
     #if "3.000000e+00	2.000000e+00	2.000000e+00" in l: continue
     #if "7.500000e+00	2.500000e+00	2.500000e+00" in l: continue
     lout="   ".join([split[0],split[1],split[2],str(float(split[3])/1000.),str(float(split[4])/1000.)])+"\n"
   else:
     lout=l
   outf.write(lout)
 inf.close()
 outf.close()
