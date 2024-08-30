




from users.authentication import validate_token


def token_validator(request):
    auth_header = request.headers.get('Authorization')
    if auth_header is None:
        return False,{'error':'Authentication Token not provided'}
    if validate_token(auth_header) is False:  
        return False,{'error':'Token error:Token is Expired or Invalid'}
    return True,{}