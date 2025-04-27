from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('student_registration/', views.student_registration, name = 'student_registration'),
    path('body/', views.body),
    path('login/', views.login, name = 'login'),
    path('home/', views.home, name = 'home'),
    path('orders/', views.orders, name = 'orders'),
    path('registered/', views.registered, name = 'registered'),
    path('parentsDashboard/', views.parentsDashboard, name='parent_dashboard'),
    path('place_order/', views.place_order, name = 'place_order'),
    path('view_orders', views.view_orders, name='view_orders'),
    path('contact', views.contact),
    path('logout/', views.logout, name = 'logout'),
    path('view_my_qr', views.view_my_qr, name = 'view_my_qr'),
    path('verify_user', views.verify_user, name = 'verify_user'),
    path('forgotpass', views.forgotpass, name = 'forgotpass'),
    path('startpage', views.startpage, name = 'startpage'),
    path('scanner', views.scanner, name = 'scanner'),
    path('get_student_details', views.get_student_details, name = 'get_student_details'),
    path('changepass', views.changepass, name = 'changepass'),
    path('passwordrequest', views.passwordrequest, name = 'passwordrequest'),
    path('about', views.about, name = 'about'),
    path('profile', views.profile, name = 'profile'),
    path('schoolregistration', views.schoolregistration, name = 'schoolregistration'),
    path('view_student/<int:student_id>/', views.view_student, name='view_student'),
    path('download/permanent_qr/<int:qr_id>/', views.download_permanent_qr, name='download_permanent_qr'),
    path('download/multiple_qrs/<int:student_id>/', views.download_multiple_qrs, name='download_multiple_qrs'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('update_order_status/<int:order_id>/', views.update_order_status, name='update_order_status'),  # Update order status
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)