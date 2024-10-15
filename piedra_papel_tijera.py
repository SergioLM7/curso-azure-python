#"Piedra, papel, tijeras" es un juego con dos participantes. El juego consta de rondas. En cada ronda, un participante elige un símbolo entre piedra, papel o tijeras, y el otro participante hace lo mismo. Después, para determinar el ganador de la ronda, se comparan los símbolos elegidos. Las reglas del juego determinan que la piedra gana a las tijeras, las tijeras ganan al papel (lo cortan) y el papel gana a la piedra (la envuelve). Al ganador de la ronda se le concede un punto. El juego continúa durante tantas rondas como los participantes acuerden. El ganador es el participante con más puntos.

class Participant:
    def __init__(self):
        self.point = 0;
        self.election = "";

class GameRound:
    def __init__(gamerElection1, gamerElection2):
        if gamerElection1 == gamerElection2:
            return "This round is tied."
        elif gamerElection1 == "scissors" and gamerElection2 == "rock":
            gamerElection2.point += 1;
            return "Participant 2 has won this round";
        elif gamerElection1 == "rock" and gamerElection2 == "scissors":
            gamerElection1.point += 1;
            return "Participant 1 has won this round";
        elif gamerElection1 == "paper" and gamerElection2 == "scissors":
            gamerElection2.point += 1;
            return "Participant 2 has won this round";
        elif gamerElection1 == "scissors" and gamerElection2 == "paper":
            gamerElection1.point += 1;
            return "Participant 1 has won this round";
        elif gamerElection1 == "rock" and gamerElection2 == "paper":
            gamerElection2.point += 1;
            return "Participant 2 has won this round";
        elif gamerElection1 == "paper" and gamerElection2 == "rock":
            gamerElection1.point += 1;
            return "Participant 1 has won this round";

class Game:
    def __init__(self):
        self.endGame = False;
        self.participant = Participant();
        self.secondParticipant = Participant();
    def whoWins(gamerElection1, gamerElection2):
        if gamerElection1.point > 5:
            return "Participant 1 is the winner!!!";
        elif gamerElection2.point > 5:
            return "Participant 2 is the winner!!!";