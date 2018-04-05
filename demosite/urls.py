from django.conf.urls import url
import views

urlpatterns = [
 	url(r'^about/',views.about,name="about"),
 	url(r'^signup/',views.sign_up,name="signup"),
 	url(r'^login/',views.log_in,name="login"),
    url(r'^user_details/', views.user_details),
    url(r'^logout/', views.signout, name='logout_url'),

]
