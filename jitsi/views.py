from django.shortcuts import render

# Create your views here.


def JitsiMeetView(request):
    return render(request, 'home.html', context={})