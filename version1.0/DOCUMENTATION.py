def GIVEN_CONSTRAINTS():
	One robot body that could carry the buckets.
	Less than 51 pounds.
	Remote Control.
	Can interact with children and have voice command/interaction.

	As not many constraints were given, I followed these quite strictly. I did not consider that a trailer may be a better option
	as there were only a few requirements given and I needed to start somewhere.

	Get the kit to the classroom.
	Interact with the students. 
	Initially only fun and excite them for robotics, moving forward maybe more comprehensive functions to learn about the robot.
	Be able to manouvre around a classroom.
	Be able to access anywhere a wheelchair can.
	Each part less than 51 pounds.
	Be 100% controllable.
	Be on a low budget.

	Fr60 Cyr5

	He3/ R and D

	He3/s 5nstr4ct6rs and teaches r6b6t5cs

def Ideation():
	Drive Mechanism:
		Different options were considered. 
			Direct Drive:
				No oportuinty for suspension. Any bumps would cause direct vibrations in the robot.
				It would be difficult to contain everthing under a 'hood'. I wanted to avoid having any finger pinching points.
				More difficult to design mounting. As weight is a key concern we cannot have heavy frames to support the motor,wheel,bearings at the 
				same point on the structure.
			Tracks:
				This option was considered with the possibility of adding stair climbing ability to the robot.
				I quickly ruled this out as even if it could be done the torque needed to get the robot up the stairs
				with the buckets of kit would be quite substancial, upping the batteries needed quite a bit. This also started the problem of diminishing returns as 
				as we add batteries, we add weight and so need more batteries. I did not want to pursue this as it would consume the restraints for the design and while
				stair climbintg would be an excellent feature it is not a strict restraint.
				Considering this, I decided that tracks would not be nessesary and wheels could be much neater and contained inside the robot much better than tracks.
			Belt Drive:
				This option solves some of the problems discovered above.
				The belt will help absorb some vibration to allow smoother driving.
				The belt also means that the motors and electronics can be contained within the body of the robot.
				We can also control the ratio of the pulleys meaning we have more control should we need more power or speed. This would be customizable much later into
				the design meaning changes can be made after testing.
				This drive mechanism was selected based off these considerations.

	Belt Drive:
		Once it was decided that a belt drive would be used, I started designing different options for this.
		The first task was to design the motor mounts. These had to be strong to support the motor. It was decided that a frame of 80/20 would be used. The motor
		mounts had to attach to this. The mounts that came with the motors would not provide enough height for the motors to be mounted above the frame. Different options were designed.
		These can be seen in motormountings.JPEG.
		The full rectangle was chosen to add some structural support rather than the cross.

		The initil design of the drive mech can be seen in motor_mount.JPEG.
		Originally four wheel drive was designed but due to budget it was decided that we would start with two wheel drive and complete testing before upgrading to four wheel if needed.
		This initial four wheel drive can be seen in images marked with 17/05/22 and 18/05/22.

		After recieving feedback on this design it was noted that having the wheels attached at just one point on the frame was a weak structural desicion.
		Should the wheels be mounted at two points of contact the turning moment produced with one point of contact would be minimized. 
		Additional vertical extrusion was added to the frame. This would serve both the wheels but would also add some additional structural support to carry the weight of the load.
		This can be seen in fulldesigndetail.JPEG.


	Shape 1:
		As within the constraints the robot has to be big enough to carry the kit buckets. This was not considered an option.
		The smallest possible frame that could contain the buckets was designed.

		Thermoforming was suggested for the main cover. This would be a end game addition. 
		To prototype different ideas 3D printing will be used.

		The shape of the cobot evolved over time. This included the place where the load (buckets) would be stored.
		In the original design the buckets were stored raised above the frame. This was to allow space for the electronics beneth the cargo. This can be seen in chassis.JPEG.
		The flaw with this design is that the bulk of the weight of the robot would not be utilising the extrusion for support. Should this design be implemented the frame would need to extend
		upwards, and make a box type shape to ensure the weight was directly supported on the frame. This was not ideal, and an obvious design flaw. 

		To avoid this additional structural building, a new design was made. The idea is that the buckets are seated directly on the frame utilising the support from the existing extrusion.
		Feet would be placed on the frame to ensure the buckets didnt slip. This can be seen in cobot.JPEG and fulldesign1.JPEG.

	Motors:
		When looking at motors many existing similar systems were looked at.
		These are the following; 
			Wheelchairs
			Scooters
			Kids toy cars (ride on cars)
			eBikes
			Skateboards
		Many of the above motors were brushed DC. I decided to use brushless for the following reasons.
			Less Maintence.
			Better Control.
			Rated for torque rather than speed. We will need to focus on carrying weight and moving slowly.
			More reliable.
		The next step was to look at the options available.
		This was based on both what we need but also what we can get. There are not a ton of options for the kind of power and control we need.
			We need essentially industrial robotic motors. We need fine control and also power. Industry uses variations of servo motors which are very expensive. BLDC motors 
			are a very good replacement of this, initially intended for 'hobby' use.
			Lead times are a major factor.
			Budget is also a factor. There was no figure available, rather, as little as possible.
		The full list of considered motors can be seen in motors1.JPEG and motors2.JPEG

	Electronics:
		The breif given for the software aspects are as follows:
			The robot must be able to interact with children
			Be remote control
			Listen and execute voice commands
			Must have a touch screen
		The following options were considered:
			The touch screen could have buttons/games/information
			A sentient face could be implemented
		I decided that to begin with a face would be implemented and following this different screens could be accessed.
		A raspberry pi was chosen as it will be sufficient and we have lots available. The Nvidia Jetson was considered but the lead time at the time was anywhere up to 2 years.

		See Software_Main_Timeline for a detailed analysis of the software development.

	Chassis:
		Original Plan:
			The chassis must be big enough to carry the crates.
			The design was completed as essentially a robot cart.
			This design process can be seen in more detail in shape 1.
			After testing this proved very un manouvre friendly.
			The robot was only just small enough to fit through doors and didnt even have bumpers yet.
			The turning radius was also very large, it would not be able to navigate around the classroom.

		Version 2:
			The next design aimed to fix these problems.
			A much smaller more manouvreable chassis would be designed and it would drag a trailer with the buckets when needed
			This way the cobot would be much smaller and could potentially move around a classroom, and still complete the original brief.

			This new design is a roomba type robot, it is circular with two driven wheels and two castors.
			The front castor has suspension to allow it move over bumps better.

			Please see Chassis_version_2() for a detailed design process on this version.

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
	Tested out pocketsphinx, an offline speech to text, terrible accuracy.

	Set up pi. Connected pi to GitHub
	Speech rec working on pi
	Pyaudio was originally used to do this. This was then tested on the Pi. The same script did not work. After lots of research and troubleshooting it was discovered that 
	PyAudio was not a good fit for the Pi. Another package called SpeechRecognition would work much better. This was implemented.

	Added a led to indicate recording. This means that the script can work without checking the cmd prompt for updates.
	A direct response to a direct command is given from a csv. This is just printed on the screen.

	The next step was to integrate the motors.
	Spun the motor with a voice command from the pi
	Added face to gui, displays what it heard and a response

	Stated to investigate using pygame rather than guizero
	This allows moving features and constant updating of the screen whilst scanning for inputs, still using python

	Working on reading PWM on pi .. IMPOSSIBLE
		The pi is not set up to read PWM signals. I attempted doing this using analog reading of when the signal is high/low but it is not very accurate.
		Testing this I could produce a graph but I could see inconsistancies with my eyes nevermind the numbers. This would not do for the kind of control we need.
		Next the arduino was tested for recording PWM signals.
	Set up arduino to read PWM, so much better
	Wrote code for controlling the motor with throttle and turning magnitude
		The short alforithim works as following:
			The throttle sets the absolte value. This means that if the throttle is set to the lowest, even to one side(indicating turning) it will not move.
			This ensures that the robot will not turn faster than you ever set the throttle to be.
			The magnitude is then set to be a factor of how far the side to side is on the same throttle stick.
			This is varient so you can turn slowly or on the spot.
			This goal is to give lots of control and allow different kinds of turns.

	Looking at Rule based chat bots
	The arduino and pi are communicating over serial

	Current state:
		Nano is controlling Motors RC 
		PI is working with pygame for voice rec and response and basic 'face'
		PI and arduino Uno communicating

	The above was all combined into the PI as the hub, with the arduino acting as a 'motor driver'
	The PI and Uno are running while also listening for messages between each other
	This can be seen in data1blockdiagram.JPEG.

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

