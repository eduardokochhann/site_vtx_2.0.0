from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator

from .forms import BriefingForm
from .models import Briefing
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.views.generic import (
    UpdateView,
    CreateView,
    DeleteView,

)


def home(request):
    print('home')
    return render(request, 'vortex_core/index.html')


def briefing(request):
    print('login')
    form = BriefingForm()

    return render(request, 'vortex_core/briefing.html', {'form': form})


def send_application(request):
    if request.method == 'POST':
        form = BriefingForm(request.POST)
        if form.is_valid():
            apply = form.save()
            messages.success(request, f"Sua mensagem foi enviada!")
            return briefing(request)
        else:
            messages.success(request, f"Sua mensagem foi enviada!")
            return briefing(request)
    else:
        messages.error(request, f"Utilize o formulário para essa ação!")
    messages.error(request, f"Sua mensagem não foi enviada!")
    return briefing(request)


def send_mail_with_attachment(applicant):
    obj = Briefing.objects.get(id=applicant)
    codigo = ''
    if obj.cod_vaga != '':
        codigo = 'VAGA - ' + obj.cod_vaga
    subject = 'Candidatura ' + codigo
    from_email = '"Página Trabalhe Conosco" <dpo@nd.org.br>'
    to = 'apoio.ti@nd.org.br'
    text_content = 'Currículo enviado através da página Trabalhe Conosco'
    html_content = '<h4>Currículo enviado através da página Trabalhe Conosco.<h4>' \
                   '<p>Nome: ' + obj.nome + '</p>' \
                   '<p>E-mail: ' + obj.email + '</p>' \
                   '<p>Telefone: ' + obj.telefone + '</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.attach_file(obj.arquivo.path)
    msg.send()


# def login_page(request):
#     return render(request, 'work_us/login_page.html')


# Create your views here.
