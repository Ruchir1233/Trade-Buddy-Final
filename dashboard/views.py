from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Item

@login_required
def index(request):
    unListeditems = Item.objects.filter(created_by=request.user, keepactive=False)
    items = Item.objects.filter(created_by=request.user,keepactive=True)


    return render(request, 'dashboard/index.html', {
        'items': items,
        'unlisteditems': unListeditems
    })
