from django.shortcuts import render
from .models import EntryCodes,Rating,Faculty,Subject,EntryCodes

# Create your views here.

def index(request):
    if request.method == 'POST':
        entryCode = request.POST.get('entryCode')
        print(entryCode)
        codeData = EntryCodes.objects.all()
        for data in codeData:
            if entryCode==data.code and data.isActive:
                entryData = EntryCodes.objects.get(code=entryCode)
                return render(request,'core/rating.html',{'code':entryData})
        return render(request,'core/fail.html')
    return render(request,'core/index.html')

def submitData(request):
    if request.method == 'POST':
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        code = request.POST.get('entryCode')
        codeObject = EntryCodes.objects.get(code=code)
        r1 = request.POST.get('inlineRadioOptions')
        r2 = request.POST.get('inlineRadioOptions1')
        r3 = request.POST.get('inlineRadioOptions2')
        r4 = request.POST.get('inlineRadioOptions3')
        r5 = request.POST.get('inlineRadioOptions4')
        comment = request.POST.get('comments')
        ratingObject = Rating.objects.create(ip=ip,faculty=codeObject.faculty,subject=codeObject.subject,rating1=r1,rating2=r2,rating3=r3,rating4=r4,rating5=r5,review=comment)
        ratingObject.save()
    return render(request,'core/success.html')