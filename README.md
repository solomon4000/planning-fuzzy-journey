# Drill Robot
ROUGH SKETCHES/IDEAS


DIAGRAMS


Onshape document we will be using

VERSIONS
If we have time, we will take it to work on the code and improve the robot's ability to perform different unique functions with the drill:
Use sensors to be able to function in certain sections

FUNCTION
The drill will be attached to an arm that rotates about a point in order to make the points to drill variable. (x-rotation)
Maybe make it go X/Y if we have the time for it?
We will use grippers to pick up the impact that has been drilled out.
Small stuff goes into the device or into a chute to the surface. The large stuff gets picked off the conveyor and deposited behind itself
Robot arm grips drill
Two arms, one for the drill and the other to pick rubbish off the conveyor belt
Servo motor to press button for drill?

LEARNING/RESEARCH
What ways can make the arm mobile in X/Y directions seamlessly without adding an extra unnecessary dimension?
How will we not blow up the earth in the process?

SUCCESS
We will be successful when:
There is something we can test the drill on
The robot arm is functional enough that the drill can be pressed and does what it needs to without going overboard
We do not start a World War and the mines do not blow up and destroy the earth.

SAFETY
For this project, we should definitely remember not to get unsafe. It's not necessary to resort to sketchy induction motors found on EBay or AliBaba to power any of this stuff, and all of these materials will be found in the Sigma lab.

PROBLEM
We might have unexploded munitions beneath the school or something like that. Also our drainage systems kinda suck right now.

BILL OF MATERIALS
A few stepper motors
A way to fabricate a metal drill (PLA will probably snap if used to drill sand)
Or a 50mm spade bit?



PSEUDOCODE
Void setup(){
pinMode(9, OUTPUT)
pinMode(10, OUTPUT)
pinMode(11, OUTPUT)
pinMode(12, OUTPUT)
}
Void loop(){
digitalWrite(11, HIGH)
digitalWrite(12, HIGH)
//Spin motor forwards
Pin 9 and 10 make it so it tunnels at 45° for 3 seconds
Level out after three seconds
Drills straight for 5 minutes
Return to surface by drilling for three seconds at 45°
}

SCHEDULE
March 4 - Start planning
March 12 - Finish planning, start CAD
April 12 - Finish CAD, start code
April 19 - Finish code and start testing individually
April 15 - Assemble project
April 26 - Revise and make improvements
May 20 - Finish improvements + documentation
May 24 - Project complete
