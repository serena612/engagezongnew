from engage.tournament.game.base import BaseGameClient


class ClashRoyaleClient(BaseGameClient):
    domain = 'https://api.clashroyale.com/v1/'
    players_endpoint = 'players/'
    tournaments_endpoint = 'tournaments/'

    def get_headers(self):
        return {
            'Authorization': f'Bearer {self.token}'
        }

    def fetch_winners(self, tournament, winners_count):
        members = sorted(tournament.get('membersList', []),
                         key=lambda x: x['rank'])[:winners_count]
        return members

    def is_winner(self, winners, player_tag):
        for winner in winners:
            tag = winner['tag']
            name = winner['name']
            rank = winner['rank']
            score = winner['score']

            if tag == player_tag or name == player_tag:
                return True

        return False
