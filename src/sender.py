import aiosmtplib
import os
from email.message import EmailMessage
from .models import SendEmailRequest

async def send_email(request: SendEmailRequest):
    msg = EmailMessage()
    msg["From"] = os.getenv("SMTP_FROM", "noreply@flowforge.io")
    msg["To"] = ", ".join(request.to)
    msg["Subject"] = request.subject
    if request.html: msg.set_content(request.body, subtype="html")
    else: msg.set_content(request.body)
    await aiosmtplib.send(msg, hostname=os.getenv("SMTP_HOST", "localhost"), port=int(os.getenv("SMTP_PORT", "587")))
