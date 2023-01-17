from django.shortcuts import render
from .models import Contact
from django.contrib import messages
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
        except:
            messages.add_message(request, messages.ERROR, '发送失败', extra_tags='danger')
        else:
            messages.add_message(request, messages.SUCCESS, '发送成功', extra_tags='success')
    site_title = "联系"
    return render(request, 'contacts/contact.html', locals())
