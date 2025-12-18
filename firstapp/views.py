from django.shortcuts import render

# Create your views here.
def myView(request):
    car_list = [{'title': 'BMW'}, {'title': 'Mazda'}]
    context = {'car_list': car_list}
    return render(request, 'myFirstApp/carlist.html', context)