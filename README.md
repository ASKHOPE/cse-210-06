# PORTAL RUSH GAME BYUI-CSE-210-06

# Rules
Portal Rush is played according to the following rules. The player can jump up using Space Key and A and D or Left and Right Arrow Keys to move foward and backward. Players try to maneuver far away from the Reaper so he won't come closer and snatch our player's soul. If a player collides with the obstacles the reaper gets a chance to come closer and closer ever time. A "game over" message is displayed in the middle of the screen if reaper was success full in snaching the player's soul. This is a infinite runner as the game becomes faster and faster at certain check points and a suprise in the end awaits.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python Portal Rush
```

## Project Structure
---
The project files and folders are organized as follows:
```
root                   	                                  
  +--README.md			                    
  +--constants.py                       
  +--game
      +--actor.py                       
      +--cast.py                                                
      +--score.py                       
      +--cycle.py                       
      +--director.py          
      +--action.py                  
      +--control_actors_action.py   
      +--draw_actors_action.py      
      +--handle_collisions_action.py 
      +--move_actors-action.py       
      +--script.py                   
      +--keyboard-services.py            
      +--video-service.py           
      +--color.py            
      +--point.py 
  +--__main__.py            
```

## Required Software
* Python 3.8.0 
* Raylib Python CFFI 3.7


## Authors & Contributions
---
* Arnold Sujan Katru (kat21015@byui.edu)- Game Play / Scripts
* Sandra Asamoah Adeleye (ade21006@byui.edu)- Game Assets / Casting
* Marcus Blanc (bla21011@byui.edu)- I/O / Services
* Karrass Phiri (phi21020@byui.edu)- Game Play / Directing 