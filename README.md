# YouTube and TikTok Comment Game Controller
This Python script allows you to control games, such as Pokemon, using comments from YouTube and TikTok videos. It captures the comments from both platforms and maps them to keypresses that are then used to control the game.
<br><img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGU3OGJlMzdiODk5MTU3NDUyMDExNGQ3ZGRmZjY1ZGI4Nzg2MmNiNSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/IUwz373aFex6aEBdGc/giphy.gif" height="500px"/>

## Prerequisites
* Python 3.6 or higher
* keyboard library (install using pip install keyboard)
* TikTokLive library (install using pip install TikTokLive)
* pytchat library (install using pip install pytchat)
## Setup
1. Clone the repository or download the script file to your local machine.
2. Install the required libraries using the commands mentioned in the "Prerequisites" section.
3. Obtain the TikTok username that you want to use for the live comments. Enter it when prompted by the script.
4. Provide the URL of the YouTube video (end id) that you want to capture comments from. Enter it when prompted by the script.
## Usage
1. Run the script using the command python game_controller.py.
2. The script will start capturing comments from both TikTok and YouTube platforms.
3. Whenever a comment containing a specific key event (e.g., "up", "down", "left", "right", "a", "b") is detected, the corresponding key will be simulated as a keypress.
4. The simulated keypress will be sent to the game, allowing you to control it using the comments.
5. The script will display the name of the user and the comment for each detected key event.

**Note:** Make sure the game window is active and in focus while running the script for the keypresses to be recognized correctly.

## Important Information
* The script uses the keyboard library to simulate keypresses. Ensure that the game you want to control is compatible with keypress inputs.
* The script utilizes the TikTokLive library to capture TikTok comments and the pytchat library to capture YouTube comments.
* Comments containing the specified key events ("up", "down", "left", "right", "a", "b") will be detected and used for game control.
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[**Apache License 2.0**](LICENSE)

## Disclaimer
This script is provided as-is, without any warranty or guarantee. Use it at your own risk. The author is not responsible for any damages or consequences caused by using this script.

**Note:** Please ensure that you comply with the terms of service of YouTube and TikTok when using this script.

