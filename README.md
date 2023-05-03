# INTRODUCTION
## Game Name: Asteroid Defense
![Game Image](assets/Game%20Image.png)
### Software Needed to Run Game:
-	Python 3.11
-	Pygame 2.1.2
-	Git Bash
-	Visual Studio Code
### Instructions on Download:
1.	Download Git Bash (https://gitforwindows.org/).
2.	Open File Explorer.
3.	Create a folder to keep game.
4.	Open Git Bash.
5.	Use the “git clone” command to clone the game repository into your new folder.
a.	git clone https://github.com/Ethan-Eill/Asteroid-Defense
6.	View all the files and folders from game.
7.	Open all of the python files in an IDE such as Visual Studio Code.
8.	Run the main.py file.
### Game Controls:
-	WASD: Movement (relative to where spaceship is facing)
    - W: Moves the spaceship forward
    - A: Moves the spaceship to the left
    - S: Moves the spaceship backwards
    - D: Moves the spaceship to the right
-	Mouse: Aim/Turn Spaceship
-	Left Mouse Click: Shoot


# GAME DESIGN
## Mechanics/Technology
### Gameplay Loop
The gameplay loop of the game lies within the start_game() function of the code in the view layer. The loop first determines the difficulty of the game chosen by the player before clicking the play button(in difficulty settings). There are different levels of difficulty which includes easy, medium, and hard. Each have a different difficulty modifier in order to modify the asteroid production. The asteroids are produced randomly and spawns from different sides of the game map. The asteroid speed also depends on the difficulty chosen by the player. Afterwards, the loop determines if the player collides with an asteroid or not. If the player collides with an asteroid, the player loses a life. The player has a total of three lives to play the game. Subsequently, the loop determines the bullet collision with an asteroid. If a bullet does collide with an asteroid, the player gains 10 points to their score, regardless of the size of the asteroid. If the bullet collides with a large asteroid, the large asteroid splits into two medium asteroids. If the bullet collides with a medium asteroid, the medium asteroid splits into two small asteroids. If the bullet collides with a small asteroid, the asteroid is destroyed and disappears from the game map. The loop continues by determining different button clicks during the game. If the player clicks the left mouse button, the spaceship fires bullets. If the sound option is turned on, then the bullets make a laser sound. If the player clicks the keys WASD, then the spaceship will move relative to where the spaceship is facing. The player can also press the Esc key to pause or quit the game. Afterwards, the loop determines if the player has lost the game. If the player loses the game without a new high score, then a Game Over message will display. Afterwards, the list of high scores from each difficulty level will appear on the screen. The player will then have the option to play the game again or click quit to exit the game. If the player loses the game with a new high score, the game will let the player enter a three-digit name. After the player clicks continue, there will be a list of high scores from each difficulty level. The player will then have the option to play the game again or click quit to exit the game.

### Core Mechanics
The core mechanic of this game includes health. Health is a game mechanic that determines the most amount of damage a thing can take before leaving the game loop. In Asteroid Defense, there is an implementation of health in the main game loop. The implementation of health in this game is not a typical health bar but rather just hit points or lives. Hit points or HP is the total amount of hits it would take to defeat a player. In this game, the player has three HP. This means that the player can get hit by an asteroid of up to three times. If the player hits the three HP mark, they are defeated, and the game will be over.

### Game Gimmick
The game’s gimmick lies within the controls of the game. The controls to move the spaceship in a certain direction are WASD. The W key moves the spaceship forward. The A key moves the spaceship to the left. The S key moves the spaceship backwards. The D key moves the spaceship to the right. The controls sound relatively straightforward for the spaceship. The game has a gimmick where the controls are relative to where the spaceship is facing. If the spaceship is facing towards the top of the game map, then the spaceship will reflect the original controls of WASD. An example of where the gimmick enters is when the spaceship is facing to the right or any other direction in a 360-degree axis. If the spaceship is facing to the right, the controls will be the same, but the controls will move the spaceship relative of where it is facing. This means that the W key will move the spaceship forward to the right of the game map. The A key will move the spaceship to the top of the game map. The S key will move the spaceship backwards to the left of the game map. The D key will move the spaceship to the bottom of the game map. This applies for the other directions the spaceship can face in a 360-degree axis. This gimmick can get annoying and confusing to deal with when also dealing with asteroids spawning from different sides of the map. Another gimmick that can be considered is the asteroids. When the large or medium asteroids are hit by a bullet, the asteroids split in two. Two large asteroids split into two medium asteroids and two medium asteroids split into two small asteroids. This gimmick also contributes to the game to make a game a bit more challenging. It can also get annoying dealing with different types of asteroid sizes flying towards you.

### Game Difference
This game is different from other games in the same genre because of the survival theme of the game. Many spaceship games involve missions and objectives to progressively advance through the game. Other games also have upgrades that can be utilized when a certain level or point is reached. This game’s main theme is to survive the onslaught of asteroids spawning on the screen while also obtaining points. There is no upgrade component to this game which makes this game more challenging to survive from asteroids. Another aspect that makes this game different from other games is that the direction movement controls are relative to the spaceship rather than to the game screen. 

## Player Experience
### Player Challenges
There will be many types of challenges that the player will face when playing the game. One challenge is that the WASD controls can confuse the player. The WASD keys move the spaceship in a certain direction. W moves the spaceship forward. A moves the spaceship left. S moves the spaceship backwards. D moves the spaceship right. The challenge kicks in when the player needs to aim and shoot while also moving the spaceship in a certain direction. They will start to see that the controls move relative to where the spaceship is facing and not relative to the game screen. This can play with the player’s head for a little bit before they get use to the controls. The player will overcome this little gimmick by constantly playing the game and getting use to the controls. Another challenge that the player will face is the asteroid production. The asteroids are produced and spawned randomly from all directions. This will cause the player to have to move and shoot the asteroids without getting hit while also dealing with the WASD control gimmick. The player will overcome this by constantly playing the game and getting use to the asteroid production. If the asteroid production is too much, the player can also change the difficulty level of the game.

### Player Rewards
There is a reward that the player will receive for progressing through the game. After the player loses the game, there will be a total score displayed to the screen. If the total score beats another high score, then the player will have the opportunity to type in three letters to represent themselves. After the player types in their name, there will be a list of high scores from each difficulty displayed to the player. The reward for progressing through the game and doing better than a previous round is being put on the list of high scores. The player will be able to see their name on the list of high scores when their score is high enough to be on the list.

### Player Feedback
The feedback that the player will receive while playing the game involves the score. Every time the player shoots an asteroid, they are rewarded 10 points. The score will constantly be updated every time the player shoots an asteroid. This feedback shows constant progress in the game so that the player knows if their score is high enough to make it to the high scoreboard or if they beat their own previous score.

### Audio/Visual Elements
The elements that will enhance the player’s experience involves the audio effects. The audio effect provided for this game is a space arcade audio effect to make the game seem more vintage and old-school. Another audio effect added is that when the spaceship shoots, a laser sound is played. This makes the game seem more like an old arcade game. The final audio effect provided for the game is a game over sound effect that also gives the game an old school vibe to it when the game is over without a new high score. All of these audio elements provided are meant to enhance the player’s experience by giving an old school arcade vibe to the game. This can help the player connect better with the game and add a sense of nostalgia. The player will also have the option to turn the sounds effects off if the player finds the sounds to be too distracting.


# GAME DESIGN CHANGES
### Original Design and Concept
The original game design and proposal for this game was that Asteroid Defense will be categorized as a 2-D arcade shooter game, with a hint of strategy. The player will control a spaceship trying to defend their home planet from incoming asteroids. The objective of Asteroid Defense is to destroy the incoming asteroids as quickly as possible before they pass by you and damage your home planet. The unique game element that separates Asteroid Defense from other 2-D arcade games is the leveling and skill tree aspect of the game. As the spaceship defeats incoming asteroids and passes different waves, the spaceship will earn experience points. With these XP points, the player can upgrade their spaceship by unlocking new abilities and increasing their strength via the skill tree. The skill tree will follow a tree like pattern where one ability unlocked will open up a new ability to be unlocked. The player will be able to navigate their spaceship all across the screen, however they must make sure they avoid and destroy any incoming asteroids. The spaceship will be able to shoot and destroy the asteroids in order to earn XP points. The XP points earned will help the player level up in order to unlock new abilities. The skill tree will have three different categories of upgrades that the player can earn. The first will be defense and health related upgrades. This includes things such as, more health, mobility upgrades and more. The next category of upgrades will be the combat category. This category will include upgrades such as increased damage dealt, faster fire rate, etcetera. The final category of upgrades will be the utility section. This branch of upgrades will include new abilities to be unlocked and help you survive the waves of asteroids.

### Design Change Over Time
The game design has changed constantly throughout the development of this game. We had a lot planned for this game to try and make it as original as possible, but there were many challenges that we faced during the development of the game. We planned to have a skill tree for the game, where the player could unlock different upgrades for their spaceship based on the experience they gain. This particular feature had to be cancelled due to technical as well as adaptive challenges that we have faced during the development process. The technical challenge we faced with the skill tree is that just implementing something like this is challenging in and of itself. The adaptive challenge ties into this technical challenge where both of us have such differing schedules to meet and work on the project early on in the process. Because of the adaptive challenge preventing us from working on the project and starting early, we had to cancel the skill tree feature. The complexity of creating a skill tree is high, which is also another reason why we had to cancel this feature. Another entity that we planned to have in the game is a planet entity. The original idea is to have a spaceship protect a planet from asteroids. The planet would be its own entity and have a health bar. It would take damage when hit by an asteroid and explode if the health bar was empty. Similar to the feature above, there were adaptive challenges that we both faced during the development process. We both have such differing schedules and each of us had loads of assignments, exams, and projects every week. This prevented us from starting the implementation of the game early in which we had to sacrifice and take some things out. The planet entity is another one of the things we had to take out due to schedule issues.

### Original Plan for Game Mechanics 
The original plan for the game mechanics included health, experience points, and power-ups. The spaceship would have a health bar and the planet entity that we planned early on would also have a health bar. The plan for health changed by having a spaceship have lives rather than a health bar, and the planet entity was removed completely from the game so there was no implementation of a health bar. The reason the plan changed is because of the technical and adaptive challenges mentioned above. There were packed schedules as well as meeting conflicts that prevented us from starting early and implement these ideas. Experience points would be gained if the spaceship were to destroy and asteroid. Since the skill tree idea was removed from the implementation of the game, the idea of experience points also diminished as well. The reason we removed the idea of experience points was because we did not find a need for it after removing the skill tree. Why have experience points if it was not going to upgrade the game? The reason we removed the skill tree is because of the technical and adaptive challenges we faced. The complexity of creating a skill tree is extremely high and the packed schedule that we both faced did not help contribute to creating the skill tree early on in the development process. For this reason, we removed the skill tree which made us also remove the experience points as well. The power-ups were going to be implemented in the skill tree in order to upgrade the shooting and durability of the spaceship. Since the skill tree was removed from the game, the whole idea of power-ups also diminished. The reason we removed the skill tree is mentioned above. 

### Original Plan for Game Gimmick
The original plan for the game gimmick was to have a skill tree in order to upgrade the spaceship’s shooting ability as well as durability. This idea has been removed from the implementation of the game due to adaptive and technical challenges we have faced during the development process. The adaptive challenge we face is scheduling conflicts. We both have such packed schedules, having assignment, exams, and projects every week. Our schedules are also different which makes it harder for us to meet and work on the project. The technical challenge we faced is the skill tree itself. The complexity of creating a skill tree in a short amount of time is almost near impossible. For these reasons, we had to abandon the skill tree from the implementation. In replacement of that gimmick, we added a smaller gimmick. This gimmick lies within the controls of the game. The controls to move the spaceship in a certain direction are WASD. The W key moves the spaceship forward. The A key moves the spaceship to the left. The S key moves the spaceship backwards. The D key moves the spaceship to the right. The controls sound relatively straightforward for the spaceship. The game has a gimmick where the controls are relative to where the spaceship is facing. If the spaceship is facing towards the top of the game map, then the spaceship will reflect the original controls of WASD. If the spaceship faces a different direction, then the controls adjust to where the spaceship is facing. An example is provided in the gimmick section of this document. This gimmick can get annoying and confusing to deal with when also dealing with asteroids spawning from different sides of the map. This little gimmick is not a big one, but it makes the game a little bit more unique and obnoxious to deal with initially. Another gimmick that can be considered is the asteroids. When the large or medium asteroids are hit by a bullet, the asteroids split in two. Two large asteroids split into two medium asteroids and two medium asteroids split into two small asteroids. This gimmick also contributes to the game to make a game a bit more challenging. It can also get annoying dealing with different types of asteroid sizes flying towards you. This gimmick also makes the game a bit more unique since the common collision from a bullet to an asteroid is the asteroid being completely destroyed. 


# GAME DEVELOPMENT AND DOCUMENTATION
## All Classes and Major Functionality Methods
### Controller.py
Functions:
-	init(): initiate the game.
-	game_loop(): the main game loop that controls all the input while playing the game.

### Main.py
Functions:
-	main(): initiate the game and run the main game loop from controller file.

### Model.py
Classes:
-	Space_Ship()
    -   Functions:
        - init(self): initializes the stats of the spaceship.
        - update_ship(self, mouse_x, mouse_y): move ship and keep ship inbounds.

-   Bullet(object)
    -   Functions:
        - init(self, player): initializes the stats of the bullets.
        - move(self): determines how the bullets move.
        - draw(self): draws the bullet.
        - check_off_screen(self): determines if the bullet moves off the game screen.

-	Asteroid(object)
    -   Functions:
        - init(self, rank): initializes the stats of the asteroid.
        - draw(self): draws the asteroid.

### View.py
Functions:
-	init(): displays the initial setup for game window and display.
-	main_menu(): displays the main menu screen.
-	difficulty_screen(): displays the difficulty settings screen in options.
-	menu_shut_down(): closes the menu.
-	change_sound(): option to turn on/off game sound.
-	in_menu_options(): displays all buttons and options when menu is open.
-	in_game_options(): displays all buttons and options when game is playing.
-	pause(): pause functionality while in game.
-	check_new_wave(wave_number, score): checks if a new wave should begin.
-	start_game(): the game loop of the main game.
-	gameover_screen(): displays the game over screen.
-	stats_screen(score): displays the high scores of each difficulty.
-	enter_new_highscore(score): allows user to enter new high score.
-	display_scores(dif_txt, width_1, width_2): displays the score of the player.
-	change_highscore(user_input, score): replaces a high score if a new high score is achieved.

### Model-View-Controller Details
The game is implemented in a model-view-controller architecture pattern. The model represents the current state of the game. This section includes the game entities such as the spaceship, bullet, and asteroid. The model is updated based on player input and other game logic implemented in the functions. The view layer is responsible for rendering the game to the player. The view is updated based on the current state of the game model. The view layer takes the information from the model through the controller layer in order to update and display the information to the screen. The view layer has many different functions to display specific information/features to the screen. The controller layer is responsible for passing information between the model and view layer when necessary. The controller handles the game state through the game loop and passes the game state to the view layer to display.

### Bugs/Flaws
There are not any major bugs or flaws in the game that we are aware of at the current moment.

### Collaboration/ Code Versioning Tools
The tool we used to facilitate collaboration and code versioning is Git/Github as well as Visual Studio Code.


# GROUP MEMBER ROLES, TASKS, AND PERFORMANCE
## Division of Labor

For the development of this game, we followed the SCRUM methodology for the workload. This included meetings each week. In these meetings, we discussed what we have finished, what we will be working on, and any blockers or problems that we faced. We both were not responsible for any particular section but rather we split up the workload based on our sprint goals. For example, for one week, we met and one of us was responsible for the spaceship display and movement, and the other was responsible for asteroid creation and movement. This allowed us both to get a solid understanding of the MVC development process as well as a better understanding of how larger projects should be handled in the future.

## Updated Project Timeline/Outline
### Milestone 1: March 30
-	Task 1: Spaceship
    -   Justin: 100%
        -	Created model for spaceship.
-	Task 2: View Layer
    -	Ethan: 100%
        -	Created view layer for the main menu.

### Milestone 2: April 18
-	Task 1: Spaceship
    -	Ethan: 80%, Justin: 20%
        -	Created model for spaceship.
        -	Functionality, make sure spaceship movement works.
-	Task 2: View Layer
    -	Ethan: 100%
        -	Created view layer for the main menu.
        -	Spaceship shows up in view layer.
-	Task 3: Asteroids: 
    -	Justin: 100%
        -	Randomization and Speed, make sure asteroid production is random and how fast they fly depending on level, still needs to be put and tested in view layer.

### Final Game Submission: May 3
-	Task 1: Spaceship
    -	Ethan: 100%
        -	Shooting works 
-	Task 2: Collisions
    -	Ethan: 100%
        -	Spaceship, asteroids, bullets, and planet each have unique collision factor.
-	Task 3: View Layer
    -	Ethan: 100%
        -	All model changes can be updated and presented to screen.
-	Task 4: Controller Layer 
    -	Ethan: 50%, Justin: 50%
        -	Make sure all data is passed from model to the view.
-	Task 5: Updated Game Document
    -	Justin: 100%
-	Task 6: Completed and polished game
    -	Ethan: 70%, Justin: 30%
-	Task 7: Completed Game Document game
    -	Justin: 100%

### Final Game Presentation: May 4
-	Present game during final period of this class (Deadline: May 4)

As stated in our project proposal, we both are not individually responsible for a particular section but rather we split up the workload based on our current sprint goals. 

### Cancelled/Removed
-	Skill Tree: Ability Options and Choice Selection, make sure the skill tree has good  number of options and see what happens when player chooses an ability on one branch of the tree. 
-	XP Production: make sure XP is received when an asteroid is destroyed.
-	Planet: Model and Health, make sure planet has health bar and takes damage when hit by an asteroid.
