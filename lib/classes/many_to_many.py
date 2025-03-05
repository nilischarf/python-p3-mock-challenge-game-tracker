class Game:
    all_games = [] 
    def __init__(self, title):
        if not isinstance(title, str) or len(title) == 0:
            raise Exception("Title must be a non-empty string.")
        if not hasattr(self, "_title"):
            self._title = title
            Game.all_games.append(self)
        
    @property
    def title(self):
        return self._title
        
    def results(self):
        return [result for result in Result.all if result.game is self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        scores = [result.score for result in self.results() if result.player is player]
        sum(scores) / len(scores) if scores else 0

class Player:
    all_players = [] 

    def __init__(self, username):
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise Exception("Username must be a string between 2 and 16 characters.")
        self.username = username
        Player.all_players.append(self)

    @property
    def results(self):
        return [result for result in Result.all if result.player is self]

    def games_played(self):
        return list({result.game for result in self.results})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return sum(1 for result in self.results if result.game is game)

class Result:
    all = []

    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            raise Exception("Player must be an instance of Player.")
        if not isinstance(game, Game):
            raise Exception("Game must be an instance of Game.")
        if not isinstance(score, int):
            raise TypeError("Score must be an integer.")
        if not (1 <= score <= 5000):
            raise ValueError("Score must be between 1 and 5000.")
        if not hasattr(self, "_score"):
            self._player = player
            self._game = game
            self._score = score
            Result.all.append(self)

    @property
    def score(self):
        return self._score

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game

