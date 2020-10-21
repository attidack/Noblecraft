from django.urls import path
from production.views import (
    productiontrackerview,
    productioncreateview,
    productiondetailview,
    productionupdateview,
    productiondeleteview,
    productioncreateviewstart,
    productioncreateviewend

)
app_name ='production'
urlpatterns = [
    path('', productiontrackerview.as_view(), name='production-tracker'),
    path('create/', productioncreateview.as_view(), name='production-create'),
    path('<int:id>/', productiondetailview.as_view(), name='production-detail'),
    path('<int:id>/update/', productionupdateview.as_view(), name='article-update'),
    path('<int:id>/delete/', productiondeleteview.as_view(), name='production-delete'),
    path('start/', productioncreateviewstart.as_view(), name='production-start'),
    path('end/', productioncreateviewend.as_view(), name='production-end'),


]
