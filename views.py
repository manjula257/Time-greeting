from django.shortcuts import render
from datetime import datetime

def get_time_greeting():
    current_time = datetime.now().time()
    
    if current_time < datetime.strptime("12:00", "%H:%M").time():
        greeting = "Good morning."
    elif current_time < datetime.strptime("17:00", "%H:%M").time():
        greeting = "Good afternoon."
    else:
        greeting = "Good evening."
    
    return greeting

def time_wisher(request):
    user_greeting = get_time_greeting()
    return render(request, 'time_wisher.html', {'user_greeting': user_greeting})
