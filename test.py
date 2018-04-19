from monopoly_backend import *


def main():
   print("start")
   n = int(input("Enter number of players: "))
   gameboard = Board(n)
   playgame = 1
   while playgame == 1:
      for player in gameboard.playerlist:
         if len(gameboard.playerlist) == 1:
            for player in gameboard.playerlist:
               print(player.name + " WINS!")
            playgame = 0
         print(player.number, "<- turn")
         if player.jailtime > 0:
            print(player.number, " is in JAIL.")
         gameboard.premove(player)
         print(player.number, "rolls the dice!")
         die1 = random.randint(1,6)
         die2 = random.randint(1,6)
         print("die 1 roll:      " + str(die1))
         print("die 2 roll:      " + str(die2))
         if die1 == die2:
            player.droll = 1
         else:
            player.droll = 0
         gameboard.playermove(player, int(die1+die2), 0)
         print(player.boardpos)
         input()
main()
