from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Fiscal


class FiscaisView(TemplateView):
    template_name = 'fiscais.html'