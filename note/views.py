from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import logging
from django.http import HttpResponse

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)
# Create your views here.
def homepage(request):

    return render(request, "home.html")


def note(request):
    notes = Note.objects.all()

    return render(request, "notes.html", context={"notes": notes})


def createNote(request):
    if request.method == "POST":
        item = request.POST.get("item")
        basePrice = float(request.POST.get("basePrice"))
        discount =float(request.POST.get("discount"))
        tax = 0

        config = {
            "A": {
                "minPrice": 1000,
                "maxPrice": 7500,
                "tax": 12,
                "type": "percentage",
            },
            "B": {"minPrice": 7500, "tax": 18, "type": "percentage"},
            "C": {"minPrice": 0, "tax": 200, "type": "fixed"},
        }

        for key1,val in config.items():
            if basePrice >= val["minPrice"]:
                if val.__contains__("maxPrice"):
                    if basePrice <= val["maxPrice"]:
                        tax =tax+((val["tax"] * basePrice) / (100.0))
                else:
                    if val["type"] == "fixed":
                        tax = tax + val["tax"]
                    else:
                        tax = tax + ((val["tax"] * basePrice) / (100.0))
            logger.error(tax)
            
        discountedPrice=((100.00-discount)*basePrice)/(100.00)

    return JsonResponse(
        {
            "status": "Valid",
            "tax": tax,
            "basePrice": basePrice,
            "finalPrice": discountedPrice + tax,
        }
    )
