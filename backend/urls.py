#file: backend/backend/urls.py
from django.contrib import admin
from django.urls import path, include
from listings.api import views as listing_api_views
from django.conf import settings
from django.conf.urls.static import static
from users.api import views as users_api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listings/', listing_api_views.ListingList.as_view()),
    path('api/listings/create/', listing_api_views.ListingCreate.as_view()),
    path('api/listings/<int:pk>/', listing_api_views.ListingDetail.as_view()),
    path('api/listings/<int:pk>/delete/', 
        listing_api_views.ListingDelete.as_view()),
    path('api/listings/<int:pk>/update/', 
        listing_api_views.ListingUpdate.as_view()),
    path('api/profiles/', users_api_views.ProfileList.as_view()),
    path('api/profiles/<int:seller>/', users_api_views.ProfileDetail.as_view()),
    path('api/profiles/<int:seller>/update/',
         users_api_views.ProfileUpdate.as_view()),      
    path('api-auth-djoser/', include('djoser.urls')),
    path('api-auth-djoser/', include('djoser.urls.authtoken')),
    path('feedback/', include('feedback.urls')),
    path('api/', include('blog.urls')),
    path('cityinsight/', include('cityinsight.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    
