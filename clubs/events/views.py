from django.shortcuts import render
from datetime import datetime
from calendar import HTMLCalendar
import calendar

# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B'), *args, **kwargs):

    month = month.capitalize()
    month_numeral = list(calendar.month_name).index(month)
    month_numeral = int(month_numeral)

    cal = HTMLCalendar().formatmonth(year, month_numeral)

    now = datetime.now()
    current_year = now.year

    context = {
        "current_year": current_year,
        "year": year,
        "month": month,
        "cal": cal,
    }
    return render(request, 'events/home.html', context)
