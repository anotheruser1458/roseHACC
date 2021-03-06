from django.shortcuts import render
from .forms import CreateReservationForm
from .models import Reservation
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse, redirect
from django.views.generic import UpdateView
from pages.models import Traffic

@login_required
def reservationsPage(request):
    if request.method == 'POST':
        form = CreateReservationForm(request.POST)
        user = request.user
        if form.is_valid():
            newRes = Reservation()
            newRes.hike = form.cleaned_data['hike']
            newRes.user = request.user
            newRes.time = form.cleaned_data['time']
            newRes.date = form.cleaned_data['date']
            newRes.number_of_people = form.cleaned_data['number_of_people']
            newRes.emergency_contact_name = form.cleaned_data['emergency_contact_name']
            newRes.emergency_contact_phone_number = form.cleaned_data['emergency_contact_phone_number']
            newRes.save()
            url = "/users/profile/"+str(request.user.pk)

            #update corresponding traffic instance
            date = newRes.date
            month = date.month
            day = date.day
            year = date.year
            
            newDate = str(date.month) + str(date.day) + str(date.year)[2:]
            traffic = Traffic.objects.filter(date=newDate, hike_id=newRes.hike.hike_id)[0]
            hour = int(newRes.time.hour)
            people = int(newRes.number_of_people)
            print(hour)
            print(type(hour))
            print(type(people))

            if hour > 20:
                traffic.num_people_6 += people
            elif hour > 16:
                traffic.num_people_5 += people
            elif hour > 12:
                traffic.num_people_4 += people
            elif hour > 8:
                traffic.num_people_3 += people
            elif hour > 4:
                traffic.num_people_2 += people
            else:
                traffic.num_people_1 += people
            traffic.save()

            return redirect(url)
    else:
        form = CreateReservationForm()
    return render(request, "reservationsPage.html", {'form':form})