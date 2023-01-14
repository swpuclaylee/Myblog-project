from django.shortcuts import render
from .models import Contact
from django.contrib import messages
# Create your views here.


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        topic = request.POST.get('subject')
        text = request.POST.get('message')
        try:
            Contact.objects.create(
                name=name,
                email=email,
                topic=topic,
                text=text
            )
        except:
            messages.add_message(request, messages.ERROR, '发送失败', extra_tags='error')
        else:
            messages.add_message(request, messages.SUCCESS, '发送成功', extra_tags='success')
    return render(request, 'contacts/contact.html', locals())
