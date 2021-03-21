from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import stripe

# Create your views here.


@login_required
def memberships(request):
    """ A view to display the memberships page """

    return render(request, 'memberships/memberships.html')


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = settings.DOMAIN_URL
        stripe.api_key = settings.STRIPE_SECRET_KEY
        price = settings.STRIPE_PRO_PRICE_ID
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=(request.user.id if request.user.is_authenticated else None),
                success_url=(domain_url + 'success?session_id={CHECKOUT_SESSION_ID}'),
                cancel_url=domain_url + 'cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': price,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
