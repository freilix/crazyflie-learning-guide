# Crazyflie learning guide

The Crazyflie learning guide is a starter software for crazyflie 2.0 quadcopters and the loco positioning system.

## Getting started

### Prerequisites
Before setting up the system you need to update the firmware and set the addresses of the nodes from 0-5. This can be achieved with the [LPS configuration tool](www.github.com/bitcraze/lps-tools/releases). After that you have to set the anchor positions with the [Crazyflie PC client](www.github.com/bitcraze/crazyflie-clients-python). The detailed documentation on how to set up the system is explained on the [Getting started with the Loco Positioning system](www.bitcraze.io/getting-started-with-the-loco-positioning-system) page. 

### Flying with the system
Place the copter in the middle of your flying area facing the anchor systems positive x-axis. Turn on or restart the Crazyflie 2.0.
Run the Crazyflie learning guide by starting with [Frontend/MainWindow.py](Frontend/MainWindow.py). 
Press the "Search" button in the ribbon. The possible radio settings for your Crazyflie are displayed in the drop-down list behind the button. Choose your Crazyflie from the drop-down list. Click the “Connect” button. 
From the left side you can choose the elements. You can drag and drop them to the playground. If you want to remove an element, just drop it over the bin area on the left side. Just take care that you don't send the Crazyflie to coordinates that aren't good for it!
Now that you have created your flight plan, press the "Play" button in the ribbon and see what happens. 
To stop the flight plan or as killswitch press the "Stop" button in the ribbon or "Esc" on your keyboard. 
For more information on how to set up, install or test your Crazyflie, go to [Getting started with the Crazyflie](www.bitcraze.io/getting-started-with-the-crazyflie-2-0). 

## Background
The communication to the crazyflie is based on [cflib](www.github.com/bitcraze/crazyflie-lib-python):
cflib is an API written in Python that is used to communicate with Crazyflie
and Crazyflie 2.0 quadcopters. It is intended to be used by client software to
communicate with and control a Crazyflie quadcopter.
The user interface was developt with elements of the python ui framework [PyQt5](www.riverbankcomputing.com/software/pyqt/intro). 

## Acknowledgments
This software was developt as part of the course "Autonomous mobile systems" at the University of Applied Sciences in Darmstadt Germany.
Thanks to our lecturer Stephan Gimbel. 
