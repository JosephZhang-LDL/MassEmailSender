import smtplib
import getpass
import openpyxl as xl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def add_attachment(attachment_name):
    filename = attachment_name
    attachment = open(attachment_name, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    return p

# Mail Definitions
username = str(input('Your Username:'))
password = str(getpass.getpass('Your Password:'))
From = username
Subject = str(input('Subject line:'))
is_attached = True if (input("Do you want to add an attachment (y or n):") == "y") else False
if is_attached:
    attachment_name = input("Attachment name including ending:")
your_name = input("What is your name:")
text_file = open("message.txt", "r")
text_read = text_file.read()

# Parse the spreadsheet
wb = xl.load_workbook(r'email_list.xlsx')
sheet1 = wb['Sheet1']

# Array Definitions
names = []
emails = []
subjects = []
customization = []

# Fill the arrays
for cell in sheet1['A']:
    names.append(cell.value)
names = list(filter(None, names))

for cell in sheet1['B']:
    emails.append(cell.value)
emails = list(filter(None, emails))

for cell in sheet1['C']:
    subjects.append(cell.value)
subjects = list(filter(None, subjects))

for cell in sheet1['D']:
    customization.append(cell.value)
customization = list(filter(None, customization))

# Start the server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(username, password)

# Send the emails
for i in range(len(names)):
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = emails[i]
    msg['Subject'] = Subject + subjects[i]
    text = text_read.format(names[i], customization[i], your_name)
    msg.attach(MIMEText(text, 'plain'))

    # File Attachment
    if is_attached:
        msg.attach(add_attachment(attachment_name))
    message = msg.as_string()

    try:
        server.sendmail(username, emails[i], message)
        print('Mail sent to', emails[i])
    except:
        print("Unable to send email to", emails[i])

server.quit()
print('Emails sent successfully')
