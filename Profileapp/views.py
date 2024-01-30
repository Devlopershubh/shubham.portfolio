from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import ContactMessage
from .models import PortfolioItem
from .models import Skill
from .forms import SkillForm

def index(request):
    return render(request, 'Profileapp/index.html')

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

       
    return render(request, 'Profileapp/index.html', {'message': 'Your message has been sent. Thank you!'})

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    portfolio_items = PortfolioItem.objects.all()
    context = {
        'portfolio_items': portfolio_items
    }
    return render(request, 'portfolio.html', context) 

def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'skill_list.html', {'skills': skills})

def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm()
    return render(request, 'skill_form.html', {'form': form})

def skill_update(request, skill_id):
    skill = Skill.objects.get(id=skill_id)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'skill_form.html', {'form': form})

def skill_delete(request, skill_id):
    skill = Skill.objects.get(id=skill_id)
    if request.method == 'POST':
        skill.delete()
        return redirect('skill_list')
    return render(request, 'skill_confirm_delete.html', {'skill': skill}) 

