from django.shortcuts import render

# Create your views here.
def Conditions(request):
    d={'a':600,'b':578,'c':78}
    return render(request,'Conditions.html',context=d)

def loops(request):
    di={'name':'yahoshuva'}
    return render(request,'loops.html',di)