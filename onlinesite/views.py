from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.contrib import messages
from .forms import *
# Create your views here.


def templatess(request):
    f_media=footerMedia.objects.all()
    # if request.method=='POST':
    #     name=request.POST['feedbackName']
    #     email=request.POST['feddbackEmail']
    #     message=request.POST['feedbackMessage']
    #     forms=feedbackForm(f_name=name,f_email=email,f_message=message)
    #     forms.save()
    return {'f_media':f_media}

def demos(request):
    if request.method=='POST':
        d_name=request.POST['d_name']
        d_email=request.POST['d_email']
        d_number=request.POST['d_number']
        d_subject=request.POST['d_subject']
        demoform=demo(demo_name=d_name,demo_email=d_email,demo_pnumber=d_number,demo_subject=d_subject)
        demoform.save()
        messages.success(request,'We will reach you soon')
        print('success')
        return redirect('demos')
    return render(request,'demos.html')

def index(request):
    logos=logo.objects.all()[:1]
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
    f_media=footerMedia.objects.all()
        
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
                print('The Captcha is Correct')
                name=request.POST['feedbackName']
                email=request.POST['feedbackEmail']
                message=request.POST['feedbackMessage']
                forms=feedbackForm(f_name=name,f_email=email,f_messages=message)
                forms.save()
               
                messages.success(request,'We will reach you soon')
                return redirect('/')
            # Do something else with the form data
        else:
            messages.warning(request,'The Captcha is not correct')
            print("The Captcha is Invalid")
            
           
    form = MyForm()
    context = {
        'logos':logos,
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
        "form":form,
        'f_media':f_media

    }
    return render(request, 'index.html', context)


def cap(request):
    logos=logo.objects.all()[:1]
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            print('The Captcha is Correct')
        else:
            print("The Captcha is Invalid")
    form = MyForm()
    return render(request, 'forms.html', {'form': form})


def about(request):
    logos=logo.objects.all()[:1]
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
                name=request.POST['feedbackName']
                email=request.POST['feedbackEmail']
                message=request.POST['feedbackMessage']
                forms=feedbackForm(f_name=name,f_email=email,f_messages=message)
                forms.save()
               
                messages.success(request,'We will reach you soon')
                return redirect('/')
            # Do something else with the form data
        else:
            messages.warning(request,'The Captcha is not correct')
            print("The Captcha is Invalid")
                    
    form = MyForm()
    context = {
        'logos':logos,
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
    logos=logo.objects.all()[:1]
    services2 = service2.objects.all()
    group100 = groups100.objects.all()
    group101 = groups101.objects.all()
    context = {
        'logos':logos,
        's2': services2,
        'g100': group100,
        'g101': group101,
    }
    return render(request, 'services.html', context)


def contact(request):
    logos=logo.objects.all()[:1]
    group100 = groups100.objects.all()
    group101 = groups101.objects.all()
    groups7 = group7.objects.all()
    contacts1 = contact1.objects.all()[:1]
    contacts2 = contact2.objects.all()
    contacts3 = contact3.objects.all()
    contacts4 = contact4.objects.all()
    f_media=footerMedia.objects.all()
    f_medias=footerMedia.objects.all()[:5]
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
                print('The Captcha is Correct')
                name=request.POST['feedbackName']
                email=request.POST['feedbackEmail']
                message=request.POST['feedbackMessage']
                forms=feedbackForm(f_name=name,f_email=email,f_messages=message)
                forms.save()
               
                messages.success(request,'We will reach you soon')
                return redirect('/')
            # Do something else with the form data
        else:
            messages.warning(request,'The Captcha is not correct')
            print("The Captcha is Invalid")
                  
    form = MyForm()
    context = {
        'logos':logos,

        'g100': group100,
        'g101': group101,
        'g7': groups7,
        'c1': contacts1,
        'c2': contacts2,
        'c3': contacts3,
        'c4': contacts4,
        'form':form,
        'f_media':f_media,
        'f_medias':f_medias

    }
    return render(request, 'contact.html', context)


def prices(request):
    logos=logo.objects.all()[:1]
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
        'logos':logos,
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





def page_not_found(request, exception):
    return render(request, '404.html', status=404)