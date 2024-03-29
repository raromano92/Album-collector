from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('albums/', views.albums_index, name='albums'),
  path('albums/<int:album_id>/', views.albums_detail, name='detail'),
  path('albums/create/', views.AlbumCreate.as_view(), name='albums_create'),
  path('albums/<int:pk>/update', views.AlbumUpdate.as_view(), name='albums_update'),
  path('albums/<int:pk>/delete', views.AlbumDelete.as_view(), name='albums_delete'),
  path('albums/<int:album_id>/add_track/', views.add_track, name='add_track'),
  path('band_members/', views.BandMemberList.as_view(), name='members'),
  path('band_members/<int:pk>/', views.BandMemberDetail.as_view(), name='members_detail'),
  path('band_members/create/', views.BandMemberCreate.as_view(), name='members_create'),
  path('band_members/<int:pk>/update/', views.BandMemberUpdate.as_view(), name='members_update'),
  path('band_members/<int:pk>/delete/', views.BandMemberDelete.as_view(), name='members_delete'),
  path('albums/<int:album_id>/assoc_bandmember/<int:bandmember_id>/', views.assoc_bandmember, name='assoc_bandmember')
]
