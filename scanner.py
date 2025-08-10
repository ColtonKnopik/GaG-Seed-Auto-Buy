import pyautogui
import time
import subprocess
import restock
import trick

TOTAL_SEEDS = 24    #Change this to the total number of seeds you want to scan
chosen_rarities = []

#AutoHotkey script path
ahk_path = "C:\\Program Files\\AutoHotkey\\v1.1.37.02\\AutoHotkeyU64.exe"
script_path = "click.ahk"

RARITY_COLORS = {
    "Common": (169, 169, 169),
    "Uncommon": (82, 169, 97),
    "Rare": (7, 118, 253),
    "Legendary": (253, 253, 0),
    "Mythical": (169, 84, 253),
    "Divine": (253, 84, 0),
    "Prismatic": None  # Prismatic handled differently
}
green_color = (0, 255, 0)
red_color = (255, 0, 0)
menu_color = (72, 32, 14)

# All coordinates grouped by resolution
COORDINATES = {
    "1366x768": {
        "rarity_x": 779,
        "rarity_y": 588,
        "price_low_x": 601,
        "price_high_x": 737,
        "buy_button_x": 558,
        "menu_scroll_down_init": -82,
        "menu_scroll_down": -137,
        "buy_button_low_y": 435,
        "buy_button_high_y": 612
    },
    "1920x1080": {
        "rarity_x": 1098,  
        "rarity_y": 842,
        "price_low_x": 842,
        "price_high_x": 978,
        "buy_button_x": 790,
        "menu_scroll_down_init": -88,
        "menu_scroll_down": -158,
        "buy_button_low_y": 650,
        "buy_button_high_y": 867
    }
}

#Function to verify the color at a specific position
def verify_color(x, y):
    global chosen_rarities
    color = pyautogui.pixel(x, y)

    if color == menu_color:
        return False

    time.sleep(0.1)
    newColor = pyautogui.pixel(x, y)

    # Special Prismatic check
    if "Prismatic" in chosen_rarities and newColor != color:
        return True

    # Check if pixel matches any chosen rarity's color
    for rarity in chosen_rarities:
        if RARITY_COLORS[rarity] == color:
            return True  # Buy
    return False


#Initializes the menu by scrolling to the top and moving to the initial position
def init_menu():
    time.sleep(1)
    pyautogui.scroll(8000)
    pyautogui.scroll(menu_scroll_down_init)
    pyautogui.moveTo(rarity_x, rarity_y)

#Scan bottom right corner for rarities
def scan_position(x, y, iterations):
    for _ in range(iterations):        
        if (color := verify_color(x, y) != False):
            print(f"Verified color at ({x}, {y})")
            if(check_in_stock(y)):
                buy_seed(x, y)
                return True

        pyautogui.scroll(menu_scroll_down)
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

def get_resolution():
    while True:
        print("Choose Resolution:\n")
        print("1. 1920 x 1080")
        print("2. 1366 x 768")
        choice = input(">> ").strip()
        if choice == "1":
            return "1920x1080"
        elif choice == "2":
            return "1366x768"
        else:
            print("Invalid choice, try again.")

def get_target_rarities():
    global chosen_rarities
    rarities = [
        "Prismatic",
        "Divine",
        "Mythical",
        "Legendary",
        "Rare",
        "Uncommon",
        "Common"
    ]
    chosen_rarities.clear()  

    while True:
        print("1. Prismatic\n2. Divine\n3. Mythical\n4. Legendary\n5. Rare\n6. Uncommon\n7. Common")
        print("Type and enter the name or number of a rarity to add to purchase list ('d' or 'done' to exit)")

        selection = input(">> ").strip()

        if selection.lower() in ("d", "done"):
            break

        if selection.isdigit():
            index = int(selection) - 1
            if 0 <= index < len(rarities):
                rarity = rarities[index]
            else:
                print("Invalid number. Please try again.")
                continue
        else:
            matches = [r for r in rarities if r.lower() == selection.lower()]
            if matches:
                rarity = matches[0]
            else:
                print("Invalid rarity name. Please try again.")
                continue

        if rarity not in chosen_rarities:
            chosen_rarities.append(rarity)
            print(f"Added: {rarity}")
        else:
            print(f"{rarity} is already in your purchase list.")

def main():
    res = get_resolution()
    globals().update(COORDINATES[res])

    get_target_rarities()
    print(rarity_x, rarity_y, price_low_x, price_high_x, buy_button_x)

    scan_loop()
    while True:
        if(restock.restock_listener(res)):
            scan_loop()

if __name__ == "__main__":
    main()
