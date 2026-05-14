import smtplib, os, sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

folder, subject_prefix = sys.argv[1], sys.argv[2]
date = sys.argv[3]
filepath = f"{folder}/{date}.md"

if not os.path.exists(filepath):
    print(f"No file: {filepath}")
    sys.exit(0)

with open(filepath) as f:
    body = f.read()

msg = MIMEMultipart()
msg["Subject"] = f"{subject_prefix} {date}"
msg["From"] = "keds.with.ai@gmail.com"
msg["To"] = "keds.with.ai@gmail.com"
msg.attach(MIMEText(body, "plain", "utf-8"))

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
    s.login("keds.with.ai@gmail.com", os.environ["GMAIL_APP_PASSWORD"])
    s.sendmail("keds.with.ai@gmail.com", "keds.with.ai@gmail.com", msg.as_string())
print(f"Email sent: {date}")
