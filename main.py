import subprocess
import os

#retcode = subprocess.call("rscript --vanilla r_code/test_r_code.r r_data/socal.txt", shell=True)
#first run and display luen's code
retcode = os.system("cd r_code; rscript test_r_code.r ../r_data/socal.txt")

if int(retcode) == 0:
    print "success"
else:
    print "failed, check run stack"
