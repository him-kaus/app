from django.urls import path
from .views import appointment, book, landing, load_slots, privacypolicy, cookiespolicy, termsnconditions, ShopView, AdsView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    path('', landing, name='home'),
    path('appointments', appointment, name='appointments'),
    path('book-appointment', book, name='book'),
    path('Ads', AdsView, name='ads'),
    path('AddBot', ShopView, name='shop'),
    path('privacypolicy', privacypolicy, name='privacypolicy'),
    path('cookiespolicy', cookiespolicy, name='cookiespolicy'),
    path('termsnconditions', termsnconditions, name='termsnconditions'),

    path('ajax_load_slots', load_slots, name='ajax_load_slots'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
