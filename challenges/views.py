from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

'''

# Create your views here.
def january(request):
    return HttpResponse("Watch only good stuffs");   

def february(request):
    return HttpResponse("Walk atleast 20 mins a day!") '''




monthly_challenges={"january":"Walk for at least 20 minutes every day!",
                     "february":"Learn Django for at least 20 minutes every day!",
                     "march":"Bang Someone",
                     "april":"Walk for at least 20 minutes every day!",
                     "may":"Bang Someone",
                     "june":"Learn Django for at least 20 minutes every day!",
                     "july":"Walk for at least 20 minutes every day!",
                     "august":"Walk for at least 20 minutes every day!",
                     "september":"Bang Someone",
                     "october":"Learn Django for at least 20 minutes every day!",
                     "november":"Walk for at least 20 minutes every day!",
                     "december":"Bang Someone"}


def monthly_challenge(request,month):
    challenge_text=None
    try:
        challenge_text=monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not supported')
 
def monthly_challenge_by_number(request,num):
    months=list(monthly_challenges.keys())
    if(num>len(months) or  num<1):
       return HttpResponseNotFound("No Month defined for the input")
    else:
        x=months[num-1]
        return HttpResponseRedirect("/challenges/"+x)


