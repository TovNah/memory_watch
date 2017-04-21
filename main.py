from subprocess import Popen, PIPE
import sys
import subprocess, datetime
import os
import time
import Windows
from PyQt5.QtWidgets import QApplication, QWidget
# import logbook

# notify-send -i "path/to/icon.png" \
# "Title (bold)" \
# "Text Line1
# Text Line2
# Text Line3"
# log = logbook.Logger('APP')
# handler = logbook.FileHandler('app.log')
totalMem = 0 
freeMem = 0
cached = 0

def main():
      log_info('WAKE UP, NEO.')
      do()
      
      log_info('SLEEP')
      # time.sleep(60) 

def do() :

  # app = QApplication(sys.argv)
  # ex = Windows.Windows()
  # sys.exit(app.exec_())
  show_mem_stat()
  update_mem_stat()
  if get_proc_free() < 10.0 :
    # log_info("\n\n" + get_top_processes())
    show_mem_stat()
        
  if int(cached) > 1000 :
    clear_cache()
    
def update_mem_stat() :
  free = Popen("free -m", shell=True, stdin=PIPE, stdout=PIPE).stdout.read().split()
  global totalMem 
  global freeMem
  global cached

  totalMem = free[7].decode("utf-8") 
  freeMem = free[9].decode("utf-8") 
  cached = free[11].decode("utf-8") 

def clear_cache() :
  reset = Popen(". /home/bolotov-aa/bin/mem_watch/reset.sh", shell=True, stdin=PIPE, stdout=PIPE).stdout.read().decode("utf-8")
  # log_info(reset)

def show_mem_stat() :
  update_mem_stat()

  log_info('SHOW NOTIFY1')

  arg1 = "Free %.1f" % get_proc_free() +"% " + freeMem + "Mb cached " + cached + "Mb"
  arg2 = get_top_processes()

  log_info("STAT " + arg1)

  subprocess.Popen([". notify-send " + arg1 + " " + arg2])

def show_mem_stat_without_proc():
  update_mem_stat()

  log_info('SHOW NOTIFY2')

  
  arg1 = "Free %.1f" % get_proc_free() +"% " + freeMem + "Mb cached " + cached + "Mb"
  log_info("STAT " + arg1)
  subprocess.Popen(["sh", "send_notify.sh", arg1], shell=True, stdin=PIPE, stdout=PIPE)

def get_top_processes() :
  return Popen(". /home/bolotov-aa/bin/mem_watch/processes.sh", shell=True, stdin=PIPE, stdout=PIPE).stdout.read().decode("utf-8")

def get_proc_free():
  return 100 / int(totalMem) * int(freeMem)

def log_info(msg):
  now = datetime.datetime.now()
  print(str(now) + ": " + msg)

if __name__ == "__main__":
  log_info('INIT')
  main()
