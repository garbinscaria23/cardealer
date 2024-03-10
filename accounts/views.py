from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

from django.contrib.auth import update_session_auth_hash


@login_required
def update_password(request):
    if request.method == 'POST':
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if new_password == confirm_password:
            # Check if the user is authenticated
            if request.user.is_authenticated:
                # Update the user's password
                request.user.set_password(new_password)
                request.user.save()

                # Update the user's session to reflect the new password
                update_session_auth_hash(request, request.user)

                messages.success(request, 'Password updated successfully.')
                return redirect('dashboard')
            else:
                messages.error(request, 'User not authenticated.')
                return redirect('login')
        else:
            messages.error(request, 'Password and Confirm Password do not match.')
            return redirect('update_password')

    return render(request, 'accounts/update_password.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in.')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


@login_required(login_url = 'login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    # count = Contact.objects.order_by('-create_date').filter(user_id=request.user.id).count()

    data = {
        'inquiries': user_inquiry,
    }
    return render(request, 'accounts/dashboard.html', data)

@login_required(login_url='login')
def delete_inquiry(request, inquiry_id):
    # Ensure that the inquiry belongs to the logged-in user
    inquiry = get_object_or_404(Contact, id=inquiry_id, user_id=request.user.id)

    if request.method == 'POST':
        inquiry.delete()
        messages.success(request, 'Inquiry deleted successfully.')
        return redirect('dashboard')

    return render(request, 'accounts/confirm_delete.html', {'inquiry': inquiry})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')

@login_required
def update_usr(request, pk):
    print(pk)

    # Use get_object_or_404 to get the user or return a 404 response if not found
    user = get_object_or_404(User, id=pk)

    if request.method == 'POST':
        user.email = request.POST.get('email', user.email)
        # empuser.Address = request.POST.get('address', user.Address)
        # empuser.pin = request.POST.get('pin', user.pin)
        user.password = request.POST.get('password', user.password)
        user.save()
        return redirect('update_usr')
    else:
        return render(request, 'accounts/update.html', {'user': user})
