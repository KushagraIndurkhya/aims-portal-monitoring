# Aims-Portal-Utillity
A Monitoring tool for IIITR Students which can be used to calculate current cgpa and to automate the task of checking the aims portal for result updates

## Cloning the repo
- clone the repo and install requirements

```git clone https://github.com/KushagraIndurkhya/aims-portal-monitoring.git ; cd aims-portal-monitoring; pip3 install -r requirements.txt```

## Obtaining cookie
Login to https://aims.iiitr.ac.in/
go to dev tools (```ctrl+shift+i```) and copy the valu of JSESSIONID from cookie
![Dev Tools](/static/cookie.png)

## Running the script
- run the python script
  - for linux ```python3 aims.py```
  - for windows ```python aims.py```
- enter the copied cookie
- Your Current cgpa will be displayed
- Let the script run in background whenever the result gets updated your grades will be displayed

## Using Mail for notifications
To recieve notifications via mail do the following
- add your email address and password to mail_util.py
- Go to your gmail accounts security settings and turn on mails from less secure apps
![Security Settings](/static/gs.png)
- uncomment line 44 in aims.py
- run the python script
  - for linux ```python3 aims.py```
  - for windows ```python aims.py```
