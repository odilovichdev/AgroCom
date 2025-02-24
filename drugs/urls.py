from django.urls import path

from drugs.views import AgroProductDetailView, AgroProductListView, FertilizerListApiView, CategoryListAPIView, \
    DrugListAPIView

urlpatterns = [
    path('', AgroProductListView.as_view()),
    path('<int:id>/', AgroProductDetailView.as_view()),
    path("fertilizers/",FertilizerListApiView.as_view()),
    path("drugs/", DrugListAPIView.as_view()),
    path("categories/", CategoryListAPIView.as_view())
]