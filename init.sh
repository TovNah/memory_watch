#устанавливаем демона для питона
sudo apt-get install supervisor
sudo apt install python-logbook 

#настраиваем конфиги для демона
sudo echo  -e '[program:mem_watch] \n'\
'command = python3 '$(pwd)'/main.py \n'\
'autorestart = true \n'\
'stderr_logfile = /var/log/mem_watch.err.log \n'\
'autostart=true \n'\
'stdout_logfile='$(pwd)'/app_sd.log \n'\
'stdout_logfile_maxbytes=50MB \n'\
'stdout_logfile_backups=50 \n'\
'stdout_logfile = /var/log/mem_watch.log' >  /etc/supervisor/conf.d/mem_watch1.conf
 
#стартуем демона
sudo service supervisor start
supervisorctl reread
