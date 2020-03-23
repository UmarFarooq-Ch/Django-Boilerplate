# Third party imports
from django.db.utils import OperationalError, IntegrityError
from django.http.response import Http404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_integrity_error_handler(exc):
    import re
    error_message = str(exc)
    match = re.search(r'DETAIL:  (.*) in table', error_message)
    if match:  # True in case of foreign key match failure
        # remove special characters from the message
        error_message = re.sub(r'_|id|\(|\)', '', match.group(1))
    else:  # else find Detail attribute and append it into error
        match = re.search(r'(.*)\nDETAIL:  (.*)', error_message)
        if match and match.group(1) and match.group(1)[:4] == "null":
            # Error message for database constraint
            error_message = match.group(1)
        elif match and match.group(2):
            error_message = match.group(2)
    return Response({'errors': [f'{error_message}']}, status=status.HTTP_400_BAD_REQUEST)


def custom_operational_error_handler():
    return Response({'errors': ['database server down']}, status=status.HTTP_503_SERVICE_UNAVAILABLE)


def custom_exception_handler(exc, context):
    # handle default exceptions before calling django exception handler
    if isinstance(exc, OperationalError):
        return custom_operational_error_handler()

    elif isinstance(exc, IntegrityError):
        return custom_integrity_error_handler(exc)

    # Now Call REST framework's default exception handler,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is None:
        return response

    response.data = {}
    errors = []

    if isinstance(exc, Http404):
        errors.append("Not found" if str(exc) == "" else f"Not found, {str(exc)}")

    elif hasattr(exc.detail, 'items'):
        for key, value in exc.detail.items():
            errors.append("{} : {}".format(key, " ".join(value)))

    elif isinstance(exc, ValidationError):
        errors.append("{}".format(" ".join(exc.detail)))

    else:
        errors.append("{}".format(exc.detail))

    response.data['errors'] = errors

    return response
