#"Piedra, papel, tijeras" es un juego con dos participantes. El juego consta de rondas. En cada ronda, un participante elige un símbolo entre piedra, papel o tijeras, y el otro participante hace lo mismo. Después, para determinar el ganador de la ronda, se comparan los símbolos elegidos. Las reglas del juego determinan que la piedra gana a las tijeras, las tijeras ganan al papel (lo cortan) y el papel gana a la piedra (la envuelve). Al ganador de la ronda se le concede un punto. El juego continúa durante tantas rondas como los participantes acuerden. El ganador es el participante con más puntos.

class Participant:
    def __init__(self, name):
        self.point = 0;
        self.choice = "";
        self.name = name;
    
    def isChooseRight(self, choice):
        return choice in ["scissors", "paper", "rock", "spock", "lizard"];
    
    def choose(self):
        self.choice = input(f"{self.name}, select rock, paper, scissors, lizard or spock: ");

        while not self.isChooseRight(self.choice.lower()):
            self.choice = input(f"{self.name}, select rock, paper, scissors, lizard or spock: ");
        
        print(f"{self.name} selects {self.choice.lower()}");
        return self.choice.lower();

class GameRound:
    def __init__(self, gamer1, gamer2):
        self.gamer1 = gamer1;
        self.gamer2 = gamer2;
    
    def compareChoices(self):
        choice1 = self.gamer1.choose();
        choice2 = self.gamer2.choose();

        if choice1 == choice2:
            return "This round is tied.";

        winner, loser = self.determine_round_winner(choice1, choice2)

        if winner:
            winner.point += 1
            return f"{winner.name} has won this round!"
        
    def determine_round_winner(self, choice1, choice2):
        rules = {
            "rock": ["scissors", "lizard"],
            "scissors": ["paper", "lizard"],
            "paper": ["rock", "spock"],
            "lizard": ["spock", "paper"],
            "spock": ["scissors", "rock"]
        }

        if choice2 in rules.get(choice1, []):
            return self.gamer1, self.gamer2
        else:
            return self.gamer2, self.gamer1
        
class Game:
    def __init__(self, gamer1, gamer2):
        self.endGame = False;
        self.participant = Participant(gamer1);
        self.secondParticipant = Participant(gamer2);
    
    def start(self):
        while self.participant.point < 5 and self.secondParticipant.point < 5:
            game_round = GameRound(self.participant, self.secondParticipant);
            print(game_round.compareChoices());
            print(f"Scores => {self.participant.name}: {self.participant.point}, {self.secondParticipant.name}: {self.secondParticipant.point}");
        print(self.whoWins());
   
    def whoWins(self):
        if self.participant.point > self.secondParticipant.point:
            return f"{self.participant.name} is the winner!!!"
        elif self.secondParticipant.point > self.participant.point:
            return f"{self.secondParticipant.name} is the winner!!!"
        else:
            return "The game is tied!"

game = Game("Sergio", "Ana");
game.start();
