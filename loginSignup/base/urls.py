from django.urls import path, include
from .views import *

urlpatterns = [
 path("", home, name="home"),
 path("signup/", authView, name="authView"),
 path("learning_tasks/", learningtasks, name="learningtasks"),
 path("mock_interview/", mockinterview, name="mockinterview"),
 path("company/", company, name="company"),
 path('tcs/', tcs, name='tcs'),
 path('jpmorgan/', jpmorgan, name='jpmorgan'),
 path('salesforce/', salesforce, name='salesforce'),
 path('cognizant/', cognizant, name='cognizant'),
 path('wipro/', wipro, name='wipro'),
 path('infosys/', infosys, name='infosys'),
 path('spark/', spark, name='spark'),
 path('java/', java, name='java'),
 path("accounts/", include("django.contrib.auth.urls")),
 path('generate_questions/', generate_questions, name='generate_questions'),
]
