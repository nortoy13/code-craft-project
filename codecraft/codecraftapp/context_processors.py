from .models import Course


def courses_processor(request):
    return {'courses': Course.objects.all()}
