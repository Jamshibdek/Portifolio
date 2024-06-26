from django.shortcuts import render
from .models import About_me, MyProject, Education, Contact
from django.views import View
from django.http import HttpResponse
# from .forms import ContactForm

class Umumiy(View):
    
    def get(self, request):
        
        about_me = About_me.objects.all()
        myproject = MyProject.objects.all()
        education = Education.objects.all()
        
                
            
        context = {
                "abouts": about_me,
                "myproject": myproject,
                "edu": education, 
            }
        return render(request, "index.html", context)








from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'footer.html', {'form': form})

        
        
