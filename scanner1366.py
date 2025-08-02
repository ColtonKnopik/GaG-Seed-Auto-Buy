import pyautogui
import time
import subprocess
import restock
import trick

TOTAL_SEEDS = 24    #Change this to the total number of seeds you want to scan

#AutoHotkey script path
ahk_path = "C:\\Program Files\\AutoHotkey\\v1.1.37.02\\AutoHotkeyU64.exe"
script_path = "C:\\Users\\colto_\\Documents\\Personal Projects\\Roblox\\click.ahk"

#Colors:
green_color = (0, 255, 0)
red_color = (255, 0, 0)
common = (169, 169, 169)
uncommon = (82, 169, 97)
rare = (7, 118, 253)
legendary = (253, 253, 0)
mythical = (169, 84, 253)
divine = (253, 84, 0)
menu_color = (72, 32, 14)

rarity_x = 779
rarity_y = 588

price_low_x = 601
price_high_x = 737

buy_button_x = 558




#Function to verify the color at a specific position
def verify_color(x, y):
    color = pyautogui.pixel(x, y)

    if color == menu_color:
        return False

    time.sleep(0.1)
    newColor = pyautogui.pixel(x, y)

    #Prismatic check
    if newColor != color:
        return True
    #Colors to buy
    if color in (mythical, divine):
        return True

    #Colors to skip
    elif color in (common, uncommon, rare, legendary):
        return False

    return False

#Initializes the menu by scrolling to the top and moving to the initial position
def init_menu():
    time.sleep(1)
    pyautogui.scroll(8000)
    pyautogui.scroll(-82)
    pyautogui.moveTo(rarity_x, rarity_y)

#Scan bottom right corner for rarities
def scan_position(x, y, iterations):
    for _ in range(iterations):        
        if (color := verify_color(x, y) != False):
            print(f"Verified color at ({x}, {y})")
            if(check_in_stock(y)):
                buy_seed(x, y)
                return True

        pyautogui.scroll(-137)
        time.sleep(trick.getRandDelay(0.5, 1))

    return False

#Scans left to right to find price, returns true if it sees green, returns flase if it sees red
def check_in_stock(y):
    if y is None:
        print("No rarity button found, cannot check stock.")
        return False

    for x in range(price_low_x, price_high_x):
        color = pyautogui.pixel(x, y)

        if color == green_color:
            print(f"\033[92mIn Stock at ({x}, {y})\033[0m")
            return True
            break

        if color == red_color:
            print(f"\033[91mNo Stock at ({x}, {y})\033[0m")
            return False
            break

    return False


def buy_seed(x, y):
    subprocess.run([ahk_path, script_path]) #Click
    if (buy_y := find_buy_button_y()) is not None:
        pyautogui.moveTo(buy_button_x, buy_y)
        subprocess.run([ahk_path, script_path]) #Click
        time.sleep(0.5)
        close_seed(buy_button_x, buy_y)
    

def close_seed(buy_x, buy_y):
    pyautogui.moveTo(buy_x, buy_y - 150)
    subprocess.run([ahk_path, script_path]) #Click
    print("Closing seed menu...")

                
def find_buy_button_y():
    buy_button_low_y = 435
    buy_button_high_y = 612

    for y in range(buy_button_low_y, buy_button_high_y + 1):
        pyautogui.moveTo(buy_button_x, y)
        color = pyautogui.pixel(buy_button_x, y)
        if color == menu_color:
            continue

        if color in ((29, 179, 29), (1, 91, 1), (255, 255, 255), (38, 238, 38)):
            print(f"Buy button found at ({buy_button_x}, {y})")
            pyautogui.moveTo(buy_button_x, y)
            return y
    
    print("No buy button found in the specified range.")
    return None


def scan_loop():
    while True:
        init_menu()
        result = scan_position(rarity_x, rarity_y, TOTAL_SEEDS - 2)
        if result:
            continue  # Found and bought, repeat process
        else:
            print("No valid item found, exiting.")
            init_menu()
            return


def main():
    while True:
        if(restock.restock_listener()):
            scan_loop()

if __name__ == "__main__":
    main()
