# Drill Robot*
#### by Solomon and Raffi
*Formerly known as "Solomon's really really really really really really really really really really really really really really really really really really really really really really really really good project" and "RECORD: 1.9 GB"

## Planning
#### ROUGH SKETCHES/IDEAS
![Untitled](https://github.com/solomon4000/planning-fuzzy-journey/assets/90640484/7252a3d8-c401-4b5e-b52c-e14bf663f62c)


#### DIAGRAMS<br>
![Capture](https://github.com/solomon4000/planning-fuzzy-journey/assets/90640484/610121e8-d9fd-4019-bec9-05010f9b3550)


[Onshape document we will be using](https://cvilleschools.onshape.com/documents/c2a9d48291cc143e1c5c2e36/w/15419713e5234e2432e6f2f1/e/79c7b2bf3c5ad69468cf4189)

#### VERSIONS
If we have time, we will take it to work on the code and improve the robot's ability to perform different unique functions with the drill:
Use sensors to be able to function in certain sections

#### FUNCTION
The drill will be attached to an arm that rotates about a point in order to make the points to drill variable. (x-rotation)
Maybe make it go X/Y if we have the time for it?
We will use grippers to pick up the impact that has been drilled out.
Small stuff goes into the device or into a chute to the surface. The large stuff gets picked off the conveyor and deposited behind itself
Robot arm grips drill
Two arms, one for the drill and the other to pick rubbish off the conveyor belt
Servo motor to press button for drill?

#### LEARNING/RESEARCH
What ways can make the arm mobile in X/Y directions seamlessly without adding an extra unnecessary dimension?
How will we not blow up the earth in the process?

#### SUCCESS
We will be successful when:
There is something we can test the drill on
The robot arm is functional enough that the drill can be pressed and does what it needs to without going overboard
We do not start a World War and the mines do not blow up and destroy the earth.

#### SAFETY
For this project, we should definitely remember not to get unsafe. It's not necessary to resort to sketchy induction motors found on EBay or AliBaba to power any of this stuff, and all of these materials will be found in the Sigma lab. We will make sure the drill won't catch fire either as there should be an overload protection.

#### PROBLEM
We might have unexploded munitions beneath the school or something like that. Also our drainage systems kinda suck right now. We can solve this by digging out the munitions and drilling a new drainage system.

#### BILL OF MATERIALS
~~A few stepper motors~~ Using a TT motor instead of a steper motor
~~A way to fabricate a metal drill (PLA will probably snap if used to drill sand)~~ We are going to use plastic
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
Our wiring consisted of a solenoid, a TT motor, a limit switch, and an Adafruit M0
![Wiring Robot](https://github.com/solomon4000/planning-fuzzy-journey/assets/143544930/5c252582-c052-4969-bb49-08139c2bf5b8)

## Code
<a href="https://github.com/solomon4000/planning-fuzzy-journey/blob/main/Solenoid/Solenoid.py">Link to code</a>

## CAD
![GOOD Motor (2)](https://github.com/solomon4000/planning-fuzzy-journey/assets/143544930/a3787f81-7784-4946-8ea3-ba2c27b54502)
![GOOD Motor (1)](https://github.com/solomon4000/planning-fuzzy-journey/assets/143544930/be646114-76bd-43fc-ad34-475d1b0cc478)
![Part Studio 1 (8)](https://github.com/solomon4000/planning-fuzzy-journey/assets/143544930/e8d1e24f-579e-4d53-b86a-200c753859a1)

Here are some parts we included before the final, but didn't end up using:
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
    <th>Comments</th>
  </tr>
  <tr>
    <td>Start planning</td>
    <td>March 4</td>
    <td>March 4</td>
    <td></td>
  </tr>
  <tr>
    <td>Finish planning, start CAD</td>
    <td>March 12</td>
    <td>April 11</td>
    <td></td>
  </tr>
  <tr>
    <td>Finish CAD, start code</td>
    <td>April 1</td>
    <td>May 20</td>
    <td></td>
  </tr>
  <tr>
    <td>Finish code and start testing individually</td>
    <td>April 9</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Assemble project</td>
    <td>April 15</td>
    <td></td>
    <td></td>
  </tr>
    <tr>
    <td>Revise and make improvements</td>
    <td>April 22</td>
    <td></td>
    <td></td>
  </tr>
    <tr>
    <td>Finish improvements + documentation</td>
    <td>May 20</td>
    <td></td>
    <td></td>
  </tr>
    <tr>
    <td>Project complete</td>
    <td>May 24</td>
    <td></td>
    <td></td>
  </tr>
</table>

## Problems
We did not get to assembeling the robot. It was half complete and we didn't have the baseplate yet. I really hoped we could finish this assignment in time.
## Reflection

## Obituary
We didn't finish this assignment in time. This was really sad. I should have picked a less ambitious project to work on this time. This is to bad honestley because it would have been nice to finish in time. I think I (Solomon) was far to distracted trying to help my freind in the lab thinking I could get my 6 profesionalism points back. I also ended up getting distracted while working on my own things and ended up spending some time hanging out with her.
