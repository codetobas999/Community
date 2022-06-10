import smtplib

recipient = input("recipient: ")
subject = input("ืsubject: ")
body = input("message: ")

try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    username = 'coconuties@gmail.com'
    password = 'Pizza2400'
    server.login(username, password)
    msg = 'Subject: {}\n\n{}'.format(subject, body)
    server.sendmail(username, recipient, msg)
    server.quit()
    print("Done")
except:
    print("Fail... try again")
