from django.shortcuts import render
from .models import EntryCodes

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