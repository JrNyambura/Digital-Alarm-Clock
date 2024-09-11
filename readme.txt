This is a simple Python application using tkinter that allows users to view the current time in either 12-hour or 24-hour 
format and set an alarm.

Features
12-Hour Clock: Displays the current time in 12-hour format (AM/PM).
24-Hour Clock: Displays the current time in 24-hour format.
Alarm: Allows the user to set an alarm for a specific time.

Requirements
Python 3.x
tkinter
playsound
Pillow

Usage
A window will appear with three buttons:

12-Hour Clock: Click to display the time in 12-hour format.
24-Hour Clock: Click to display the time in 24-hour format.
Alarm: Click to set an alarm.
If you choose to set an alarm:

Enter the hour and minute for the alarm.
Click the "Start" button to begin the alarm.
When the alarm time is reached, an alarm sound will play, and a message box will appear indicating that it's time.

Code Overview
tick(val): Determines which clock or alarm function to call based on the button clicked.
time_24(): Displays the current time in 24-hour format and updates every second.
time_12(): Displays the current time in 12-hour format and updates every second.
alarm(): Opens a new window to set the alarm time.
alarm_begin(event): Starts the alarm and checks every second if the current time matches the set alarm time.


Acknowledgements
Tkinter for the GUI.
playsound for playing the alarm sound.
Pillow for image handling.
