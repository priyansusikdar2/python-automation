import smtplib
from email.mime.text import MIMEText
from config import EMAIL, PASSWORD, RECEIVER

def send_email(product, price):

    subject = "Amazon Price Drop Alert!"

    body = f"""
    Price dropped for product:

    {product}

    Current Price: {price}
    """

    msg = MIMEText(body)

    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = RECEIVER

    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login(EMAIL,PASSWORD)

    server.sendmail(EMAIL,RECEIVER,msg.as_string())

    server.quit()

    print("Email alert sent")