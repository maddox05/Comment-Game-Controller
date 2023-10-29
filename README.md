
<h1 align="center">
  <br>
  Comment Game Controller 🎮
  <br>
</h1>

<h3 align="center">Plays games from live stream user comments!</h3>
<h4 align="center">Python script to control games using YouTube and TikTok comments</h4>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#prerequisites">Prerequisites</a> •
  <a href="#important-information">Important Information</a> •
  <a href="#setup">Setup</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a> • 
  <a href="#disclaimer">Disclaimer</a>
</p>

<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGU3OGJlMzdiODk5MTU3NDUyMDExNGQ3ZGRmZjY1ZGI4Nzg2MmNiNSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/IUwz373aFex6aEBdGc/giphy.gif" height="500px"/>

<h2 id="description">Description</h2>

This Python script allows you to control games, such as Pokémon, using comments from YouTube and TikTok videos. It captures the comments from both platforms and maps them to keypresses that are then used to control the game.

<h2 id="prerequisites">Prerequisites</h2>

To clone and run this application, you'll need -

* Python 3.6 or higher
* keyboard library 
  
`pip install keyboard`

* TikTokLive library 
 
`pip install TikTokLive`
* pytchat library 

`pip install pytchat`

<h2 id="important-information">Important Information</h2>

* The script uses the keyboard library to simulate keypresses. Ensure that the game you want to control is compatible with keypress inputs.

* The script utilizes the TikTokLive library to capture TikTok comments and the pytchat library to capture YouTube comments.

* Comments containing the specified key events ("up", "down", "left", "right", "a", "b") will be detected and used for game control.

<h2 id="setup">Setup</h2>

1. Clone the repository or download the script file to your local machine.
 
`git clone https://github.com/maddox05/Comment-Game-Controller.git`

2. Install the required libraries using the commands mentioned in the <a href="#prerequisites">"Prerequisites"</a> section.

<h2 id="how-to-use">How To Use</h2>

1. Run the script using the command `python game_controller.py`

2. If you want to use comments from
      * TikTok - 
        * Obtain the TikTok username that you want to use for the live comments. Enter it when prompted by the script.
    
      * YouTube - 
        * Provide the URL of the YouTube video (End ID) that you want to capture comments from. Enter it when prompted by the script.

3. The script will start capturing comments from chosen platforms.

3. Whenever a comment containing a specific key event (e.g., "up", "down", "left", "right", "a", "b") is detected, the corresponding key will be simulated as a keypress.

4. The simulated keypress will be sent to the game, allowing you to control it using the comments.

5. The script will display the name of the user and the comment for each detected key event.

**Note:** Make sure the game window is active and in focus while running the script for the keypresses to be recognized correctly.

<h2 id="contributing">Contributing</h2>

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

<h2 id="license">License</h2>

[**Apache License 2.0**](LICENSE)

<h2 id="disclaimer">Disclaimer</h2>

This script is provided as-is, without any warranty or guarantee. Use it at your own risk. The author is not responsible for any damages or consequences caused by using this script.

**Note:** Please ensure that you comply with the terms of service of YouTube and TikTok when using this script.

---

> GitHub [@maddox05](https://github.com/maddox05) 
