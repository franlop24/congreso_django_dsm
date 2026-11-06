from django.shortcuts import render

from .models import Workshop

def workshop_list(request):
    workshops = Workshop.objects.all()
    context = {
        "workshops": workshops
    }
    return render(request, "workshops/workshop_list.html", context)