import logging
import datetime

from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

# for logging - define "error" named logging handler and logger in settings.py
error_log=logging.getLogger('error')


@receiver(user_logged_in)
def log_user_logged_in(sender, user, request, **kwargs):
    try:
        login_logout_logs = ActivityLogger.objects.filter(session_key=request.session.session_key, user=user.id)[:1]
        if not login_logout_logs:
            login_logout_log = ActivityLogger(login_time=datetime.datetime.now(),session_key=request.session.session_key, user=user, host=request.META['HTTP_HOST'])
            login_logout_log.save()
    except Exception as e:
        # log the error
        error_log.error("log_user_logged_in request: %s, error: %s" % (request, e))

@receiver(user_logged_out)
def log_user_logged_out(sender, user, request, **kwargs):
    try:
        login_logout_logs = ActivityLogger.objects.filter(session_key=request.session.session_key, user=user.id, host=request.META['HTTP_HOST'])
        login_logout_logs.filter(logout_time__isnull=True).update(logout_time=datetime.datetime.now())
        if not login_logout_logs:
            login_logout_log = ActivityLogger(logout_time=datetime.datetime.now(), session_key=request.session.session_key, user=user, host=request.META['HTTP_HOST'])
            login_logout_log.save()
    except Exception as e:
        #log the error
        error_log.error("log_user_logged_in request: %s, error: %s" % (request, e))