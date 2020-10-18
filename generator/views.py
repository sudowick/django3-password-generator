from django.shortcuts import render
#from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html', {'password':'123sfdsKJHNk','team':'India'})

def password(request):

    chars_low = list("abcdefghijklmnopqrstuvwxyz")
    chars_upp = [i.upper() for i in chars_low]
    nums = list("0123456789")
    specials = list("$#@!%^&*")

    length = int(request.GET.get('length',12))
    upp = request.GET.get('upper')
    number = request.GET.get('number')
    special = request.GET.get('special')

    seq = chars_low

    if upp:
        seq.extend(chars_upp)
    if number:
        seq.extend(nums)
    if special:
        seq.extend(specials)

    password = ''

    for i in range(length):
        password += random.choice(seq)

    return render(request, 'generator/password.html', {"pass":password})

def about(request):
    return render(request,'generator/about.html')
