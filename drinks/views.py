from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Drink, Alcohol

# Create your views here.

def all_drink(request):
    """ A view to show all kind of drinks, including sorting and search queries """
    
    drinks = Drink.objects.all()
    query = None
    sort = None
    way = None

    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, 'Error entered search term')
                return redirect(reverse('drinks'))
            queries = Q(name__icontains = query)
            drinks = drinks.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                drinks = drinks.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'descending':
                    sortkey = f'-{sortkey}'
            drinks = drinks.order_by(sortkey)

    sorting_by = f'{sort}_{way}'

    context = {
        'drinks': drinks,
        'search_term':query,
        'sorting_by':sorting_by,
    }
    return render(request, "drinks/drinks.html", context)


def each_drink(request, drink_id):
    """ A view to show each drink's details individual """

    drink = get_object_or_404(Drink, pk=drink_id)
    context = {
        'drink': drink
    }
    return render(request, "drinks/each_drink.html", context)