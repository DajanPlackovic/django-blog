from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateRequestForm

# Create your views here.


def about(request):
    if request.method == "POST":
        collaborate_form = CollaborateRequestForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateRequestForm()

    return render(
        request,
        "about/about_page.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        }
    )
