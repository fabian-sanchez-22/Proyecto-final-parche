from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.urls import include, path
from . import views
from .views import (ActividadDetailAPIView, ActividadListAPIView,
                    EmpresaPersonaDetailAPIView, EmpresaPersonaListAPIView, PuntoDeportivoDetailView, get_sorted_puntos_deportivos)

urlpatterns = [
    
    path('', views.HomepageProject, name='vistaPrincipal', ),
    path('Register/User', views.registerUser, name='register'),
    path('login', views.login, name='login'),
    path('CreateEvent', views.CreateEvent, name='CreateEvent'),
    path('Register/Company', views.RegisterCompany, name='RegisterCompany'),
    path('profile', views.Profile, name='profile'),
    path('coverImage', views.CoverImage, name='CoverImagen'),
    path('Report/<int:pk>/', views.ReportEvent, name='Report'),
    path('select/user', views.SelectUser, name='selectUser'),
    path('eventCreate',views.eventForUser, name='eventUser' ),
    path('eliminar/<int:idactividad>', views.viewEventoELI, name='eliminar'),
    path('Update/<int:idactividad>', views.UpdateEvent, name='update'),
    path('updateUser/<int:idregistro>/<str:tipousuario>', views.UpdateUser, name='UpdateUser'),
    path('updateUserCompany/<int:idregistro>/<str:tipousuario>', views.UpdateUserCompany, name='UpdateUserCompany'),
    path('eventos', views.MostrarEvento, name='mostrarEventos'),
    path('eliminar/<int:idactividad>', views.viewEventoELI, name='eliminar'),
    
    path('detalles/<int:idactividad>/', views.DetallesEvento, name='detalles_evento'),
    path('profile/dislikes/<int:pk>', views.adddislike, name='dislike'),
    path('profile/likes/<int:pk>', views.addLikes, name='likes'),
    path('interfaz/<str:empresa_idempresa>/User', views.interfazUser, name='interfaz'),
    path('profile/dislikes/<int:id>/comment', views.addCommentDislike, name='dislikecomment'),
    path('profile/likes/<int:id>/comment', views.addCommentLikes, name='likescomment'),
    path('profile/delete/<int:id>/comment', views.deleteComment, name='deleteComment'),
    path('reportar_usuario/<int:pk>/', views.send_report_email, name='report'),
    
    path('detalles/<int:idactividad>/', views.DetallesEvento, name='detalles_evento'),
    path('profile/delete/<int:id>/comment/user', views.deleteCommentUser, name='deleteCommentUser'),
    path('join/event/<int:pk>', views.joinEvent, name='joinEvent'),
    path('evento/inscripcion/', views.eventoRegistration , name='inscripcion'),
    path('evento/inscripcion/anular/<int:idactividad>', views.deleteRegistration , name='inscripcionDeletes'),
    path('reportar_usuario/<int:pk>/', views.send_report_email, name='report'),
    path('Report/<int:pk>/', views.ReportEvent, name='Report'),
    path('participantes/evento/<int:pk>/', views.eventParticipante, name='participantes'),
    path('eliminar/participantes/evento/<int:idregistro>/<int:pk>', views.anularinscripcion, name='Eliminarparticipantes'),
    path('resena/Evento/<int:idEvento>',views.calificacionFinal, name='finalReseña' ),
     

    path('puntoDeportivo', views.agregarPd, name='puntoDeportivo'),
    # path('mostrarPd/', views.mostrarPd, name='mostrarPd'),
    path('punto_deportivo/<int:pk>/', PuntoDeportivoDetailView.as_view(), name='punto_deportivo_detail'),
    path('api/get_sorted_puntos_deportivos/', get_sorted_puntos_deportivos, name='get_sorted_puntos_deportivos'),
    
    path('api/actividades/', ActividadListAPIView.as_view(), name='actividad-list'),
    path('api/actividades/<int:pk>/', ActividadDetailAPIView.as_view(), name='actividad-detail'),
    path('api/usuarios/', EmpresaPersonaListAPIView.as_view(), name='usuario-list'),
    path('api/usuarios/<int:pk>/', EmpresaPersonaDetailAPIView.as_view(), name='usuario-detail'),
    
]