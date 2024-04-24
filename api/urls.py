from carsharingAPI.urls import path
import api.views as v

urlpatterns = [
    path("cars/", v.CarViewset.as_view()),
    path('cars/<int:id>', v.CarViewset.as_view()),
]
