import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
# read environment variables
import os
from dotenv import load_dotenv
load_dotenv()

# email variables
email = os.getenv('SENDER_MAIL')
password = os.getenv('SENDER_PASSWORD')

def pretest_notify(target_user: str, target_mail: str) -> None:
    message = MIMEMultipart()
    message["From"] = email
    message["To"] = target_mail
    message["Subject"] = "0915 期初檢測賽 注意事項"
    
    with open("./pretest_content.txt", "r", encoding="utf-8") as file:
        text_content = file.read()
    body = text_content.format(target_user)
    message.attach(MIMEText(body, "plain"))

    path = "./files/"
    filename = "112-1期初檢測賽規則與流程.pdf"
    with open(path + filename, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name=filename, _subtype="pdf")
    # encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)

        text = message.as_string()
        server.sendmail(email, target_mail, text)
        print("成功發送給", target_user)
    except Exception as e:
        print("發送失敗", str(e))
    finally:
        server.quit()