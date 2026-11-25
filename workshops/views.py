from django.shortcuts import render, get_object_or_404

from .models import Workshop

def workshop_list(request):
    workshops = Workshop.objects.all()
    context = {
        "workshops": workshops
    }
    return render(request, "workshops/workshop_list.html", context)

def workshop_details(request, id):
    workshop = get_object_or_404(Workshop, id=id)
    context = {
        "workshop": workshop
    }
    return render(request, "workshops/workshop_details.html", context)