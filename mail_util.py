import smtplib, ssl
def send_mail(course_name,grade,cg):
    port = 465
    smtp_server = "smtp.gmail.com"
    email = ""  # Enter your email address
    password = ""# Enter your password
    message = """\
    Subject: Aims portal grades_updated

    Grade {} assigned for {}.
    Updated CG:{}""".format(course_name,grade,cg)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(email, password)
            server.sendmail(email,email, message)
        except Exception:
            print("Error in sending email")