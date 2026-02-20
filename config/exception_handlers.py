import logging
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from rest_framework import status

# Use the same logger as the recommendations app
logger = logging.getLogger("recommendations")


def custom_exception_handler(exc, context):
    # First, let DRF try to handle known exceptions (e.g. ValidationError)
    response = drf_exception_handler(exc, context)

    # If DRF already created a response, just log it and return
    if response is not None:
        logger.warning("Handled exception: %s", exc)
        return response

    # If we reach here, it's an unexpected error (likely 500)
    # Log full stack trace for debugging
    logger.exception("Unhandled exception: %s", exc)

    # Return a clean and consistent error response
    return Response(
        {"detail": "Internal server error"},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )