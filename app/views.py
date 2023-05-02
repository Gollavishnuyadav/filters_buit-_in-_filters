from django.shortcuts import render

# Create your views here.
def filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'my Name ISS Vishnu YAdav',"dt":dt,'c':0}
    return render(request,'filters.html',d)