SetDefaultMouseSpeed, 0

; Move 5 pixels to the left (relative)
MouseMove, -5, 0, 0, R
Sleep, 250

Loop, 3 {
    DllCall("mouse_event", "UInt", 0x02, "UInt", 0, "UInt", 0, "UInt", 0, "UPtr", 0) ; Mouse down
    Sleep, 500
    DllCall("mouse_event", "UInt", 0x04, "UInt", 0, "UInt", 0, "UInt", 0, "UPtr", 0) ; Mouse up
    Sleep, 150
}
