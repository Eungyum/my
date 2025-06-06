from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Message
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def root(request):
    return render(request, 'contact.html')

def message(request):
    if request.method == "POST":
        name = str(request.POST.get('name') or None)
        phone = str(request.POST.get('phone') or None)
        email = str(request.POST.get('email') or None)
        content = str(request.POST.get('content') or None)
        Message.objects.create(
            name=name,
            phone=phone,
            email=email,
            content=content
        )
        send_mail(
            subject=f"[My 사이트] {name}님의 메시지 도착",
            message=f"""
이름: {name}
전화번호: {phone}
이메일: {email}

[문의 내용]
{content}
                    """,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False
        )
        messages.success(request, "메시지가 성공적으로 전달되었습니다.")
        return redirect('contact_root')
            
    return redirect('contact_root')