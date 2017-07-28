    rps - The Classic Game of Rock Paper Scissors! 
    Copyright (C) 2017 - Rahul Chaudhary 

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Contact us at: 2520@tuta.io

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def checkInput(selection):
  if selection not in ["rock", "paper", "scissors"]:
    print "Player Made Invalid Selection.Exiting"
    exit()

keepPlaying = "yes"
while keepPlaying == "yes":

  player1 = raw_input("Player 1 Picks: ")
  player2 = raw_input("Player 2 Picks: ")

  checkInput(player1)
  checkInput(player2)

  print player1
  print player2
  
  if player1 == player2:
    print "It's a tie!"
 
  if player1 == "rock":
    if player2 == "paper":
       print "Player 2 wins"
  if player2  == "scissors":
      print "Player 1 wins"
 
  if  player1 == "paper":
    if player2 == "scissors":
      print "Player 2 wins"
    if player2 == "rock":
      print "Player 1 wins"
    
  if player1 == "scissors":
    if player2 == "papper":
      print "Player 1 wins"
    if player2 == "rock":
      print "Player 2 wins"
  keepPlaying =raw_input("Do you want to keep playing? (yes/no)")
  print "Game Over!"
