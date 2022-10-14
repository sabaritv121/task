from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from zf_app.forms import UserProfileUpdate
from zf_app.models import student, marks


def studentdash(request):
    return render(request,"student.html")


@login_required(login_url='login_view')
def profile(request):
    u = request.user
    profile = student.objects.filter(user=u)


    return render(request, 'student_profile.html', {'profile': profile})

@login_required(login_url='login_view')
def profile_update(request, id):
    profile = student.objects.get(id=id)

    if request.method == 'POST':
        form = UserProfileUpdate(request.POST,request.FILES or None, instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        form = UserProfileUpdate(instance=profile)

    return render(request, 'student_update_profile.html', {'form': form})


