from django.urls import path, include
from account.views import AuthView, PasswordResetConfirmView, PasswordResetView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', AuthView.login, name="login"),
    path('logout/', AuthView.logout, name="logout"),
    # path('signup/', AuthView.signup, name="signup"),
    path('password-reset/', include([
        path('', PasswordResetView.as_view(
            template_name='account/password_reset_form.html'), name='password_reset'),
        path('done/', auth_views.PasswordResetDoneView.as_view(
            template_name='account/password_reset_done.html'), name='password_reset_done')
    ])),
    path('reset/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(
        template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='account/password_reset_complete.html'), name='password_reset_complete')
]
