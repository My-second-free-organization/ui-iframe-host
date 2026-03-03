from pydantic import BaseModel
from typing import Optional

class SendEmailRequest(BaseModel):
    to: list[str]
    subject: str
    body: str
    html: bool = False
    cc: list[str] = []
    attachments: list[str] = []

class EmailTemplate(BaseModel):
    to: list[str]
    template_name: str
    variables: dict = {}
    def to_send_request(self) -> SendEmailRequest:
        return SendEmailRequest(to=self.to, subject=f"FlowForge: {self.template_name}", body=str(self.variables))
