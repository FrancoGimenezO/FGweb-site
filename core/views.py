from django.shortcuts import render, HttpResponseRedirect, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Contact

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
            
            # Envía el correo electrónico
            send_mail(
                f'Mensaje de {name}',
                message,
                email,  # El correo electrónico del remitente
                ['francogz19980427@gmail.com'],  # Tu dirección de correo electrónico
                fail_silently=False,
            )
            return redirect('thanks')  # Redirige después de enviar el formulario
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def thanks(request):
    return render(request, "core/thanks.html")
