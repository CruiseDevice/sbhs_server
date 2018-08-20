from django.shortcuts import render
from django.conf import settings

def user_has_profile(user):
    return hasattr(user, 'profile')

def email_verified(func):
    """
    This decorator is used to check if email is verified.
    If email is not verified then redirect user for email
    verification.
    """

    def is_email_verified(request, *args, **kwargs):
        user = request.user
        context = {}
        if not settings.IS_DEVELOPMENT:
            if user.is_authenticated() and user_has_profile(user):
                if not user.profile.is_email_verified:
                    context['success'] = False
                    context['msg'] = "Your account is not verified. \
                                        Please verify your account"
                    return render(
                        request, 'account/activation_status.html', context
                    )
        return func(request, *args, **kwargs)
    return is_email_verified