import datetime

from .models import ActivityLog, AccessLog
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone


class ActivityLogMiddleware(object):

    def __init__(self, get_response=None):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # create session
        if not request.session.session_key:
            request.session.create()

        activity_logs = dict()

        # get the request path

        paths = ["/accounts/login/", "/accounts/logout/"]

        if request.path in paths:
            activity_logs["path"] = request.path

            # get the client's IP address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            activity_logs["ip_address"] = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
            
            activity_logs["method"] = request.method
            activity_logs["session_key"] = request.session.session_key
            activity_logs["timestamp"] = timezone.now()

            try:
                ActivityLog(**activity_logs).save()
            except Exception as e:
                pass

        response = self.get_response(request)
        return response


class AccessLogMiddleware(object):

    def __init__(self, get_response=None):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # create session
        if not request.session.session_key:
            request.session.create()

        access_logs = dict()

        if request.method=="POST":
            # get the request path
            access_logs["path"] = request.path

            # get the client's IP address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            access_logs["ip_address"] = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

            access_logs["referrer"] = request.META.get('HTTP_REFERER',None)
            access_logs["session_key"] = request.session.session_key

            data=dict()
            data['post'] = dict(request.POST.copy())

            # remove password form post data for security reasons
            keys_to_remove = ["password", "csrfmiddlewaretoken", "old_password", "new_password1", "new_password2", "password1", "password2"]
            for key in keys_to_remove:
                data["post"].pop(key, None)

            access_logs["data"] = str(data["post"])
            access_logs["timestamp"] = timezone.now()

            try:
                AccessLog(**access_logs).save()
            except Exception as e:
                pass

        response = self.get_response(request)
        return response


class Command(BaseCommand):

    help = 'Clean the user access logs older than x days'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        days_to_keep_access_data = 2
        days_to_keep_activity_data = 7
        now = timezone.now()
        AccessLogs.objects.filter(timestamp__lt=(now - datetime.timedelta(days=days_to_keep_access_data))).delete()
        ActivityLogs.objects.filter(timestamp__lt=(now - datetime.timedelta(days=days_to_keep_activity_data))).delete()