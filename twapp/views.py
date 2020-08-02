from django.shortcuts import render, get_object_or_404, redirect
from .models import Friends,Pages
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User

class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Friends
    context_object_name = 'fd'

    def get_queryset(self):
        fd = super().get_queryset()
        return fd.filter(manager=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['pg'] = Pages.objects.filter(manager=self.request.user)

        # And so on for more models
        return context

class FPDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Friends
    context_object_name = 'fdd'
    def get_context_data(self, **kwargs):
        context = super(FPDetailView, self).get_context_data(**kwargs)
        context['pgg'] = Pages.objects.filter(manager=self.request.user)
        return context

@login_required
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Friends.objects.filter(
            Q(name__icontains=search_term)
        )
        search_results1 = Pages.objects.filter(
            Q(names__icontains=search_term)
        )
        context = {
            'search_term': search_term,
            'fd': search_results.filter(manager=request.user),
            'pg': search_results1.filter(manager=request.user)
        }
        return render(request, 'search.html', context)
    else:
        return redirect('home')


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

# class Editviewform(UserCreationForm):
#     class Meta:
#         model=User
#         fields=(
#             'email','first_name','last_name',
#         )

def view_profile(request):
    args={'user':request.user}
    # return render(request,'profile.html',args)

    form = PasswordChangeForm(data=request.POST,user=request.user)
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user) 
        return redirect('logout')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'profile.html', {'form': form})

    return render(request,'profile.html',args)

# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST,user=request.user)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('logout')
#         else:
#             form = PasswordChangeForm(user=request.user)
#             return render(request, 'change_password.html', {'form': form})

#     else:
#         form = PasswordChangeForm(user=request.user)
#         return render(request, 'change_password.html', {'form': form})


# def edit_profile(request):
#     if(request.method=='POST'):
#         form = Editviewform(request.POST,instance=request.user)
#         if form.is_valid():
#             form.save()
#             #update_session_auth_hash(request, form.user)
#             return redirect('/profile/')
#         else :
#             form = Editviewform(instance=request.user)
#             args={'form':form}
#             return render(request,'edit.html',args)
#             # args={'user':request.user}
#             # return render(request,'profile.html',args)
#     else:
#         form = Editviewform(instance=request.user)
#         args={'form':form}
#         return render(request,'edit.html',args)



