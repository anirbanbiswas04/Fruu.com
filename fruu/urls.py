from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from core.views import home, sign_up, profile
from market.views import list_detail, sell, update_sell, delete_sell, category_detail, search


urlpatterns = [
    path('', include('pwa.urls')),
    path('', home, name='home'),
    path('sell/', sell, name='sell'),
    path('sell-update/<slug:slug>/', update_sell, name='update_sell'),
    path('delete-sell/<slug:slug>/', delete_sell, name='delete_sell'),
    path('list-detail/<slug:slug>/', list_detail, name='list_detail'),
    path('category-detail/<slug:slug>/', category_detail, name='category_detail'),
    path('search/', search, name='search'),
    path('profile/', profile, name='profile'),
    path('signup/', sign_up, name='sign_up'),
    path('login/', LoginView.as_view(template_name='login.html'), name='log_in'),
    path('logout/', LogoutView.as_view(), name='log_out'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
