from django.shortcuts import render, get_object_or_404
from .models import About

# Create your views here.


def about(request):
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about_page.html",
        {"about": about}
    )