def Chassis_version_2():

	The goal of this chassis is to overcome the issues with the original design.
	This chassis will be a 2 part unit. There will be a small manouvreable unit along with a trailer for the buckets.

	To understand this design explanation please view the diagram alongside.

	The constraints considered were;
		The size. This is two fold.
			A smaller size to manouvre around the classroom.
			A size that can be 3D printed. This is to due to being able to produce a shell around the chassis without Thermoforming.
			The goal will be to print the whole piece.
			I decided that four quaters would be managable and remain sturdy and so set this as the constraint, making each quater as big as possible on the printers.
		Reusing Parts.
			As this is a second design and budget is a key factor I wanted to use as many of the previous parts as possible.

	The design:
		As mentioned the outer limit on size was set.
		As with the previous design, 
			I aimed to have the drive mechanism contained within the chassis.
			Wheels mounted at 2 points.
			Belt Drive.

		Some options are considered below. Please refer to smaller_chassis1.JPEG and smaller_chassis2.JPEG.

		In design one, the two driven wheels are at the front and one castor is at the back for balance. The benefits of this design is that the driven wheels are at the very front of the chassis 
		providing excellent control for turning and can assist with getting over bumps. Although, the front still has corners. The turning radius is also not minimised, the robot has a turning radius
		the length of itself. It could spin on the spot but would need the centre distance between the two wheels. While this is an improvement on the original design, it could be better.

		The second design consists of a circular shape. This aims to reduce the size of the chassis from above. The issue here is that the drive mechanism is exposed. This is due to the wheels being
		placed at the widest distance of the chassis, apart from one another. This is to give the best chance at turning and for balance. Putting the wheels closer together, a smaller width than
		the widest section of the chassis would result in some of the chassis extending over the wheels. This would be unstable. The turning radius is the centre distance between the wheels and the 
		castor similar to above.

		The third design aims to enslose the drive mech within the body, while avoiding the issues in design one. For these reasons the wheels were placed at the back. Once considered it is 
		evident that the control of this chassis when driving would be minimal. The front castor has no control at all. This is not possible.

		The next design, design 4, is looking at a circular shape again. Instead of putting the wheels at the front, they are placed in the centre, at the widest section of the chassis. To allow this design to 
		work the majority of the weight would need to be placed at the back to ensure the front dosent drag on the ground. While this may work, it opens up lots of problems regarding balance.
		If the robot was pushed or the weight became unabalanced it could very easily tipped forward. It is also only using half of the chassis for storage, as the front would have to be essentially 
		empty for it to be light. This causes many issues for the drive mechanism as there is no longer space for both motors, the battery ect.

		Considering all of the above options it is evident that a circular shape is the best. It has a turning radius of zero, it can turn on the spot. The drive mech can be contained within, there are
		no corners, it can move in any direction easily. It is also a symetrical shape and very asthetically pleasing. Looking at the movement of roombas we can see how effective the circle shape
		is. 
		By adding an additional castor at the front all of the problems of design 4 would be solved, while all of the benefits would remain.

		The final design is design 5. 
		The castor at the front is nessesary for balance, suspension will be added as if it were static it would cause vibrations through the whole chassis on bumps. This can be seen in 
		smaller_chassis2.
		The four quaters of the chassis can be printed. The round shape will be able to complete on the spot turns and can move backwards with the same accuracy 
		as forwrads should this be nessesary. 

		To view an image of this version of the chassis with the head please view newchassis.JPEG

