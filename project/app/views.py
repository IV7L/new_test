from django.shortcuts import redirect, render
from .models import Member, City, Country
from .forms import CreateNewMemberForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def add_new_member(request):
    if request.method == 'POST':
        form = CreateNewMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New member added.')
            return redirect('members_list')
        else:
            print(form.errors)
            messages.error(request, 'Please add valid informations.')
    else:
        form = CreateNewMemberForm()

    return render(request, 'members/add_member.html', {
        'form':form
    })

@login_required
def view_all_members(request):
    data = Member.objects.all()
    return render(request, 'members/members_list.html',{
        'data':data
    })

def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(
        request,
        'other/city_dropdown_list_options.html',
        {'cities': cities}
    )