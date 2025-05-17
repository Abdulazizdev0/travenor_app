from django.urls import path, include

urlpatterns = [
    path('category/',include('api.category.urls')),
    path('region/',include('api.region.urls')),
    path('user/',include('api.user.urls')),
    path('travel/',include('api.travel.urls')),
    path('booking/',include('api.booking.urls')),
    path('review/',include('api.review.urls')),
    path('payment/',include('api.payment.urls')),
    path('staff/',include('api.staff.urls')),
    path('travelguide/',include('api.travelguide.urls')),
    path('saved/',include('api.saved.urls')),
    path('notification/',include('api.notification.urls')),
    path('calendar/',include('api.calendar.urls')),

    
]