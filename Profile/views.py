from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.models import User


def userprofile(request, username):
    user = User.objects.filter(username=username).first()
    if user:
        profile = get_object_or_404(Profile, user=user)
        bio = profile.bio
        user_img = profile.image
        data = {'user_obj': user, 'bio': bio, 'userImg': user_img}
        return render(request, 'userprofile/userprofile.html', data)
    else:
        return HttpResponse('No Such User')


@login_required
def saveProfile(request):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
        return redirect(reverse("userprofile:userprofile", args=[request.user.username]))
    else:
        return redirect(reverse("userprofile:userprofile", args=[request.user.username]))
