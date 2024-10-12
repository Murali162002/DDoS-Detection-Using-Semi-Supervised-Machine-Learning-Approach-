import re

from django.db.models import Q, Count
from django.shortcuts import render, redirect


# Create your views here.
from data_admins.models import ddos_dataset


def index(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('username')
            pswd = request.POST.get('password')
            if usid == 'murali' and pswd == '4542':
                return redirect('userpage')
            elif usid == 'kishore' and pswd =='4547':
                return redirect('userpage')
            else:
                return

    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def userpage(request):
    obj = ddos_dataset.objects.all()
    return render(request,'userpage.html',{'object':obj})

def add_data(request):
    attack1 = []
    attack2, attack3, attack4, attack5, attack6, attack7, attack8, attack9 = [], [], [], [], [], [], [], []
    ans = ''
    txt = ''
    splt = ''
    if request.method == "POST":
        txt = request.POST.get("name")

        splt = (re.findall(r"[\w']+", str(txt)))

    for f in splt:
        if f in ('IPid','FDDI','x25','rangingdistance'):
            attack1.append(f)
        elif f in ('tcpchecksum','mtcp','controlflags','tcpoffset','tcpport'):
            attack2.append(f)
        elif f in ('ICMPID','udptraffic','udpunicorn','datagramid','NTP','RIP','TFTP'):
            attack3.append(f)
        elif f in ('GETID','POSTID','openBSD','appid','sessionid','transid','physicalid'):
            attack4.append(f)
        elif f in ('SYN','ACK','synpacket','sycookies'):
            attack5.append(f)
        elif f in ('serverattack','serverid','blockbankwidth'):
            attack6.append(f)
        elif f in ('monlist','getmonlist','NTPserver'):
            attack7.append(f)
        elif f in ('portid','FTPID','tryion','fragflag'):
            attack8.append(f)
        elif f in ('malwareid','gethttpid','httpid'):
            attack9.append(f)

    if len(attack1) > len(attack2) and len(attack1) > len(attack3) and len(attack1) > len(attack4) and len(
            attack1) > len(attack5) and len(attack1) > len(attack6) and len(attack1) > len(attack7) and len(
            attack1) > len(attack8) and len(attack1) > len(attack9):
        ans = "Ip Fragment Attack"
    elif len(attack2) > len(attack1) and len(attack2) > len(attack3) and len(attack2) > len(attack4) and len(
            attack2) > len(attack5) and len(attack2) > len(attack6) and len(attack2) > len(attack7) and len(
            attack2) > len(attack8) and len(attack2) > len(attack9):
        ans = "TCP Based Attack"
    elif len(attack3) > len(attack2) and len(attack3) > len(attack1) and len(attack3) > len(attack4) and len(
            attack1) > len(attack5) and len(attack1) > len(attack6) and len(attack1) > len(attack7) and len(
            attack1) > len(attack8) and len(attack1) > len(attack9):
        ans = "UDP Based Attack"
    elif len(attack4) > len(attack2) and len(attack4) > len(attack3) and len(attack4) > len(attack1) and len(
            attack4) > len(attack5) and len(attack4) > len(attack6) and len(attack4) > len(attack7) and len(
            attack4) > len(attack8) and len(attack4) > len(attack9):
        ans = "Layer Based Attack"
    elif len(attack5) > len(attack2) and len(attack5) > len(attack3) and len(attack5) > len(attack4) and len(
            attack5) > len(attack1) and len(attack5) > len(attack6) and len(attack5) > len(attack7) and len(
            attack5) > len(attack8) and len(attack5) > len(attack9):
        ans = "SYN Floods Attack"
    elif len(attack6) > len(attack2) and len(attack6) > len(attack3) and len(attack6) > len(attack4) and len(
            attack6) > len(attack5) and len(attack6) > len(attack1) and len(attack6) > len(attack7) and len(
            attack6) > len(attack8) and len(attack6) > len(attack9):
        ans = "Slowloris"
    elif len(attack7) > len(attack2) and len(attack7) > len(attack3) and len(attack7) > len(attack4) and len(
            attack7) > len(attack5) and len(attack7) > len(attack6) and len(attack7) > len(attack1) and len(
            attack7) > len(attack8) and len(attack7) > len(attack9):
        ans = "NTP Amplification"
    elif len(attack8) > len(attack2) and len(attack8) > len(attack3) and len(attack8) > len(attack4) and len(
            attack8) > len(attack5) and len(attack8) > len(attack6) and len(attack8) > len(attack7) and len(
            attack8) > len(attack1) and len(attack8) > len(attack9):
        ans = "Ping of Death Attack"
    elif len(attack9) > len(attack2) and len(attack9) > len(attack3) and len(attack9) > len(attack4) and len(
            attack9) > len(attack5) and len(attack9) > len(attack6) and len(attack9) > len(attack7) and len(
            attack9) > len(attack8) and len(attack9) > len(attack1):
        ans = "HTTP Flood Attack"

    else:
        ans = "Unlabed Data"
    ddos_dataset.objects.create(ddos_data=txt,attack_result=ans)
    return render(request,'add_data.html')
def labeled_data(request):
    obj = ddos_dataset.objects.filter(Q(attack_result='Ip Fragment Attack')|Q ( attack_result='TCP Based Attack') |Q(attack_result='UDP Based Attack') |Q (attack_result='NTP Amplification') |Q (attack_result='HTTP Flood Attack')|Q (attack_result='Layer Based Attack')| Q(attack_result='Slowloris') |Q (attack_result='Ping of Death Attack') |Q (attack_result='SYN Floods Attack'))
    return render(request,'labeled_data.html',{'object':obj})

def unlabeled_data(request):
    obj = ddos_dataset.objects.filter(attack_result='Unlabed Data')
    return render(request,'unlabeled_data.html',{'object':obj})

def ddos_analysis(request):
    chart = ddos_dataset.objects.values('attack_result').annotate(dcount=Count('attack_result'))
    return render(request,'ddos_analysis.html',{'objects':chart})

def chart_page(request,chart_type):
    chart = ddos_dataset.objects.values('attack_result').annotate(dcount=Count('attack_result'))
    return render(request,'chart_page.html',{'chart_type':chart_type,'objects':chart})

