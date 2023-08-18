from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from celery_tasks.task import send_mail_task

import json
import logging
# Create your views here.

logger = logging.getLogger("contacts")


# 联系
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        try:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            flag = 0
            name = json.dumps(name)
            try:
                send_mail_task.delay(name, flag)
            except Exception as e:
                logger.error("transfer send_mail_task failed in contacts. reason: %s", e)
        except Exception as e:
            messages.add_message(request, messages.ERROR, '发送失败', extra_tags='danger')
            logger.error("contact failed. reason: %s", e)
        else:
            messages.add_message(request, messages.SUCCESS, '发送成功', extra_tags='success')
    site_title = "联系"
    return render(request, 'contacts/contact.html', locals())
