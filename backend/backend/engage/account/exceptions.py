from rest_framework import status
from rest_framework.exceptions import APIException


class GameAccountUnavailable(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = 'Game account is missing'
    default_code = 'game_account_unavailable'

class CoinLimitReached(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = 'Coin Limit Reached'
    default_code = 'coin_limit_reached'
    
class MinimumProfileLevelException(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = 'Your profile level is bellow the minimum profile level for this tournament'
    default_code = 'minimum_profile_level'




