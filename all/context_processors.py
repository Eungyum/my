from .models import Menu

def menu(request):
    menus = Menu.objects.first()
    return {'menus':menus}