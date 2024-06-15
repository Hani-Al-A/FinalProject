from datetime import datetime

def current_date(request):
    now = datetime.now()
    return {
        'current_month': now.month,
        'current_year': now.year,
    }