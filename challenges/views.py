from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
                     "december":None}


def index(request):
    months=list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{"months":months})

def month_list(request):
    months=list(monthly_challenges.keys())
    return render(request,"challenges/random.html",{"months":months})

def base_show(request):
    return render(request,"base.html")



"""
    
def monthly_challenge(request,month):
    try:
       challenge_text=monthly_challenges[month]
       response_text=f"<h2>{challenge_text}</h2>"
       return HttpResponse(response_text)
    
    except:
        return HttpResponseNotFound(f"<h2>Invalid month Input</h2>") """


#capitalize()


def monthly_challenge(request,month):
    month=month.lower()
    challenge_text=monthly_challenges.get(month)
    if challenge_text:
        return render(request,"challenges/challenge.html", 
                      {"text":challenge_text,"month_name":month})
    else:
        return HttpResponseNotFound(f"<h2>Invalid month Input</h2>")
    

def monthly_challenge(request,month):
    month=month.lower()
    challenge_text=monthly_challenges.get(month)
    if challenge_text:
        return render(request,"challenges/challenge.html", 
                      {"text":challenge_text,"month_name":month})
    elif(challenge_text==None):
        return render(request,"challenges/challenge.html", 
                      {"text":"No tasks for the given month","month_name":month})

    else:
        return HttpResponseNotFound(f"<h2>Invalid month Input</h2>")
    
def monthly_challenge_by_number(request,number):
    if(number<1 or number>len(monthly_challenges)):
        return HttpResponseNotFound("No corresponding Number for the Input")
    else:
        months=list(monthly_challenges.keys())
        month=months[number-1]
        redirect_path=reverse("month_challenge",args=[month])
        return HttpResponseRedirect(redirect_path)
    



'''
def monthly_challenge(request,month):
    try:
       challenge_text=monthly_challenges[month]
       response_text=render_to_string("challenges/challenge.html")
       return HttpResponse(response_text)
    
    except:
        return HttpResponseNotFound(f"<h2>Invalid month Input</h2>")







def monthly_challenge(request,month):
    try:
       challenge_text=monthly_challenges[month]
       response_text=f"<h2>{challenge_text}</h2>"
       return HttpResponse(response_text)
    
    except:
        return HttpResponseNotFound(f"<h2>Invalid month Input</h2>")






def monthly_challenge(request,month):
    try:
       challenge_text=monthly_challenges[month]
       response_text=render_to_string("challenges/challenge.html")
       return HttpResponse(response_text)
    
    except:
        return HttpResponseNotFound(f"<h2>Invalid month Input</h2>")



`       def index(request):
    months = [
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"]
    return render(request, "challenges/index.html", {"months": months})


    def monthly_challenge(request,month):
    month=month.lower()
    challenge_text=monthly_challenges.get(month)
    if challenge_text:
        return render(request,"challenges/challenge.html", 
                      {"text":challenge_text,"month_name":month})
    else:
        return HttpResponseNotFound(f"<h2>Invalid month Input</h2>")







    
    ''' 