def DRIVE_MECH_TESTING_v2():

	Test 1:
		Notes:
			Initially the tyres just spun.
			There was no traction.
			I used a piece of wood as the floor, the cobot moved forward.
		Results:
			Not enough grip on the tyres.
			The printed filastic tyres, I have added teeth to the tyres reducing the surface area of the grip.
			Forgot to check current draw
		Changes to be made:
			Use elastics around the tyres
			Highten the front castor to ensure the drive wheels are set on the ground

			Calibration Problems:
				Test 1 19/08/22:
					Set up:
						Code: M1 first, with 1000ms delays
					Results:
						MO, black wires, working
						M1, red wires, not working
				Try Again:
					Results:
						The same

				Test 2:
					Set Up:
						M0 first
						same 1000ms delays
					Results:
						both working
						not consistant

				Test 3:
					Set up:
						M0 still first
						Added longer 2000ms delays
					Results:
						Working consistantly, hasent failed yet
						The calibration sequence needed time to complete
						Problems Solved

		Test 2:
			Notes:
				Fixed the calibration problems
			Results:
				Excellent test
				Drove around the workshop
				see video on my phone 18/08/22 9:30
				Slight slipping
			Changes to be made:
				Set screws

		Test 3:
			Notes:
				Angle grinded the shafts to allow better grip for the set screws
				Testing turning code also
				Turning code: view image turning_algorithm.JPEG.
			Results:
				Excellent, no slipping yet
			Changes to be made:
				None! Drive mech working well, move to weight testing.

		Test 4:
			Notes:
				Weight testing!
			Results:
				I originally used a skateboard as a makeshift trailer. I first tested a bucket of kit for a large classroom.
				The cobot had no problem pulling this. 
				I then pulled myself, about 70 kg on the skateboard. No problem! The cobot will never need to pull this much but it is good that
				there are no problems with traction, stalling ect.
			Notes:
				The current being drawn with me on the skateboard was only 0.3A. This is very low. The speed was a low walking speed.
				
