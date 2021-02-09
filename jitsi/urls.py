from django.urls import path
from .views import  JitsiMeetView

app_name = "jitsi"

urlpatterns = [
    path('', JitsiMeetView, name='jitsimeet')

]