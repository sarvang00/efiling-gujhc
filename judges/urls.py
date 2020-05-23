from django.urls import path

from . import views

urlpatterns = [
    path('judge_dashboard', views.judge_dashboard, name='judge_dashboard'),
    path('all_cases', views.all_cases, name='all_cases'),
    path('view_case/<int:case_id>', views.view_case, name='view_case'),
    path('findcase', views.findcase, name="findcase"),
    # path('<str: Case id>', views.fresh_filing, name='fresh_filing'),
]
