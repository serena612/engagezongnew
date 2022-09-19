import requests


class BaseGameClient(object):
    # domain = 'https://domain.com/api'
    domain = 'https://engage.devapp.co/api'
    players_endpoint = ''
    tournaments_endpoint = ''

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        raise NotImplemented()

    def retrieve_account(self, account):
        response = requests.get(
            url=f'{self.domain}{self.players_endpoint}{account}',
            headers=self.get_headers()
        )
        return response.json()

    def retrieve_tournament(self, tournament):
        response = requests.get(
            url=f'{self.domain}{self.players_endpoint}{tournament}',
            headers=self.get_headers()
        )
        return response.json()

    def fetch_winners(self, tournament, winners_count):
        raise NotImplemented()

    def is_winner(self, winners, player_tag):
        raise NotImplemented()
