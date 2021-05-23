from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from mainapp.forms import ChoiceForm
from mainapp.models import Question, Choice


@login_required()
def index(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.answer += 1
            form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = ChoiceForm()
    context = {
        'title': 'главная',
        'form': form,
    }
    return render(request, 'mainapp/index.html', context)


# @login_required()
# def statistics(request):
#     choice_yes = Choice.objects.filter(title='0')
#     choice_no = Choice.objects.filter(title='1')
#     context = {
#         'title': 'статистика',
#         'choice_yes': choice_yes,
#         'choice_no': choice_no,
#     }
#     return render(request, 'mainapp/static.html', context)
