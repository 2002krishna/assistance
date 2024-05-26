from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from transformers import pipeline


@login_required
def home(request):
 return render(request, "home.html", {})

@login_required
def learningtasks(request):
    return render(request, "registration/learning_tasks.html", {})

@login_required
def mockinterview(request):
    return render(request, "registration/questions.html", {})

@login_required
def company(request):
    return render(request, "registration/company.html", {})

@login_required
def tcs(request):
    return render(request, "registration/tcs.html", {})

@login_required
def jpmorgan(request):
    return render(request, "registration/jpmorgan.html", {})

@login_required
def salesforce(request):
    return render(request, "registration/salesforce.html", {})

@login_required
def cognizant(request):
    return render(request, "registration/cognizant.html", {})

@login_required
def wipro(request):
    return render(request, "registration/wipro.html", {})

@login_required
def infosys(request):
    return render(request, "registration/infosys.html", {})

@login_required
def spark(request):
    return render(request, "registration/spark.html", {})

@login_required
def java(request):
    return render(request, "registration/java.html", {})


def generate_questions(request):
    role = request.GET.get('role')
    if role:
        questions = get_questions_for_role(role)
        return JsonResponse({'questions': questions})
    return JsonResponse({'error': 'Invalid role'})

def get_questions_for_role(role):
    question_generator = pipeline('text-generation', model='bert-base-uncased')
    prompts = {
        'data_scientist': 'Interview questions for a data scientist:',
        'software_engineer': 'Interview questions for a software engineer:',
        'product_manager': 'Interview questions for a product manager:',
    }
    prompt = prompts.get(role, 'Interview questions:')
    questions = question_generator(prompt, max_length=50, num_return_sequences=5)
    return [q['generated_text'] for q in questions]


def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("base:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})
