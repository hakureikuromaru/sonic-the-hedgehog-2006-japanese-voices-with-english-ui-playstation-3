# Sonic The Hedgehog 2006 Japanese Voices with English UI PlayStation 3

**This does not work with the Xbox 360 version of the game.** Mods of this nature already exist for that
version; go search GAMEBANANA.
Well, this was fun to make, even if it was time-consuming.
First off, I made two versions, with one very small difference: a change in filepath symbols to fit the
operating system. Windows uses backward slashes:
```
\
```
to call its filepath, and Unix-based systems (Linux, BSD, MacOS/OSX, etc.) use forward slashes:
```
/
```
to call their filepath. See the difference? Yeah. I do not have Windows, so I could not test on that. I
tested on Arch Linux, and the code works just as it should.

## Instructions

Install [Python](https://www.python.org).

Dump your **legally obtained** PlayStation 3 copy of the 2006 game, _Sonic the Hedgehog_, to your PC.
Go to the directory in this project named after whichever operating system that you are on: Windows or
UNIX (Linux, BSD, MacOS/OSX, etc.). In either directory is a file, `ej.py`. 

Move `ej.py` to the directory of your PlayStation 3 copy of _Sonic the Hedgehog_ (2006), and more
specifically, the following path within that directory:

UNIX:
```
/PS3_GAME/USRDIR/ps3/
```
Windows:
```
\PS3_GAME\USRDIR\ps3\
```

Open the command line in the directory in which you placed `ej.py`, then type and enter:
```
python ej.py
```
After that, this project is installed, and your PlayStation 3 copy of _Sonic the Hedgehog_ 2006 is now
available to be played with Japanese voices and English UI.

## Issues
You know those more cinematic cutscenes in the game? The cutscenes that look better than the actual
game? This project does not work on those. For whatever reason, I could not find the files for those.
If you find the solution, please let me know.

## Other Sonic 06-related Project
If you launch _Sonic the Hedgehog_ (2006) on RPCS3, there is a major graphical error, making the game
virtually impossible to see and by extension, play.
[This patch](https://gamebanana.com/tuts/17235) fixes that. The only thing that I can say in additon to
the instructions given there is to make sure to check the box that appears next to the patch after you
apply it.