def CALIBRATION():
	Arduino Code
	The motors were calibrating every time the arduino reset, this is not nessesary. The motors only need calibrating when they are powered on and off.
	To solve this channel 5 on the RC is used.
	When the switch is put down it initiates the calibration sequence. This can hence be done multiple times and on demand if nessesary.
	This will be very useful during testing with the pi.
	Must remember to put the switch down and straight back up once the sequence has been initiated.

def FVP():

	The first viable product has been reached. The cobot is fully built. The battery is installed. The waterjet pulleys have been installed also.
	Performance:
	The face : 
		The face has three modes at the moment. The base screen is just a blinking face. Once the robot starts to drive the eyes go into the shrinking mode.
		The speaker also starts playing a beep boop noise while driving. 
	The chat mode:
		When entering the chat mode, the robot will no longer make noise while driving. It will speak 'hello how are you' when the left throttle is maxed 
		on the remote control.
		Other than this it is button controlled. Once the user presses the record button it records the phrase and produces a response.
		This response is spoken on the speaker.
	The maths mode:
		When entering the maths mode, again the robot does not make noise when driving. I feel it would just be too disruptive but maybe not.
		Again when the right throttle is maxed the robot says the sum and initiates the answering process.
		The answering process can also be initiated from pressing a button on the robot head.

	Mechanical:
	The Drive Mech:
		The new pulleys have eliminated the slipping on the smaller pulley. This was caused from the wear on an interference fit on the motor shaft.
		While this is an improvement, due to the motor shaft being hand grinded the grind was not completly straight. This left the pulleys sitting slightly
		crooked. This is causing some extra wear on the belt but not slipping still. The pulleys were also too fat and do not really fit well on the shaft.
		They were also superglued on.
		The big pulley was just not holding. The set screws were not strong enough. I ended up supergluing the flange connectors onto the shaft which did
		actually solve the problem, although I dont think this is a good solution.

		The castors are too low causing some problems going over bumps and reversing. The traction of the drive wheels would also be slightly better if 
		these were made higher.

		Overall, there are some hacky aspects to the drive mech which should be eliminated in the next version but end of the day it is 
		working well and holding up so far.	

	Problems to fix:
		The drive mech as described above ... good luck
		The cable management in the head , make a hole in the bottom of the head and also at the bottom of the neck.
		Make the head spin ? Think about remote, no more controls really unless I start doubling up but that is very complex to remember.
		Screen is not even, fix that
		Maybe look at increasing clearance on the wheels, would require smaller pulleys ?
		Wooden dowels not pla
		Maybe look at better graphics/emotions, different blinking funcitons depending on emotion ?
		Sensors ? Maybe look at some distance sensors to avoid collisions, where would these go ?



			


