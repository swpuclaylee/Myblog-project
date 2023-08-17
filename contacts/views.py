from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from celery_tasks.task import send_mail_task
from django.core.mail import send_mail

import pickle
# Create your views here.


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
            try:
                flag = 0
                name = pickle.dumps(name)
                send_mail_task.delay(name, flag)
            except Exception as e:
                subject = '联系报错'
                message = f'错误原因：{e}'
                from_email = '1093591428@qq.com'
                recipients = ['swlz4751@gmail.com']
                send_mail(subject, message, from_email, recipients)
            #send_mail_task.delay(name, 0)
        except:
            messages.add_message(request, messages.ERROR, '发送失败', extra_tags='danger')
        else:
            messages.add_message(request, messages.SUCCESS, '发送成功', extra_tags='success')
    site_title = "联系"
    return render(request, 'contacts/contact.html', locals())
