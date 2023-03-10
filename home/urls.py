from django.urls import path
from . import views
from home.views import login_request, logout_view, indexAccountView, account_address_delete, DeleteEvent, \
    SchoolSlotsDetails

app_name = 'home'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # Manage users
    path('login/', login_request, name="login"),
    path('logout/', logout_view, name="logout"),
    path('sign-up/', views.SignUpView.as_view(), name='signup'),
    path('account/', indexAccountView, name='account'),

    # Manage schools
    path('schools/', views.SchoolIndexView.as_view(), name="schools"),
    path('school/create', views.CreateSchoolView.as_view(), name="school-create"),
    path('school/<str:id>/', views.SchoolDetailsView.as_view(), name="school-details"),
    path('schools/<int:pk>/delete/', account_address_delete, name='school-delete'),

    # Manage events
    path('school/<int:pk>/add-event/', views.ManageEventView.as_view(), name="add-event"),
    path('school/<int:pk>/edit/<int:pk2>', views.ManageEventView.as_view(), name="edit-event"),  # TO modify
    path('school/event/<int:pk>/delete', DeleteEvent, name="delete-event"),

    # Manage users actions
    path('check-school-slots/<int:pk>', views.SchoolSlotsDetails.as_view(), name="school-slots"),

    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
