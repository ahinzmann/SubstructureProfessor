#!/bin/env python

# v2 - March 2014 - yoda-files can now be named whatever in the config files

from optparse import OptionParser

import os, sys, re
import time


#
### Parser stuff
#

parser = OptionParser()

def parse_range(astr):
    result=set()
    for part in astr.split(','):
        run=part.split('-')
        result.update(range(int(run[0]),int(run[-1])+1))
    return sorted(result)
    
parser.add_option("-r", "--runs", action="store", help="Runs you want to submit, example: -r 0-13,16,18-22 (default=000)", default="000")
parser.add_option("-d", "--directory", action="store", help="Directory (default=mcruns)", default='mcruns')
parser.add_option("-c", "--configfile", action="store", help="Configuration file for cmsRun (default=rivet_cfg.py) \n Should exist in each in DIRECTOR/RUN", default='rivet_cfg.py')
parser.add_option("-q", "--batchque", action="store", help="Which batch que (default=1nh)", default='1nh')

(opts, args) = parser.parse_args()
opts.runs=parse_range(opts.runs)

#
### ask_ok
#
def ask_ok(prompt, retries=4, complaint='You need to answer y/ye/yes or n/no!!!'):
  while True:
    ok = raw_input(prompt)
    if ok in ('y', 'ye', 'yes'): return True
    if ok in ('n', 'no'): sys.exit()
    retries = retries - 1
    if retries < 0: raise IOError('refusenik user')
    print complaint

#
### function to get the name of the output-yoda from the config-file
#
def getyodaname(conffile):
  with open(conffile,"r") as inFile:
    for line in inFile:
      if "rivetAnalyzer" and "OutputFile" and "yoda" in line:
        return re.search("\'(.+?)\'", line).group(1)
  inFile.closed

#
### Builder Classes
#
class CommandBuilder:
  def __init__(self, name):
    self._name = name
  def build(self):
    try:
      os.cd(self._name)
      inputfile = open('bjob_'+name+'.sub', 'w')
      infile += '#!/bin/bash'
      infile += 'echo "hello world from "'+name
    except Exception, e:
      print "Error: %s" % str(e)  

class LXBATCHCommandBuilder(CommandBuilder):
  def __init__(self, name, directory, configfile, que, yodaout):
    CommandBuilder.__init__(self, name);
    self._directory=directory
    self._configfile=configfile
    self._que=que
    self._yodaout=yodaout
  def build(self):
    try:
      cmsswbase = os.getenv('CMSSW_BASE')
      if cmsswbase is None:
        print "you have to run cmsenv in your working area first!"
        return
      
      fulldir = os.getcwd()+"/"+self._directory+"/"+self._name
     
      scriptname="bjob_"+self._name+"_"+self._yodaout.strip(".yoda")+".sh"
      script = open(fulldir+"/"+scriptname, "w")
      infile=''
      infile += '#!/bin/bash\n'
      infile += 'pwd=`pwd`\n'
      infile += 'echo $pwd\n'
      infile += 'cd '+cmsswbase+'/src\n'
      infile += 'eval `scram runtime -sh`\n'
      infile += 'cd '+fulldir+'\n'
      infile += 'cmsRun ' + self._configfile + ' >& log_GEN_'+self._name+"_"+self._yodaout.strip(".yoda")+'.txt\n' #changed &> to >&
      infile += 'ls\n'
      script.write(infile)
      script.close()
      submitname="bjob_"+self._name+"_"+self._yodaout.strip(".yoda")+".sub"
      submit = open(fulldir+"/"+submitname, "w")
      infile=''
      infile += 'executable            = '+fulldir+"/"+scriptname+'\n'
      infile += 'arguments             = $(ClusterID) $(ProcId)\n'
      infile += 'output                = '+fulldir+"/"+submitname+'.$(ClusterId).$(ProcId).out\n'
      infile += 'error                 = '+fulldir+"/"+submitname+'.$(ClusterId).$(ProcId).err\n'
      infile += 'log                   = '+fulldir+"/"+submitname+'.$(ClusterId).log\n'
      infile += 'queue\n'
      submit.write(infile)
      submit.close()
      print "Run " + self._name + ":   "
      os.system('cd '+fulldir+';chmod u+x ' + scriptname+'; condor_submit '+submitname)
    except Exception, e:
      print "%s" % str(e) 
      ask_ok('Continue script? (y/n)');

 
#
## Loop the requested runs
#
misscounter = 0
for irun in opts.runs:
  if (irun >= 100):
    run_str='%i' % irun
  elif (irun >= 10 and irun < 100):
    run_str='0%i' % irun
  elif (irun < 10):
    run_str='00%i' % irun

  # get the name of the output .yoda-file
  yodafile_str = getyodaname(os.getcwd()+'/'+opts.directory+'/'+run_str+'/'+opts.configfile)

  if (os.path.exists(os.getcwd()+'/'+opts.directory+'/'+run_str+'/'+yodafile_str)==1):
    print "Run " + run_str + ": \n " + yodafile_str + " yodafile_str already exist   "
  else:
    misscounter=misscounter+1
#    if (irun>0): time.sleep(2) #Don't overload batch. Needed?
    commandBuilder = LXBATCHCommandBuilder(run_str, opts.directory, opts.configfile, opts.batchque,yodafile_str) 
    command = commandBuilder.build()


print "\n %i jobs submitted. \n" % misscounter
#AK   if ((os.path.exists(os.getcwd()+'/'+opts.directory+'/'+run_str+'/out.yoda'))==0):
#AK     misscounter = misscounter +1 
#AK     print "Run " + run_str + ": missing   %i "  % misscounter
