from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError, EmailMessage


# Create your views here.


def playGround(request):
    try:
        message = "This mail is sent from django"
        mail = EmailMessage("Welcome mail", message, "support@libary.com", ['oluchi@gmail.com'])
        mail.attach_file('playground/static/image/img.png')
        mail.send()
    except BadHeaderError:
        pass
    return HttpResponse("welcome to he playground")


# try:
#     message = "This mail is sent from django"
#     send_mail(message=message, subject="Welcome", from_email="support@library.com",
#               recipient_list=['cashmoney@gmail.com'])
# except BadHeaderError:
#     pass
# return HttpResponse("welcome to he playground")


def helloWorld(request):
    return render(request, "programmer.html")
