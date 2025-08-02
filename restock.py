import pyautogui
import time
import trick

#Restock popup position and color
restock_positions = [
    (520, 202),
    (520, 224)
]
restock_colors = [
    (158, 197, 210),
    (171, 213, 227),
    (144, 238, 144)
]

null_colors = [
    (84, 172, 59),
    (17, 85, 12)
]

def check_restock_pos(restock_pos):
    color = pyautogui.pixel(*restock_pos)

    if color in restock_colors:
        return True
    
    else:
        return False


def restock_listener():
    print("Listening for restock...")
    time.sleep(2)
    while True:
        trick.randomMouseMove()
        time.sleep(trick.getRandDelay(2,3))


        for restock_pos in restock_positions:
            if check_restock_pos(restock_pos):
                print(f"Restock detected at {restock_pos}!")
                return True
        

