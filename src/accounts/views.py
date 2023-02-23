from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


# ici c'est si je fais moi mm
# def signup(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password1 = request.POST.get("password1")
#         password2 = request.POST.get("password2")
#         if password1 != password2:
#             return render(request, "accounts/signup.html", context={"error": "les mots de passe sont différents"})
#         CustomUser.objects.create_user(username=username, password=password1)
#         return HttpResponse(f"Bienvenu(e) {username} !")
#
#     return render(request, "accounts/signup.html")

# on est obligé de customiser car on a une classe User Custom
class CustomSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields


def signup(request):
    # initialiser un dico vide
    context = {}

    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        # si c'est valide je save et bienvenu !
        if form.is_valid():
            # créer l'user dans la BDD avec save
            form.save()
            return HttpResponse("Bienvenu !")
        # sinon je récupère les erreurs dans le context gabarit {{ errors }}
        else:
            context["errors"] = form.errors
            # donc je retourne dans "j'arrive dans la vue avec"

    # j'arrive dans la vue avec :
    form = CustomSignupForm()
    context["form"] = form

    return render(request, "accounts/signup.html", context=context)
