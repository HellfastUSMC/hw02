from datetime import datetime as dt


def year(request):
    cur_year = dt.now().year
    return {
        'year': cur_year
    }
