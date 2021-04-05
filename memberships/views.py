from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import StripeCustomer
from profiles.models import UserProfile
from django.contrib import messages

import stripe

# Create your views here.


@login_required
def memberships(request):
    """ A view to display the memberships page """
    try:
        # Retrieve the subscription & product
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        product = stripe.Product.retrieve(subscription.plan.product)

        return render(request, 'memberships/memberships.html', {
            'subscription': subscription,
            'product': product,
            'on_membership_page': True,
        })

    except StripeCustomer.DoesNotExist:
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


@login_required
def success(request):
    return render(request, 'memberships/memberships-success.html')


@login_required
def cancel(request):
    return render(request, 'memberships/memberships-cancel.html')


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_MEMBERSHIP_WH_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')

        # Get the user and create a new StripeCustomer
        user = User.objects.get(id=client_reference_id)
        StripeCustomer.objects.create(
            user=user,
            stripeCustomerId=stripe_customer_id,
            stripeSubscriptionId=stripe_subscription_id,
        )

        profile = get_object_or_404(UserProfile, user=user)
        profile.membership_type = 'Pro'
        profile.save()

    return HttpResponse(status=200)


@login_required
def downgrade(request):
    member = get_object_or_404(UserProfile, user=request.user)
    membership_type = member.membership_type

    if membership_type == 'Pro':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        product = stripe.Product.retrieve(subscription.plan.product)

        stripe.Subscription.modify(
            subscription.id,
            cancel_at_period_end=False,
            proration_behavior='create_prorations',
            items=[{
                'id': subscription['items']['data'][0].id,
                'price': settings.STRIPE_BEGINNER_PRICE_ID,
            }]
        )

        profile = get_object_or_404(UserProfile, user=request.user)
        profile.membership_type = 'Beginner'
        profile.save()

        context = {
            'subscription': subscription,
            'product': product,
            'on_membership_page': True,
        }
        messages.success(request, 'Membership successfully downgraded')
        return render(request, 'home/index.html', context)
    else:
        context = {
            'on_membership_page': True,
        }
        messages.success(request, 'You are already a Beginner member')
        return render(request, 'home/index.html', context)


@login_required
def upgrade(request):
    member = get_object_or_404(UserProfile, user=request.user)
    membership_type = member.membership_type

    if membership_type == 'Beginner':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        product = stripe.Product.retrieve(subscription.plan.product)

        stripe.Subscription.modify(
            subscription.id,
            cancel_at_period_end=False,
            proration_behavior='create_prorations',
            items=[{
                'id': subscription['items']['data'][0].id,
                'price': settings.STRIPE_PRO_PRICE_ID,
            }]
        )

        profile = get_object_or_404(UserProfile, user=request.user)
        profile.membership_type = 'Pro'
        profile.save()

        context = {
            'subscription': subscription,
            'product': product,
            'on_membership_page': True,
        }
        messages.success(request, 'Membership successfully upgraded')
        return render(request, 'home/index.html', context)
    elif membership_type == 'Pro':
        context = {
            'subscription': subscription,
            'product': product,
            'on_membership_page': True,
        }
        messages.success(request, 'You are already a Pro member')
        return render(request, 'home/index.html', context)
    else:
        context = {
            'on_membership_page': True,
        }
        messages.success(request, 'Please use the stripe portal to purchase a membership')
        return render(request, 'memberships/memberships.html', context)
