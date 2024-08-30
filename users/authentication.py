from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


def generate_tokens_for_user(user):
    """
    Generate JWT access and refresh tokens for a given user.
    Args:
        user: The user object for which to generate the tokens.
    Returns:
        dict: A dictionary containing the access and refresh tokens.
    """
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }

def validate_token(token, token_type='access'):
    """
    Validate the JWT token.
    Args:
        token (str): The JWT token to be validated.
        token_type (str): Type of the token ('access' or 'refresh').
    Returns:
        bool: True if the token is valid, False otherwise.
    """
    try:
        if token_type == 'access':
            AccessToken(token)
        elif token_type == 'refresh':
            RefreshToken(token)
        else:
            raise ValueError("Invalid token type. Must be 'access' or 'refresh'.")
        
        return True
    except (TokenError, InvalidToken, ValueError) as e:
        # Log the error if needed
        print(f"Token validation error: {e}")
        return False