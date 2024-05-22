from django.shortcuts import render
from django.views.generic import TemplateView

class index(TemplateView):
    template_name = 'index.html'
    
    from django.shortcuts import render
from .models import Perfil_Profesional

def perfil_view(request):
    perfiles = Perfil_Profesional.objects.all()
    contexto = {'perfiles': perfiles}
    return render(request, 'perfil.html', contexto)