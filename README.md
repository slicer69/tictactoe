# Tic Tac Toe (TTT)
Various implementations of Tic Tac Toe in Python


This repository contains two implementations of the game Tic Tac Toe,
written in Python.

The ttt-cli.py file is a self-contained implementation of the game
which can be run from the command line in a terminal. The game
prompts the user to select a square (numbered 1-9) and then
acts as the opponent, making a counter move. The human player
is represented by "X" marks and the computer player places "O"
marks on the board. This continues until one player wins or a tie is forced.


The ttt-hat.py file is also a self-contained program. This one
ties into a Sense HAT module (for the Raspberry Pi and similar 
single board computers). The game is played the same way, but
output is displayed on the Sense HAT's 8x8 LED screen. The player
places red marks on the board and the computer player is represented
by blue.

The human player can select which square they want to occupy next
by using the Sense HAT's joystick to move the selection cursor.
Moving the stick up/down/left/right moves the selection cursor on
the LED display. Pressing down on the stick indicates the player's
move is final.

The selection cursor is yellow when hovering over an open square
and purple when over an occupied square.

When the game is finished a quick message scrolls across the LED
display to indicate which player won.

