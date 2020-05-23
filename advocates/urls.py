from django.urls import path

from . import views

urlpatterns = [
    path('lawyer_dashboard', views.lawyer_dashboard, name='lawyer_dashboard'),
    path('fresh_filing', views.fresh_filing, name='fresh_filing'),
    path('respond_case', views.respond_case, name='respond_case'),
    path('file_response', views.file_response, name='file_response'),
    path('file_matter', views.file_matter, name='file_matter'),
    path('view_petetion', views.view_petetion, name='view_petetion'),
    path('view_petetion/<int:petetion_id>', views.view_petetion, name='view_petetion'),
    path('advocate_view_response', views.advocate_view_response, name='advocate_view_response'),
    path('advocate_view_response/<int:response_id>', views.advocate_view_response, name='advocate_view_response'),
]
