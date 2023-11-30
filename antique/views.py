from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from antique.forms import EvaluationRequestForm, VerificationCodeForm, RegistrationForm
from antique.models import CustomUser, Evaluation, VerificationCode
from .utils import send_SMS
# Create your views here.
@login_required
def submit_evaluation_view(request):
    return render(request, 'user/create_antique_eval.html')

def auth_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('/verify')
    return render(request, 'user/login.html', {'form':form})

def verification_view(request):
    form = VerificationCodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = CustomUser.objects.get(pk=pk)
        code = user.code
        code_user = f"{user.username}: {code}"

        if not request.POST:
            #send SMS
            print(code_user)
            send_SMS(code_user, user.phone_number)
        if form.is_valid():
                verification_code = form.cleaned_data.get('code')
                if str(code) == verification_code:
                    code.save()
                    login(request, user)
                    return redirect('/submit_evaluation')
                else:
                    return redirect('/login/')    
    return render(request, 'user/verify.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/') 
    else:
        form = RegistrationForm()

    return render(request, 'user/register.html', {'form': form})

def evaluation(request):
    print(request.user)
    return render(request , 'evaluation/request_evaluation.html')

def create_evaluation(request):
    form = EvaluationRequestForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():

            evaluation_request = form.save(commit=False)
            evaluation_request.user = request.user
            evaluation_request.save()

            return HttpResponse("form submited thanks")   
        return redirect('/listings')
            # Evaluation.objects.create(user_id = user.id , comment = form.cleaned_data.get('comment') , contact_method = form.cleaned_data.get('contact_method'))
            # return redirect("/listings")    

    else:
        form = EvaluationRequestForm()
        return render(request, "evaluation/request_evaluation.html", {"form": form})
    
def evaluation_listings(request):
    listings = Evaluation.objects.all()
    return render(request , 'evaluation/evaluation_listing.html' ,{'listings' : listings})