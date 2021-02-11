* Installation notes:
=====================

The required SpeechRecognition module should install without problems using the standard

pip install SpeechRecognition

command.  This module also requires PyAudio to be installed.  If the command

pip install PyAudio

fails, you may need to directly install the binaries via

pip install pipwin
pipwin install PyAudio

* Usage notes:
==============

Once you start the seamoth.py code, it will listen for commands and issue keystrokes based on those commands.  Typical commands are of the form "action x seconds" where action is one of the following:

left
right
forward
back
dive
rise

and x is a number.  For example: "dive 4 seconds" will press the "c" key for 5 seconds forcing the seamoth to dive for that amount of time.  In addition the command "end program" will exit the python script.
