def Drive_Mechanism_Testing_v1():
	1st Test:
		Notes:
			Pulley bores are eccentric..			
		Results:
			Very Bad.
			Big wobble everywhere
			Big tension difference throughout the cycle
			Wheel is wobbling			
		Changes to be made:
			Make pulleys concentric!
			Add ribs to motor mount if needed
			Spring pulley tensioner is needed
			Look at wheel attachment
			Look at motor/esc connectors at some point. Not urgent

		2nd Test:
		Notes:
			3D printed concentric pulleys			
		Results:
			Much better !
			Slight vibration on motor mount at high speeds
			Tension good, even.
			Belt shredding slightly more than al.
			No slipping at low torque.			
		Changes to be made:
			Test on the ground!
			Move to Drive_Testing
			Scrap the ESCs. Can only go forward.

def Drive_Testing_v1():
	1st Drive Test 
		Results:
			Drove in a straight line
			Took time and distance for the motors to get up to speed
			One motor more responsive than the other
			Wheel fell off !
		Changes to be made:
			Adjust lowest speed in the code, will not try to go too slow
			Add more weight, might help responsiveness of the motors
			Tighten set screws, flatten sections of the shaft

	2nd Drive Test:
		Notes:
			Adjusted code for smoother RPM setting, added weight
		Results:
			Slippage due to set screws. This needs to be adressed next
		Changes to be made:
			Flatten surfaces for the set screws

	3rd Drive Test:
		Notes:
			Testing a bigger gear ratio
		Results:
			Slightly smaller turning radius
			Tyres have no grip
			Motors have no holding torque when set to no speed
		Changes to be made:
			Add a top layer surface with more friction to the wheels
			Instead of stopping the inside motor, set it to a low speed

	4th Drive Test:
		Notes:
			Rubber added to wheels
			Tested running one wheel backward and one forward
			Changed the inside motor to slow rather than stop
		Results:
			One forward, one backward had good results. Started to turn on the spot until belt slipping.
		Changes to be made:
			Print better pulleys, exact profile
			Printing new bearing mounts, slight misallignment of the metal ones is not helping anything.
			Use a bigger gear ratio, more torque, less speed. Better turning.
			Ordered parts to allow each motor control two wheels. This should improve turning.

	General Notes:
		The printed pulleys are not as effective when force is applied to them. Even the printed exact profile one. 
		The al pulley is not fantastic either, dosent hold up under a huge amount of force. Maybe look at something with bigger teeth than GT2.

def Common_Problems_Solutions():
	Continous Beeping of the ESC
		Turn off.
		Turn on with throttle at highest
		Flip to lowest
		One beeping, turn off
		Restart at the lowest
	If git on PI becomes corrupt
		delete the folder
		clone again
		git clone git"github.com:DaisyAdelaide/gitcobot.git"

def Software_Main_Timeline():
	Learnt GitHub and Jupyter, and interfacing them
	Speech to Text working and writing to a csv, using googles libray
	Reading and writing to seperate csvs
	Tested out pocketsphinx, an offline speech to text, terrible accuracy
	Set up pi. Connected pi to GitHub
	Speech rec working on pi
	Added a led to indicate recording and a response to a direct command from a csv
	Spun the motor with a voice command from the pi
	Added face to gui, displays what it heard and a response

	Stated to investigate using pygame rather than guizero
	This allows moving features and constant updating of the screen whilst scanning for inputs, still using python

	Working on reading PWM on pi .. IMPOSSIBLE
	Set up arduino to read PWM, so much better
	Wrote code for controlling the motor with throttle and turning magnitude
	Looking at Rule based chat bots
	The arduino and pi are communicating over serial

	Current state:
		Nano is controlling Motors RC 
		PI is working with pygame for voice rec and response and basic 'face'
		PI and arduino Uno communicating

	The above was all combined into the PI as the hub, with the arduino acting as a 'motor driver'
	The PI and Uno are running while also listening for messages between each other

	Current State of the 'brain'
		8 Face frames designed on microsoft paint and implemented to animate the face
		The face blinks
		A button opens a seperate 'mode' and starts the chatbot
		The chatbot is rule based, it can ask a name and then say hi .. (the name), and similar for name suggestions for the cobot 
		The error when the voice fails to be decoded is being caught and the robot says 'I didnt catch that', much improves functionality
		Starting to test in the classroom, results are good!

def ESCs():
	YEP 120A ESCs were selected. These were selected as they are bidirectional, support the voltage and current requirements.
	The ESCs work with the RC reciever.
	The ESCs are not bidirectional. A programming card is needed to switch direction. Not possible to work in this project.

	There is only one bidirectional ESC on the market for such high voltage and current requirement. It is on backorder.

	Another option is the ODrive. This is a BLDC driver board. From my research, it would provide the best possible precision movement of the motors, it has its own firmware installed.
	This will be difficult to use as it is new to me and for everyone at zen also, but a good addition to the project. It will allow excellent control which is needed in a classroom envirnoment.
	This will be purchased and replace the ESCs. An encoder will be used in combination with it.
			
def Brain_Ideas():
	maths
	song 
	jokes
	google a question
	favourite function, number, tree, animal, colour DONE
	mark zuckerburg
	did you know

def Chassis():
	Original Plan:
		The chassis must be big enough to carry the crates.
		The design was completed as essentially a robot cart 
		After testing this proved very un manouvre friendly.
		The robot was only just small enough to fit through doors and didnt even have bumpers yet
		the turning radius was also very large, it would not be able to navigate around the classroom

	Version 2:
		The next design aimed to fix these problems.
		A much smaller more manouvreable chassis would be designed and it would drag a trailer with the buckets when needed
		This way the cobot would be much smaller and could potentially move around a classroom, and still complete the original brief.

		This new design is a roomba type robot, it is circular with two driven wheels and two castors.
		The front castor has suspension to allow it move over bumps better.


			


