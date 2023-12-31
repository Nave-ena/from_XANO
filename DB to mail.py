import requests
import smtplib
from email.mime.text import MIMEText

# Replace the placeholder with your Xano endpoint URL
ENDPOINT_URL = 'XANO API'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'mail'
SENDER_PASSWORD = 'pwd'

try:
    response = requests.get(ENDPOINT_URL)
    data = response.json()

    # Check if the response is a list/array
    if isinstance(data, list):
        # Iterate over each record in the response
        for record in data:
            name = record.get('name')
            email = record.get('email')
            link = record.get('link')
            summary = record.get('summary')

            # Print the fetched data
            print("Name:", name)
            print("Email:", email)
            print("Link:", link)
            print("Summary:", summary)
            print()

            # Send email
            msg = MIMEText(f"Hello {name},\n\nHere is your link: {link}\n\nSummary: {summary}")
            msg['Subject'] = 'Your Link and Summary'
            msg['From'] = SENDER_EMAIL
            msg['To'] = email

            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.send_message(msg)
                print("Email sent successfully!")

    else:
        # Handle non-array response
        print("Invalid response format. Expected an array.")

except requests.exceptions.RequestException as e:
    print('Error occurred:', e)
except smtplib.SMTPException as e:
    print('Error occurred while sending email:', e)
