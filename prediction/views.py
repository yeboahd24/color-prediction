# Create your views here.
from django.shortcuts import render
from .forms import ColorPredictionForm
from .models import Color


def predict_color(request):
    if request.method == "POST":
        form = ColorPredictionForm(request.POST)
        if form.is_valid():
            # Use the model to predict the color based on the RGB values
            red = form.cleaned_data["red"]
            green = form.cleaned_data["green"]
            blue = form.cleaned_data["blue"]
            predicted_color = Color.objects.filter(
                red=red, green=green, blue=blue
            ).first()
            if predicted_color:
                return render(
                    request, "prediction/result.html", {"color": predicted_color}
                )
            else:
                return render(request, "prediction/not_found.html", {"form": form})
    else:
        form = ColorPredictionForm()
    return render(request, "prediction/predict.html", {"form": form})
