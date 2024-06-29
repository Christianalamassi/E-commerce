from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import CheckOutForm
from basket.contexts import your_order

import stripe


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        in_basket = request.session.get('in_basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'state': request.POST['state'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            }
        check_out = CheckOutForm(form_data)
        if check_out.is_valid():
            order = check_out.save()
            for basket_id, item_data in in_basket.items():
                try:
                    drink = Drink.objects.get(id=basket_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('basket'))

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'Your basket is empty')
        return redirect(reverse('drinks'))

    your_orders = your_order(request)
    totals = your_order['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    checkout_form = CheckOutForm()
    template = 'checkout/checkout.html'
    context = {
        'checkout_form':checkout_form,
        'strip_public_key': 'stripe_public_key',
        'client_secret': 'intent.client_secret'
    }

    return render(request, template, context)



def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(ToPay, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'in_basket' in request.session:
        del request.session['in_basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)