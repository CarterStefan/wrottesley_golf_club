from django.urls import path
from . import views

urlpatterns = [
    path('', views.memberships, name='memberships'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('webhook/', views.stripe_webhook),
    path('downgrade/', views.downgrade, name='downgrade'),
    path('upgrade/', views.upgrade, name='upgrade'),
]
