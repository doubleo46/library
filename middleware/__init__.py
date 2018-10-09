"""Middleware to preprocess the request."""

import re
import logging
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class HandleRequests(MiddlewareMixin):
    """Process the request based on the defined URL strings."""

    def process_request(self, request):
        """Regex comparison."""
        if not re.match(SAFE_TO_REDIRECT_URI_REGEX, request.path):
            print (request.path)
            if ('/admin_login/' == request.path):
                return None
            elif not request.user.is_authenticated:
                logging.error("User is not authenticated.")
                return redirect('admin_login')
            else:
                return None
        return None


"""Possible URL's without authentication(request.path)."""
SAFE_TO_REDIRECT_URI_REGEX = '(/admin_login/)|(/signup/)'


# import re
# from django.shortcuts import  redirect
# from django.utils.deprecation import MiddlewareMixin



# class HandleRequestsf(MiddlewareMixin):

#     def __init__(self, get_response):
#         self.get_response = get_response

#     def process_request(self, request):
#         print("Path",request.path)
#         if(request.path=='/maint'):
#             return None
#         else:
#             return redirect('maint')
