from rest_framework import status
from rest_framework.exceptions import APIException


class ParticipantExists(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = 'User is already signed up for this tournament'
    default_code = 'participant_exists'


class FreeUserCannotJoinTournament(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = 'User is not allowed to join any tournament'
    default_code = 'free_user'

class TournamentCloseException(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = "Tournament can't be closed until selecting a winner for each prize!"
    default_code = 'validation_error'

class TournamentFirstException(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = "Tournament participants must be selected first!"
    default_code = 'validation_error'

class TournamentStartException(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = "Tournament has already started!"
    default_code = 'validation_error' 