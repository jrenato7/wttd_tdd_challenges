from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        body = """
        Obrigado por se inscrever no eventex
        os dados que vc informou são:
        Nome: Renato B
        CPF: 12345678901
        Email: jose.renato77@gmail.com
        Telefone: 86995925144
        Sua inscrião foi realizada com sucesso.
        """
        mail.send_mail(
            'Inscrição no Eventex',
            body,
            'contato@eventex.com.br',
            ['contato@eventex.com.br', 'jose.renato77@gmail.com'])
        return HttpResponseRedirect('/inscricao/', form)
    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)