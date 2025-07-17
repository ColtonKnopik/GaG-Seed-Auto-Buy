SetDefaultMouseSpeed, 0

; Move 1 pixel to the left (relative)
MouseMove, -1, 0, 0, R
Sleep, 250
MouseMove, 1, 0, 0, R
Sleep, 250

DllCall("mouse_event", "UInt", 0x02, "UInt", 0, "UInt", 0, "UInt", 0, "UPtr", 0) ; Mouse down
Sleep, 500
DllCall("mouse_event", "UInt", 0x04, "UInt", 0, "UInt", 0, "UInt", 0, "UPtr", 0) ; Mouse up
Sleep, 150