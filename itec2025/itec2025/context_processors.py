from datetime import date


def get_current_year(request):
    """
    Procesador de contexto para agregar el año actual al contexto.
    """
    return {
        'current_year': date.today().year
    }

def get_current_month(request):
    return {
        'current_month': date.today().month
    }

def get_current_day(request):
    return {
        'current_day': date.today().day
    }

def get_user_info(request):
    if request.user.is_authenticated:
        return {
            'user': request.user.username or None,
            'email': request.user.email or None,
        }
    return {} 