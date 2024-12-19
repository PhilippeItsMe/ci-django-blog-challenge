from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_me(request):

    """
    Save the collaborate_form into the dB
    """

    if request.method == "POST":
            collaborate_form = CollaborateForm(data=request.POST)
            if collaborate_form.is_valid():
                collaborate_form.save()
                messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")

    """
    Collect the key informations
    """
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm

    """
    Render the about page
    """

    return render(
        request,
        "about/about.html",
        {"about": about,
         "collaborate_form": collaborate_form
         },
    )