from django.shortcuts import render, redirect

from Expenses_tracker.web.forms import CreateProfileForm, CreateExpenseForm, EditExpenseForm, DeleteExpenseForm, \
    EditProfileForm, DeleteProfileForm
from Expenses_tracker.web.models import Profile, Expense


def check_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_page(request):
    profile = check_profile()
    if not profile:
        return redirect('create profile')

    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(x.price for x in expenses)
    context = {
        'profile': profile,
        'expenses': expenses,
        'budget_left': budget_left
    }
    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateExpenseForm()

    context = {
        'form': form,
    }
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-delete.html', context)


def show_profile(request):
    profile = check_profile()
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(x.price for x in expenses)
    expenses_count = len(expenses)

    context = {
        'profile': profile,
        'expenses_count': expenses_count,
        'budget_left': budget_left,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def profile_edit(request):
    profile = check_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-edit.html', context)



def delete_profile(request):
    profile = check_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
