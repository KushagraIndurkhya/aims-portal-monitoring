# aims-portal-monitoring
Result monitoring tool for IIITR Students

## Cloning the repo
- clone the repo and install requirements
```git clone https://github.com/KushagraIndurkhya/aims-portal-monitoring.git ; cd aims-portal-monitoring; pip3 install -r requirements.txt```

## Obtaining cookie
Login to https://aims.iiitr.ac.in/
go to dev tools and copy the session cookie

## Running the script
- run the python script
```python aims.py```
- enter the copied cookie
- Your Current cgpa will be displayed
- Let the script run in background whenever the result gets updated your grades will be displayed

## Using Mail for notifications
To recieve notifications via mail do the following
- add your email address and password to mail_util.py
- Go to your gmail accounts security settings and turn on mails from less secure apps
- uncomment line 44 in aims.py
