# Grow a Garden Auto Buy

python script to scan shop menu on the popular Roblox game grow a garden. Listens for shop restock message and triggers a scan of the entire menu, buying seeds of rarity legendary or higher.

## Required Installs

 [Python 3.12.3](https://www.python.org/downloads/release/python-3123/) (or whatever the latest is)
 * Open terminal
 * Enter: `pip install pyautogui`
 * Enter: `pip install Pillow`

[AutoHotKey](https://www.autohotkey.com/download/) required to send OS level mouse output 

## Downloading code
* Click green `Code` Button and download `.Zip`
* Exctract zip file to location you want
* open folder
* right click and open in terminal
* run `python3 scanner.py`

## Configuration
Inside of `scanner.py` verify that `ahk_path` is pointing the source file you downloaded from AutoHotKey

## Usage

* Open Roblox Player
* Run `scanner.py`
* Choose the correct display resultion for your machine. `Display Settings > Display Resolution`
* Choose the fruits you want to buy based on rarity
* type 'done'
* Quickly switch window to Roblox Player in **Full Screen** windowed mode
* Position mouse over seed menu as seen here:


<img width="1919" height="1079" alt="Screenshot 2025-08-09 172205" src="https://github.com/user-attachments/assets/debcf91a-dd04-4300-a228-c450e4de7c07" />
