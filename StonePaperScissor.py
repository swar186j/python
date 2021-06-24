class Participant:
    def __init__(self,name):
        self.name=name
        self.points=0
        self.choice=""
    
    def choose(self):
        self.choice= input("{name} select Rock, Paper or Scissor:".format(name=self.name))
        print("{name} selects {choice}".format(name=self.name, choice= self.choice))

    def toNumericalChoice(self):
        switcher = {"rock": 0,"paper": 1,"scissor": 2 }
        
        return switcher[self.choice]

    def increPoint(self):
        self.points+=1


class GameRound:
    def __init__(self, p1, p2):
        self.rules=[
            [0,-1,1],
            [1,0,-1],
            [-1,1,0]
        ]
        p1.choose()
        p2.choose()
        result= self.compareChoices(p1,p2)
        print("This Round's result: {result} ".format(result=self.getResultIntoString(result)))
        if result > 0:
            p1.increPoint()
        elif result < 0:
            p2.increPoint()
        
    
    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def getResultIntoString(self,result):
        res={ 0:"draw", 1: "win", -1:"loss"}
        return res[result]

    def awardPoints(self):
        print("implement")



class Game:
    def __init__(self):
        self.endGame= False
        self.participant= Participant("John")
        self.secondparticipant= Participant("Joe")

    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondparticipant)
            self.checkEnd()

    def checkEnd(self):
        answer = input("Continue game y/n? ")
        if answer == 'y':
            GameRound(self.participant, self.secondparticipant)
            self.checkEnd()
        else:
            print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name = self.participant.name, p1points= self.participant.points, p2name=self.secondparticipant.name, p2points=self.secondparticipant.points))
            self.declareWinner()
            self.endGame = True

    def declareWinner(self):
        resultString = "It's a Draw"
        if self.participant.points > self.secondparticipant.points:
            resultString = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.secondparticipant.points:
            resultString = "Winner is {name}".format(name=self.secondparticipant.name)
        print(resultString)


game=Game()
game.start()