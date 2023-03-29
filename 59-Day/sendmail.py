#!/usr/bin/env python3
""" Sends mail to website email """
import smtplib
import os

# CONSTANTS
mail_cnf = {
    "pwd":os.getenv("PWD"),
    "sender":os.getenv("SENDER"),
    "reciever":os.getenv("RECIEVER"),
    "mail_server": "smtp.gmail.com",
    "port":587
}

class SendMail:
    def __init__(self, *, msg=None):
        with smtplib.SMTP(mail_cnf["mail_server"], mail_cnf["port"]) as mail_server:
            mail_server.starttls()
            mail_server.login(mail_cnf["sender"], mail_cnf["pwd"])
            mail_server.sendmail(mail_cnf["sender"], mail_cnf["reciever"], msg)

