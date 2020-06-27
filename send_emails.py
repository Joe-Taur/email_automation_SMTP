# Import SMTP library. smtp = simple mail transfer protocol. It's a protocol we must follow to send emails.
import smtplib

# Import Python email utils package
import email.utils

# Import Pandas to read csv file if there are a lot of emails need to be sent to
import pandas as pd

# Import MIME text format library.
# MIME = Multipurpose Internet Mail Extensions, it's an internet standard we follow to encode email contents, like attachments, pictures, links, text, etc.
from email.mime.text import MIMEText

# Which email is this being sent from
sender_email = 'dummy.joe@example.com'

sender_name = 'Dummy Joe'

# Password so we can log in to the sender account
password = 'yourEmailAccountPassword'

# Who is this email going to be sent to
recepient_emails = pd.read_csv('emails_list.csv')['email'].tolist()

recepient_names = pd.read_csv('emails_list.csv')['name'].tolist()

# Message body in html style
email_content = open('Email_Contents.html', 'r')

# Read in html file
email_body_html_style = email_content.read()

# The function
def boardcast_eamil():
    print('\nBoardcasting email...\n')

    # Get message ready in email format, and give us html functionality
    message = MIMEText(email_body_html_style, 'html')
    message.add_header('Content-Type', 'text/html')

    for recepient_name, recepient_email in zip(recepient_names, recepient_emails):
        # Populate the message object with data.
        message['To'] = email.utils.formataddr(
            (recepient_name, recepient_email))
        message['From'] = email.utils.formataddr((sender_name, sender_email))
        message['Subject'] = 'NOT SPAM, OPEN ME!'

        # Setup the email server. Gmail host, and use a common port
        server = smtplib.SMTP('smtp.gmail.com', 587)

        # Turn on Transport Layer Security. All smtp commands after this will now be encrypted
        server.starttls()

        # Log in the sender account
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, recepient_email, message.as_string())

        # Cleanup
        server.quit()

        print('Sent to ' + recepient_name + ' ' + recepient_email)

    print('\nEmail Boardcasted!\n')


# Call our code to send email
boardcast_eamil()
