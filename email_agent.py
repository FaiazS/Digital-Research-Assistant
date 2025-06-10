import os

from typing import Dict

import sendgrid

from sendgrid import SendGridAPIClient

from sendgrid.helpers.mail import To, Email, Mail, Content

from agents import Agent, function_tool

from dotenv import load_dotenv

load_dotenv(override=True)

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:

  """Send out a given email with the given subject and html body. """

  sendgrid_client = SendGridAPIClient(api_key = os.environ.get("SENDGRID_API_KEY"))

  to_email = To("faiaza037@gmail.com")

  from_email = Email("faiazrex8@gmail.com")

  content = Content("text/html", html_body)

  mail = Mail(to_emails=to_email, from_email=from_email, subject=subject, html_content=content)

  response = sendgrid_client.send(mail)

  return {"status" : "success"}

email_agent_instructions = """

You send nice HTML formatted emails based on a detailed report as you will be provided a detailed report.

Use your available tool to send one email providing the report is converted to a clean, well structured HTML with appropriate subject line.

"""

email_agent = Agent(
    
                    name = "Email Agent",

                    instructions = email_agent_instructions,

                    tools = [send_email],

                    model = "gpt-4o"
                    
                    )