from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.contrib import messages
from .forms import *
# Create your views here.


def index(request):
    groups1 = group1.objects.all()[:1]
    groups2 = group2.objects.all()
    groups3 = group3.objects.all()[:1]
    groups4 = group4.objects.all()[:1]
    groups5 = group5.objects.all()[:3]
    groups6 = group6.objects.all()[:1]
    groups7 = group7.objects.all()
    groups80 = group80.objects.all()[:1]
    groups81 = group81.objects.all()
    groups9 = group9.objects.all()
    group100 = groups100.objects.all()
    group101 = groups101.objects.all()

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
                print('The Captcha is Correct')
                
                feedbackName = request.POST['feedbackName']
                feedbackEmail = request.POST['feedbackEmail']
                feedbackMessage = request.POST['feedbackMessage']

                data = {
                    'feedbackName': feedbackName,
                    'feedbackEmail': feedbackEmail,
                    'feedbackMessage': feedbackMessage
                }
                message = '''
                        New message:{}
                        from:{}
                    '''.format(data['feedbackMessage'], data['feedbackEmail'])

                send_mail(
                    data['feedbackMessage'],
                    message,
                    '',
                    ['nischal.batash@gmail.com'],

                    fail_silently=False,
                )
                return redirect('/')
            # Do something else with the form data
        else:
            print("The Captcha is Invalid")
            
           
    form = MyForm()
    context = {
        'g1': groups1,
        'g2': groups2,
        'g3': groups3,
        'g4': groups4,
        'g5': groups5,
        'g6': groups6,
        'g7': groups7,
        'g80': groups80,
        'g81': groups81,
        'g9': groups9,
        'g100': group100,
        'g101': group101,
        "messagen": "Message Sent",
        "form":form

    }
    return render(request, 'index.html', context)


def cap(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            print('The Captcha is Correct')
        else:
            print("The Captcha is Invalid")
            

    form = MyForm()
    return render(request, 'forms.html', {'form': form})


def about(request):
    abouts1 = about1.objects.all()[:1]
    abouts2 = about2.objects.all()
    abouts3 = about3.objects.all()
    abouts4 = about4_video.objects.all()
    groups2 = group2.objects.all()
    abouts6 = about6.objects.all()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
                print('The Captcha is Correct')
                feedbackName = request.POST['feedbackName']
                feedbackEmail = request.POST['feedbackEmail']
                feedbackMessage = request.POST['feedbackMessage']

                data = {
                    'feedbackName': feedbackName,
                    'feedbackEmail': feedbackEmail,
                    'feedbackMessage': feedbackMessage
                }
                message = '''
                        New message:{}
                        from:{}
                    '''.format(data['feedbackMessage'], data['feedbackEmail'])

                send_mail(
                    data['feedbackMessage'],
                    message,
                    '',
                    ['nischal.batash@gmail.com'],

                    fail_silently=False,
                )
                return redirect('/')
            # Do something else with the form data
        else:
            print("The Captcha is Invalid")
            
    form = MyForm()
    context = {
        'a1': abouts1,
        'a2': abouts2,
        'a3': abouts3,
        'a4': abouts4,
        'g2': groups2,
        'form':form,
        'a6': abouts6,
        "messagen": "Message Sent",
    }
    return render(request, 'about.html', context)


def services(request):
    services2 = service2.objects.all()
    group100 = groups100.objects.all()
    group101 = groups101.objects.all()
    context = {
        's2': services2,
        'g100': group100,
        'g101': group101,
    }
    return render(request, 'services.html', context)


def contact(request):
    group100 = groups100.objects.all()
    group101 = groups101.objects.all()
    groups7 = group7.objects.all()
    contacts1 = contact1.objects.all()[:1]
    contacts2 = contact2.objects.all()
    contacts3 = contact3.objects.all()
    contacts4 = contact4.objects.all()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
                print('The Captcha is Correct')
               
                feedbackName = request.POST['feedbackName']
                feedbackEmail = request.POST['feedbackEmail']
                feedbackMessage = request.POST['feedbackMessage']

                data = {
                    'feedbackName': feedbackName,
                    'feedbackEmail': feedbackEmail,
                    'feedbackMessage': feedbackMessage
                }
                message = '''
                        New message:{}
                        from:{}
                    '''.format(data['feedbackMessage'], data['feedbackEmail'])

                send_mail(
                    data['feedbackMessage'],
                    message,
                    '',
                    ['nischal.batash@gmail.com'],

                    fail_silently=False,
                )
                return redirect('/')
            # Do something else with the form data
        else:
            print("The Captcha is Invalid")
            
    form = MyForm()
    context = {

        'g100': group100,
        'g101': group101,
        'g7': groups7,
        'c1': contacts1,
        'c2': contacts2,
        'c3': contacts3,
        'c4': contacts4,
        'form':form

    }
    return render(request, 'contact.html', context)


def prices(request):
    price1 = prices1.objects.all()
    price2 = prices2.objects.all()
    price3 = prices3.objects.all()
    price4 = prices4.objects.all()
    price5 = prices5.objects.all()
    price6 = prices6.objects.all()
    group100 = groups100.objects.all()
    group101 = groups101.objects.all()
    groups2 = group2.objects.all()
    context = {
        'p1': price1,
        'p2': price2,
        'p3': price3,
        'p4': price4,
        'p5': price5,
        'p6': price6,
        'g100': group100,
        'g101': group101,
        'g2': groups2,
    }
    return render(request, 'prices.html', context)
