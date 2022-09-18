from django.shortcuts import render, redirect

from GamePlay.web import models, forms
from GamePlay.web.forms import CreateProfileForm, CreateGame, EditGame, DeleteGame
from GamePlay.web.models import Game, Profile


def home_page(request):
    profile = models.Profile.objects.first()
    context = {'profile': profile}

    return render(request, 'home-page.html', context)




def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = CreateProfileForm()
    context = {'form': form,}

    return render(request, 'create-profile.html', context)


def dashboard(request):

    game = list(models.Game.objects.all())
    context = {'game': game,}
    return render(request, 'dashboard.html', context)




def profile_details(request):
    profile = models.Profile.objects.first()
    all_games = models.Game.objects.all()
    count_games = len(all_games)
    average_rating = sum(g.rating for g in all_games)
    context = {'profile': profile, 'count_games': count_games, 'average_rating': average_rating}
    return render(request, 'details-profile.html', context)



def edit_profile(request):
    profile = models.Profile.objects.first()
    if request.method == 'POST':
        form = forms.EditProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = forms.EditProfile(request.FILES, instance=profile)

    context = {'form': form,}
    return render(request, 'edit-profile.html', context)



# def delete_profile(request):
#     profile = models.Profile.objects.first()
#     if request.method == 'POST':
#         form = DeleteProfile(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('home-page')
#
#     else:
#         form = DeleteProfile(instance=profile)
#     context = {'form': form,}
#
#     return render(request, 'delete-profile.html', context)


def delete_profile(request):
    profile = models.Profile.objects.first()
    games = models.Game.objects.all()
    if request.method == 'POST':
        profile.delete()
        games.delete()
        return redirect('home-page')
    return render(request, 'delete-profile.html')


def create_game(request):
    if request.method == 'POST':
        form = CreateGame(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateGame()
    context = {'form': form,}

    return render(request, 'create-game.html', context)

def game_details(request, pk):
    game = models.Game.objects.get(id=pk)
    context = {'game': game,}
    return render(request, 'details-game.html', context)

def edit_game(request, pk):
    game = models.Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.EditGame(request.POST, instance=game,)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = forms.EditGame(instance=game,)

    context = {'pk': pk, 'game': game, 'form': form,}

    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    game = models.Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.DeleteGame(request.POST, instance=game,)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = forms.DeleteGame(instance=game,)
    context = {'form': form, 'game': game, 'pk': pk,}
    return render(request, 'delete-game.html', context)
