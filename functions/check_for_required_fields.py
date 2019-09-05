def check_for_required_fields(request, required_fields):
    status = StatusCode.OK
    for required in required_fields:
        if required not in request.data:
            status = StatusCode.REQUIRED_FIELD_MISSING
            msg = "Required key '" + str(required) + "' Not present."
            break

    if status == StatusCode.REQUIRED_FIELD_MISSING:
        return False, {'st': status,
                       'msg': msg,
                       'data': []}
    else:
        return True, {}
        
@permission_classes((permissions.IsAuthenticated,))
class RegisterGitHubUserAPI(viewsets.ViewSet):
    """
        Create a new user if not exist in current db.
        if its there it gets updated.
    """

    def create(self, request, format=None):        
    required_fields = ['username', 'token']
    validated, validation_response = check_for_required_fields(
        request, required_fields)
    if not validated:
        return Response(validation_response)        
