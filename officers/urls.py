from django.urls import path

from . import views

urlpatterns = [
    path('office_dashboard', views.office_dashboard, name='office_dashboard'),
    path('office_history', views.office_history, name='office_history'),
    path('view_filing', views.view_filing, name='view_filing'),
    path('<int:filing_id>', views.view_filing, name='view_filing'),
    path('view_sorted_filing', views.view_sorted_filing, name='view_sorted_filing'),
    path('view_filing/<int:filing_id>', views.view_sorted_filing, name='view_sorted_filing'),
    path('assign_case', views.assign_case, name='assign_case'),
    path('accept_response', views.accept_response, name='accept_response'),
    path('view_sorted_response', views.view_sorted_response, name='view_sorted_response'),
    path('view_response/<int:response_id>', views.view_sorted_response, name='view_sorted_response'),
    # path('<str>', views.officer_dashboard, name='officer_response_read'),
    # Temp replacement for above 2:
    path('response_approval_list', views.response_approval_list, name='response_approval_list'),
    path('response_view/<int:response_id>', views.view_response, name='view_response'),
]
