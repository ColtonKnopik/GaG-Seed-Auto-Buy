import pyautogui
import time
import subprocess

ahk_path = "C:\\Program Files\\AutoHotkey\\v1.1.37.02\\AutoHotkeyU64.exe"
script_path = "C:\\Users\\colto_\\Documents\\Personal Projects\\Roblox\\buy_seed.ahk"

rarity_button_x = 1087
rarity_button_start_y = 480
rarity_button_end_y = 515
menu_color = (72, 32, 14)
common_color = (169, 169, 169)
uncommon_color = (82, 169, 97)
rare_color = (7, 118, 253)
legendary_color = (253, 253, 0)
mythical_color = (169, 84, 253)
divine_color = (253, 84, 0)

buy_button_position = (866, 629)


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
            return y

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
    time.sleep(.01)
    find_buy_button_position()
    subprocess.run([ahk_path, script_path])
    pyautogui.moveTo(834, 500)
    pyautogui.click()


def find_buy_button_position():
    buy_button_x = 676
    buy_button_y = find_rarity_y() + 100

    print(f"Moving to buy button at: ({buy_button_x}, {buy_button_y})")
    pyautogui.moveTo(buy_button_x, buy_button_y)

def main():
    time.sleep(3)
    buy_seed() 

if __name__ == "__main__":
    main()

