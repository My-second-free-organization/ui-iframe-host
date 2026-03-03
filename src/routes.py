from fastapi import APIRouter, BackgroundTasks
from .models import SendEmailRequest, EmailTemplate
from .sender import send_email

router = APIRouter()

@router.post("/send")
async def send(request: SendEmailRequest, bg: BackgroundTasks):
    bg.add_task(send_email, request)
    return {"status": "queued"}

@router.post("/send-template")
async def send_template(template: EmailTemplate, bg: BackgroundTasks):
    bg.add_task(send_email, template.to_send_request())
    return {"status": "queued"}
