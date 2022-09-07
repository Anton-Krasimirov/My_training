from django.shortcuts import render, redirect

from Homework.mymusicapp.forms import CreatProfileForm, DeleteProfileForm, AddAlbumForm, EditAlbumForm, DeleteAlbumForm
from Homework.mymusicapp.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_page(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    albums = Album.objects.all()
    context = {
        'profile': profile,
        'albums': albums,
    }

    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreatProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = CreatProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    albums = Album.objects.all()
    albums_count = len(albums)

    context = {'profile': profile, 'albums_counts': albums_count, }

    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = DeleteProfileForm(instance=profile, )

    context = {'form': form, }

    return render(request, 'profile-delete.html', context)


def add_album(request):
    profile = get_profile()
    if request.method == 'POST':
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = AddAlbumForm()
    context = {'form': form, 'profile': profile}
    return render(request, 'add-album.html', context)


def album_details(request, id):
    profile = get_profile()
    album = Album.objects.get(id=id)
    context = {'album': album, 'profile': profile, }
    return render(request, 'album-details.html', context)


def edit_album(request, id):
    album = Album.objects.get(id=id)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditAlbumForm(instance=album)

    context = {'form': form, 'id': id, }

    return render(request, 'edit-album.html', context)


def delete_album(request, id):
    album = Album.objects.get(id=id)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {'form': form, 'id': id, }

    return render(request, 'delete-album.html', context)
