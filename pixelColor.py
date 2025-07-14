import pyautogui
import time

# Step 1: Scan for pure green
price_start_x = 834
price_end_x = 1028
price_start_y = 500
price_end_y = 530

rarity_button_x = 1087
rarity_button_start_y = 480
rarity_button_end_y = 515

prism_button_start_y = 775
prism_button_end_y = 850

green_color = (0, 255, 0)
red_color = (255, 0, 0)

buy_button_position = (866, 629)
buy_button_color = (29, 179, 29)

NON_PRISM_FRUIT_NUM = 19 # Number of fruits to check for stock
PRISM_FRUIT_NUM = 5


# cached colors of rarity buttons
# These colors are based on the game's UI design and may need to be adjusted if the game's UI changes.
common_color = (169, 169, 169)
uncommon_color = (82, 169, 97)
rare_color = (7, 118, 253)
legendary_color = (253, 253, 0)
mythical_color = (169, 84, 253)
divine_color = (253, 84, 0)

menu_color = (72, 32, 14)

found = False

def rgb_to_ansi(rgb):
    # Converts an RGB tuple to an ANSI escape code for 24-bit color
    return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"


def find_rarity_y():
    for y in range(rarity_button_start_y, rarity_button_end_y + 1):
        color = pyautogui.pixel(rarity_button_x, y)

        if color == menu_color:
            continue

        if color == common_color:
            print(f"{rgb_to_ansi(common_color)}Found Common rarity at: (Common) {rarity_button_x, y}\033[0m")
            continue

        elif color == uncommon_color:
            print(f"{rgb_to_ansi(uncommon_color)}Found Uncommon rarity at: (Uncommon) {rarity_button_x, y}\033[0m")
            continue

        elif color == rare_color:
            print(f"{rgb_to_ansi(rare_color)}Found Rare rarity at: (Rare) {rarity_button_x, y}\033[0m")
            continue

        elif color == legendary_color:
            print(f"{rgb_to_ansi(legendary_color)}Found Legendary rarity at: (Legendary) {rarity_button_x, y}\033[0m")
            return y
            break

        elif color == mythical_color:
            print(f"{rgb_to_ansi(mythical_color)}Found Mythical rarity at: (Mythical) {rarity_button_x, y}\033[0m")
            return y
            break
        
        elif color == divine_color:
            print(f"{rgb_to_ansi(divine_color)}Found Divine rarity at: (Divine) {rarity_button_x, y}\033[0m")
            return y
            break

    return None

def find_prism_rarity_y():
    for y in range(prism_button_start_y, prism_button_end_y + 1):
        color = pyautogui.pixel(rarity_button_x, y)

        if color == menu_color:
            continue

        else:
            print(f"Found Prism rarity at: {rarity_button_x, y} with color {color}")
            return y
            break
    
def check_in_stock(rarity_y):
    if rarity_y is None:
        print("No rarity button found, cannot check stock.")
        return False

    for x in range(price_start_x, price_end_x + 1):
        color = pyautogui.pixel(x, rarity_y)

        if color == green_color:
            print(f"\033[92mIn Stock at ({x}, {rarity_y})\033[0m")
            return True
            break

        if color == red_color:
            print(f"\033[91mNo Stock at ({x}, {rarity_y})\033[0m")
            return False
            break

    return False

def buy_seed():
    pyautogui.moveTo(834, 500)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(buy_button_position)
    for _ in range(3):  # Click multiple times to ensure the buy action is registered
        pyautogui.click()
        time.sleep(0.2)


def scan_fruits():
    for _ in range(NON_PRISM_FRUIT_NUM):
        if (check_in_stock(find_rarity_y())):
            buy_seed()
        else:
            print("Fruit not in stock, skipping buy.")

        time.sleep(0.5)
        pyautogui.moveTo(834, 500)
        pyautogui.scroll(-158)

def scan_prism_fruits():
    for _ in range(PRISM_FRUIT_NUM):
        prism_rarity_y = find_prism_rarity_y()
        if check_in_stock(prism_rarity_y):
            print("Prism fruit in stock, attempting to buy.")
            buy_seed()
        else:
            print("Prism fruit not in stock, skipping buy.")

        pyautogui.moveTo(834, 500)
        pyautogui.scroll(-158)
    
    

def main():
    time.sleep(3)
    buy_seed()  # Buy the seed at the current position
"""
    scan_fruits()  # Scan for non-prism fruits first

    pyautogui.scroll(222)   #scroll to be able to see prism fruits
    pyautogui.moveTo(1091, 815)

    scan_prism_fruits()  # Scan for prism fruits
    pyautogui.scroll(8000)  #Scroll back to the top
""" 



if __name__ == "__main__":
    main()


