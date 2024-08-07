# beamng_arduino_input WIP/Highly experimental
This project aims to allow for arduino based game inputs. it works based on arduino some serial communication and pyautogui. The target is to translate button pushes to keystrokes for in game use. keys are remapable in the python script.
arduino code can be found in src/main.cpp and was originally written for the arduino nano (new bootloader).
python code is in main.py and requires the following:
python3.9 or newer, pyautogui, pyserial, time, thread
yes the script runs multithreaded :p, sidenode. the serial library used is pyserial, there is also a library called serial, but the project is not set up to use this library so it will not work.
I know the script has some issues, feel free to contribute and distribute.
I have no clue about any licenses but beamng is definetly not free software. This project may be used as a base for other projects. No credits required 🫑.
Connection scheme is available with the project. Created with https://www.circuit-diagram.org/ and a little bit of gimp.

I will add some pictures to the repo later on to show how i built my blinkers and handbrake.

Hardware used in this project.

-4 cherry mx brown keyboard switches (ideal switch for microcontroller use and i had them laying around)
-1 arduino nano new bootloader (to convert button presses into serial output)
-a bit of wood and spraypaint
-hot glue
-a bit of time and effort
-nails and screws
-a few rubber bands (with some to spare to replace later)
-3 meters worth of cat 5 ethernet cable (stripped down to individual pairs to connect 4 switches to the arduino)
-1 400p pin breadboard (may be replaced with soldered circuit later on, in combo with a bluno beetle)


This project actually works quite well as is. I tested it with beamng and it doesn't really cause excessive load on the cpu. Especially if you have a modern processor. I use a ryzen 5 4600g. 6cores 12 threads. with 32gb ddr4@3200MHz.
This code can possibly be used with other games.
