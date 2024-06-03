# Drill Robot*
#### by Solomon and Raffi
*Formerly known as "Solomon's really really really really really really really really really really really really really really really really really really really really really really really really good project" and "RECORD: 1.9 GB"

[Onshape for our project](https://cvilleschools.onshape.com/documents/c2a9d48291cc143e1c5c2e36/w/15419713e5234e2432e6f2f1/e/79c7b2bf3c5ad69468cf4189)

## Planning
#### ROUGH SKETCHES/IDEAS
![Untitled](https://github.com/solomon4000/planning-fuzzy-journey/assets/90640484/7252a3d8-c401-4b5e-b52c-e14bf663f62c)
We really didn't know what we were doing when we started this project off, and this was the sketch that we initially came up with to get a feel for what we were working with. Unfortunately, there is no realistic way to get the drill to be able to safely explode chunks of soil/sand without affecting its other parts.

#### DIAGRAMS<br>
![Capture](https://github.com/solomon4000/planning-fuzzy-journey/assets/90640484/610121e8-d9fd-4019-bec9-05010f9b3550)
Here is an extremely simple sketch that we started with. You can see the foundational ideas all in one, where an arm picks up junk parts that are taken from a drill. This is still a simplistic, faulty design.

#### VERSIONS
If we have time, we will take it to work on the code and improve the robot's ability to perform different unique functions with the drill:
Use sensors to be able to function in certain sections

#### FUNCTION
<ul>
<li>The drill will be attached to an arm that rotates about a point in order to make the points to drill variable. (x-rotation)</li>
<li>Maybe make it go X/Y if we have the time for it?</li>
<li>We will use grippers to pick up the impact that has been drilled out.</li>
<li>Small stuff goes into the device or into a chute to the surface. The large stuff gets picked off the conveyor and deposited behind itself</li>
<li>Robot arm grips drill</li>
<li>Two arms, one for the drill and the other to pick rubbish off the conveyor belt
Servo motor to press button for drill?</li>
</ul>

#### LEARNING/RESEARCH
<ul>
<li>What ways can make the arm mobile in X/Y directions seamlessly without adding an extra unnecessary dimension?</li>
<li>How will we not blow up the earth in the process?</li>
</ul>

#### SUCCESS
We will be successful when:
<ul>
<li>There is something we can test the drill on</li>
<li>The robot arm is functional enough that the drill can be pressed and does what it needs to without going overboard</li>
<li>We do not start a World War and the mines do not blow up and destroy the earth.</li>
</ul>

#### SAFETY
For this project, we should definitely remember not to get unsafe. It's not necessary to resort to sketchy induction motors found on EBay or AliBaba to power any of this stuff, and all of these materials will be found in the Sigma lab. We will make sure the drill won't catch fire either as there should be an overload protection.

#### PROBLEM
We might have unexploded munitions beneath the school or something like that. Also our drainage systems kinda suck right now. We can solve this by digging out the munitions and drilling a new drainage system.

#### BILL OF MATERIALS
~~A few stepper motors~~ Using a TT motor instead of a steper motor<br>
~~A way to fabricate a metal drill (PLA will probably snap if used to drill sand)~~ We are going to use plastic<br>
~~Or a 50mm spade bit?~~ no


#### PSEUDOCODE
```
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
//Pin 9 and 10 make it so it tunnels at 45° for 3 seconds
//Level out after three seconds
//Drills straight for 5 minutes
//Return to surface by drilling for three seconds at 45°
}
```
#### SCHEDULE
```
SCHEDULE
March 4 - Start planning
March 12 - Finish planning, start CAD
April 12 - Finish CAD, start code
April 19 - Finish code and start testing individually
April 15 - Assemble project
April 26 - Revise and make improvements
May 20 - Finish improvements + documentation
May 24 - Project complete
```
Update April 29th, we have not finished the CAD we are about to start assembaly as we don't have a lot of time.

## Materials
<p>At first we wanted to use a large 1Kw motor I found in the back of the lab. I also wanted to use a 250mm drill bit. <br>
<strong>DO NOT TRY THIS THIS IS HOW YOU GET YOURSELF KILLED<br>
不要尝试这个，这样你就会丧命<br>
NO INTENTES ESTO ASÍ ES COMO TE MATAN<br>
NIE PRÓBUJ TEGO, W TEN SPOSÓB DASZ SIĘ ZABIĆ<br>
НЕ ПЫТАЙТЕСЬ ЭТОГО, ТАК ВЫ СЕБЯ УБИВАЕТЕ</strong></p>
<p>  
I now used a TT motor to drive the drill. This was connected to the drill bit. I used PLA for the drill and I had the drill directley connected to the TT motor. I had also used acrylic to try and print a gear box and gears. This did not work at all for me.</p>
<img src="https://github.com/solomon4000/planning-fuzzy-journey/assets/143544930/33008b02-db50-4799-bf82-00f92c1f7ba6">

## Wiring
Our wiring consisted of a solenoid, a TT motor, a limit switch, and an Adafruit M0. We made the wiring for the basic parts including the solenoid and the motor, but didn't get to finish the code or get to the bulk of it yet.
![Wiring Robot](https://github.com/solomon4000/planning-fuzzy-journey/assets/143544930/5c252582-c052-4969-bb49-08139c2bf5b8)



## Code
Here's the python code, excluding necessary delays. It should functionally get the solenoid on and off when the wiring is employed. We do not yet have the code to make it interactive or useful, but it's the only snippet of code I have for this project.
```python
import board # initiates board
import digitalio # allows communication with board output

solenoid = digitalio.DigitalInOut(board.D4) # pin that goes to solenoid is 4

solenoid.direction = digitalio.Direction.OUTPUT # solenoid is used as output

while True:

    solenoid.value = True # set as true
    solenoid.value = False # switch off solenoid
```
<a href="https://github.com/solomon4000/planning-fuzzy-journey/blob/main/Solenoid/Solenoid.py">Link to code</a>

## CAD
Here is the gearbox from a concntrated perspective:
![GOOD Motor (2)](https://github.com/solomon4000/planning-fuzzy-journey/assets/143544930/a3787f81-7784-4946-8ea3-ba2c27b54502)<br>
Isometric view of what we have so far of the CAD:
![GOOD Motor (1)](https://github.com/solomon4000/planning-fuzzy-journey/assets/143544930/be646114-76bd-43fc-ad34-475d1b0cc478)<br>
Including some bottom parts that were not finalized, but would have contributed to the final assembly:
![Part Studio 1 (8)](https://github.com/solomon4000/planning-fuzzy-journey/assets/143544930/e8d1e24f-579e-4d53-b86a-200c753859a1)<br>
Here are some parts we included before the final, but didn't end up using because of the limited functionality/mobility for the original gearbox, as well as feasibility in the Engineering lab:
![BAD motor V2 0](https://github.com/solomon4000/planning-fuzzy-journey/assets/143544930/750d3d3d-5aab-4425-9dda-16a647b904f5)

## Assembly
Here is the solenoid working. We didn't get the whole wiring done, but you can also see the TT Motor wiring.
https://github.com/solomon4000/planning-fuzzy-journey/assets/143544930/576641a3-9c59-4b93-8098-ad4ab420d84c
What little we have of the arm:<br>
![WIN_20240531_15_47_43_Pro](https://github.com/solomon4000/planning-fuzzy-journey/assets/143544930/682b74d5-f567-47ed-b8d5-ef7df315710c)

This is the solenoid in the solenoid holder. It cannot be held properly because I didn't yet mitigate the spring at the bottom of it, making the hole dysfunctional.<br>
![WIN_20240531_15_50_58_Pro](https://github.com/solomon4000/planning-fuzzy-journey/assets/143544930/2208133a-5444-49dd-98cf-f27b2286494f)

## Schedule
<table>
  <tr>
    <th>Task</th>
    <th>Intended schedule</th>
    <th>Actual schedule</th>
  </tr>
  <tr>
    <td>Start planning</td>
    <td>March 4</td>
    <td>March 4</td>
  </tr>
  <tr>
    <td>Finish planning, start CAD</td>
    <td>March 12</td>
    <td>April 11</td>
  </tr>
  <tr>
    <td>Finish CAD, start code</td>
    <td>April 1</td>
    <td>May 20</td>
  </tr>
  <tr>
    <td>Finish code and start testing individually</td>
    <td>April 9</td>
    <td>Not completed</td>
  </tr>
  <tr>
    <td>Assemble project</td>
    <td>April 15</td>
    <td>Not completed</td>
  </tr>
    <tr>
    <td>Revise and make improvements</td>
    <td>April 22</td>
    <td>N/A</td>
  </tr>
    <tr>
    <td>Finish improvements + documentation</td>
    <td>May 20</td>
    <td>June 2, sort of</td>
  </tr>
    <tr>
    <td>Project complete</td>
    <td>May 24</td>
    <td>N/A</td>
  </tr>
</table>

## Problems
We did not get to assembeling the robot. It was half complete and we didn't have the baseplate yet. Solomon really hoped we could finish this assignment in time.

One barrier that we ran into with the baseplate was how it could connect to the other parts. For the entire project, we were essentially still figuring out what we were doing. This was a big problem when attaching the gearbox initially, because we didn't even have a clear plan of what kind of gearbox/motor combination to use.

After working out problems with the gearbox and drill, we still didn't know how to incorporate a robot arm into it, since the whole initial point of the project was to have a robot arm (hence the name Robot Arm project). Raffi started with a basic arm from a previous assignmnet, but it didn't fit in many places and eventually, we ended up with an awkward bracket. But not even this could accomodate the Robot Arm.

## Reflection
We didn't learn much technically during this project, but we learned lots about conducting an effective project in the process. Most of our project was centered around basic Onshape capabilities on steroids, but only because we were trying to create something unique that didn't really have much functionality.

In terms of new projects in the future, we should definitely do a better job choosing more basic projects and adding meaning at the end. It's important to try to infuse a broader significance to the project, but without a good foundation, a good idea can't happen in the first place.

## Obituary
Solomon: We didn't finish this assignment in time. This was really sad. I should have picked a less ambitious project to work on this time. This is to bad honestley because it would have been nice to finish in time. I think I was far to distracted trying to help my freind in the lab thinking I could get my 6 profesionalism points back. I also ended up getting distracted while working on my own things and ended up spending some time hanging out with her.

Raffi: This project definitely came out to be more than I expected, considering I did not understand it in the first place. However, we didn't get any where close and I should do a better job mitigating the distraction and confusion with the project choice next time.
