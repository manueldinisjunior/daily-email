import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

def send_email():
    # Email configuration
    sender_email = "your_email@gmail.com"
    receiver_email = "recipient_email@example.com"
    subject = "Daily Report"
    body = "This is your daily report email."

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server (Gmail example)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, "your_email_password")  # Use an App Password for security

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully.")

# Schedule the job to run daily at a specific time (adjust as needed)
schedule.every().day.at("08:00").do(send_email)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
