import pyautogui
import time
import trick

#Restock popup position and color
RESTOCK_POSITIONS = {
    "1366x768": [
        (520, 202),
        (520, 224)
    ],
    "1920x1080": [
        (741, 274),  # example values, replace with actual coords
        (742, 308)
    ]
}
restock_colors = [
    (158, 197, 210),
    (171, 213, 227),
    (173, 216, 230),
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


def restock_listener(res):
    print("Listening for restock...")
    time.sleep(2)

    # Get correct positions for resolution
    restock_positions = RESTOCK_POSITIONS[res]
    print(f"Resolution: {res}")
    pyautogui.moveTo(restock_positions[1])

    while True:
        trick.randomMouseMove()
        time.sleep(trick.getRandDelay(2, 3))

        for restock_pos in restock_positions:
            if check_restock_pos(restock_pos):
                print(f"Restock detected at {restock_pos}!")
                return True

