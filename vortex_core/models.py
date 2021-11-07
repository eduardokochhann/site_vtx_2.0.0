from django.db import models
from django.utils import timezone


class Briefing(models.Model):
    nome = models.CharField("Nome", max_length=100, blank=False, null=False)
    telefone = models.CharField("Telefone", max_length=20, blank=False, null=False)
    email = models.CharField("E-mail", max_length=200, blank=False, null=False)
    company = models.CharField("Empresa", max_length=100, blank=False, null=False)
    prgum = models.TextField("1. Qual é o nicho de atuação da sua empresa?", max_length=200, blank=True, null=True)
    prgdois = models.TextField("2. A quanto tempo sua empresa está no mercado? ", max_length=80, blank=False, null=False)
    prgtres = models.TextField("3. Conte um pouco sobre a sua empresa:", max_length=200, blank=False, null=False)
    prgquatro = models.TextField("4. Quais produtos e ou serviços sua empresa oferece?", max_length=200, blank=False, null=False)
    prgcinco = models.TextField("5. Conte um pouco sobre seu público-alvo:", max_length=200, blank=False, null=False)
    prgseisa = models.BooleanField("A", blank=True, null=True)
    prgseisb = models.BooleanField("B", blank=True, null=True)
    prgseisc = models.BooleanField("C", blank=True, null=True)
    prgseisd = models.BooleanField("D", blank=True, null=True)
    prgseisout = models.CharField("Outros", max_length=100, blank=True, null=True)
    prgsete1 = models.CharField("1º Concorrênte", max_length=100, blank=True, null=True)
    prgsete2 = models.CharField("2º Concorrênte", max_length=100, blank=True, null=True)
    prgsete3 = models.CharField("3º Concorrênte", max_length=100, blank=True, null=True)
    prgoito = models.TextField("8. Qual mensagem você quer passar para o público?", max_length=300, blank=True, null=True)
    prgnove1 = models.TextField("1. Possui alguma preferência de cores? Se sim, quais?", max_length=50, blank=False, null=False)
    prgnove2 = models.TextField("2. Existe alguma cor que você não queira? Se sim, quais?", max_length=50, blank=False, null=False)
    prgdez = models.TextField("10. Possui slogan? Se sim, qual?", max_length=100, blank=True, null=True)
    prgonze = models.TextField("11. Existe alguma outra marca/empresa que te inspira?", max_length=100, blank=True, null=True)
    prgdoze1 = models.BooleanField("Moderna", blank=True, null=True)
    prgdoze2 = models.BooleanField("Séria", blank=True, null=True)
    prgdoze3 = models.BooleanField("Extrovertida", blank=True, null=True)
    prgdoze4 = models.BooleanField("Delicada", blank=True, null=True)
    prgdoze5 = models.BooleanField("Conservadora", blank=True, null=True)
    prgdoze6 = models.BooleanField("Divertida", blank=True, null=True)
    prgdoze7 = models.BooleanField("Elegante", blank=True, null=True)
    prgdoze8 = models.BooleanField("Nerd/Geek", blank=True, null=True)
    prgtreze1 = models.BooleanField("SIM", blank=True, null=True)
    prgtreze2 = models.BooleanField("NÃO", blank=True, null=True)
    prgquatorze1 = models.BooleanField("Cartão de visita", blank=True, null=True)
    prgquatorze2 = models.BooleanField("Papel Timbrado", blank=True, null=True)
    prgquatorze3 = models.BooleanField("Assinatura de e-mail", blank=True, null=True)
    prgquatorze4 = models.BooleanField("Envelope saco (A4)", blank=True, null=True)
    prgquatorze5 = models.BooleanField("Envelope Carta", blank=True, null=True)
    prgquatorze6 = models.BooleanField("Pasta", blank=True, null=True)
    prgquatorze7 = models.BooleanField("Crachá", blank=True, null=True)
    prgquatorze8 = models.TextField("outros", max_length=100, blank=True, null=True)
    prgfinal = models.TextField("Você tem algo a mais para relatar?", max_length=300, blank=True, null=True)

    def __str__(self):
        return self.nome + ' - ' + self.company

    def soft_delete(self):
        self.ativo = False
        self.data_desativado = timezone.now()
        self.save()