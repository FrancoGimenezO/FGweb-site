from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import ContactForm
import os

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def services(request):
    return render(request, "core/services.html")

def portfolio(request):
    return render(request, "core/portfolio.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Obtener las variables de entorno
            email_user = os.getenv('EMAIL_HOST_USER')
            email_password = os.getenv('EMAIL_HOST_PASSWORD')
            
            # Crear el correo electrónico
            email_message = EmailMessage(
                subject=f'Mensaje de {name}',  # Asunto del correo
                body=message,  # Cuerpo del mensaje
                from_email=email_user,  # Tu correo electrónico
                to=['franco.it.dev@gmail.com'],  # Tu dirección de correo electrónico
                headers={'Reply-To': email}  # El correo electrónico del usuario
            )
            
            # Enviar el correo electrónico
            email_message.send(fail_silently=False)
            return redirect('contact')  # Redirige después de enviar el formulario
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def thanks(request):
    return render(request, "core/thanks.html")
