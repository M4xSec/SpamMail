'''from verify_email import verify_email
hack = verify_email('din_rockin@gmail.com')
print(hack)'''
#--------------------------------------------------------------------
import re
import smtplib
import dns.resolver
import time
import sys
from time import sleep
import threading

def banner():
    print("\n")
    print('''\033[31m    ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓ ▄▄▄       ██▓ ██▓    
  ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒    
  ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░    
    ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░    
  ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒
  ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░
  ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░
  ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░     ░   ▒    ▒ ░  ░ ░   
        ░                 ░  ░       ░          ░         ░  ░ ░      ░  ░
                                                                          \033[00m''')

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(3. / 100)
        threading.Thread()


# Address used for SMTP MAIL FROM command
fromAddress = 'corn@bt.com'

# Simple Regex for syntax checking
regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

def write(addressToVerify):
    print('\033[31m{+} Email: \033[00m'+addressToVerify+'\033[31m is valid! :)\033[00m')
    file1 = open('valid_mails.txt', 'a')
    file1.write(addressToVerify)
    file1.write("\n")
    file1.close()


def check(addressToVerify):
    # Syntax check
    match = re.match(regex, addressToVerify)
    if match == None:
	    print('\033[33mExiting.... ;)\033[00m')
	    exit()

    # Get domain for DNS lookup
    splitAddress = addressToVerify.split('@')
    domain = str(splitAddress[1])
    print('\033[31m{+} Domain_Server:\033[00m', domain)

    # MX record lookup
    records = dns.resolver.resolve(domain, 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)


    # SMTP lib setup (use debug level for full output)
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    # SMTP Conversation
    server.connect(mxRecord)
    server.helo(server.local_hostname) ### server.local_hostname(Get local server hostname)
    server.mail(fromAddress)
    code, message = server.rcpt(str(addressToVerify))
    server.quit()

# Assume SMTP response 250 is success
    if code == 250:
        write(addressToVerify)
    else:
	    print('\033[31m{+} Email: '+addressToVerify+' is NOT valid! :(\033[00m')

# Email address to verify
banner()
slowprint("            \033[01m\033[33m   >>>- cOdEd By: Predator0x300 -<<<\033[00m\033[00m")
slowprint("    \033[04m\033[33m         >>>--- predator0x300@gmail.com --->>>               \033[00m\033[00m")
slowprint("      \033[01m\033[33m >>>--- GitHub:\033[31m  https://github.com/Predator0x300 \033[00m\033[33m ---<<<\033[00m\033[00m")
print("\n")
file1 = open('check_mails.txt', 'r')
# Using for loop
#print("Using for loop")
count = 0
num=0
for line in file1:

    count += 1
    inputAddress = ("{}".format(line.strip()))
    print(f"\033[01m\033[33m[{num}] Checking: \033[00m\033[00m"+inputAddress)
    #inputAddress = input('Please enter the emailAddress to verify:')
    addressToVerify = str(inputAddress)
    check(addressToVerify)
    print("------------------------")
    num +=1
# Closing files 
file1.close()





















