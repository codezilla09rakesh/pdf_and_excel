from django.urls import path
from share import views
from share import chart
from django.views.generic import RedirectView


urlpatterns = [
    path('home/', views.Home, name="home"),
    path('pdf/', views.render_pdf_view, name="pdf"),
    path("chart/", chart.graph, name="chart"),
    path("nlp/", views.Nlp, name = "nlp"),
    path('', RedirectView.as_view(url='home/')),

]
