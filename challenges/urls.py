from django.urls import path
from . import views

urlpatterns = [
    path("<int:num>/",views.monthly_challenge_by_number),
    path("<str:month>/",views.monthly_challenge)
]

''' 
 path("january/",views.january),
    path("february/",views.february),
'''

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