import os
import subprocess

def wget_dl(url):
        try:
            print("බාගත කිරීම ආරම්භ විය")
            # i was facing some problem in filename That's Why i did this ,
            #  i will fix it later :(

            filename = os.path.basename(url)
            output = subprocess.check_output("wget '--output-document' '{}' '{}' ".format(filename , url), stderr=subprocess.STDOUT, shell=True)
            
            print("බාගත කිරීම සම්පූර්ණයි",filename)
            return filename
        except Exception as e:
            print("දෝෂය බාගන්න :",e)
           
            return "error",filename
        
# wget_dl(url)
