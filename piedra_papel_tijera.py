#"Piedra, papel, tijeras" es un juego con dos participantes. El juego consta de rondas. En cada ronda, un participante elige un símbolo entre piedra, papel o tijeras, y el otro participante hace lo mismo. Después, para determinar el ganador de la ronda, se comparan los símbolos elegidos. Las reglas del juego determinan que la piedra gana a las tijeras, las tijeras ganan al papel (lo cortan) y el papel gana a la piedra (la envuelve). Al ganador de la ronda se le concede un punto. El juego continúa durante tantas rondas como los participantes acuerden. El ganador es el participante con más puntos.

class Participant:
    def __init__(self, name):
        self.point = 0;
        self.choice = "";
        self.name = name;
    
    def isChooseRight(self, choice):
        return choice in ["scissors", "paper", "rock"];
    
    def choose(self):
        self.choice = input(f"{self.name}, select rock, paper or scissors: ");
        while not self.isChooseRight(self.choice):
            self.choice = input(f"{self.name}, select rock, paper or scissors: ");
        
        print(f"{self.name} selects {self.choice.lower()}");
        return self.choice.lower();

class GameRound:
    def __init__(self, gamer1, gamer2):
        self.gamer1 = gamer1;
        self.gamer2 = gamer2;
    
    def compareChoices(self):
        choice1 = self.gamer1.choose()
        choice2 = self.gamer2.choose() 

        if choice1 == choice2:
            return "This round is tied.";
        elif choice1 == "scissors" and choice2 == "rock":
            self.gamer2.point += 1;
            return f"{self.gamer2.name} has won this round";
        elif choice1 == "rock" and choice2 == "scissors":
            self.gamer1.point += 1;
            return f"{self.gamer1.name} has won this round";
        elif choice1 == "paper" and choice2 == "scissors":
            self.gamer2.point += 1;
            return f"{self.gamer2.name} has won this round";
        elif choice1 == "scissors" and choice2 == "paper":
            self.gamer1.point += 1;
            return f"{self.gamer1.name} has won this round";
        elif choice1 == "rock" and choice2 == "paper":
            self.gamer2.point += 1;
            return f"{self.gamer2.name} has won this round";
        elif choice1 == "paper" and choice2 == "rock":
            self.gamer1.point += 1;
            return f"{self.gamer1.name} has won this round";
        

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
