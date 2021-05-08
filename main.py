def on_button_pressed_a():
    global hr
    if hr < 23:
        hr += 1
    else:
        hr = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    if min2 < 10 and hr < 10:
        basic.show_string("0" + str(hr) + ":" + "0" + str(min2))
    elif min2 < 10:
        basic.show_string("" + str(hr) + ":" + "0" + str(min2))
    elif hr < 10:
        basic.show_string("0" + str(hr) + ":" + str(min2))
    else:
        basic.show_string("" + str(hr) + ":" + str(min2))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global min2
    if min2 < 59:
        min2 += 1
    else:
        min2 = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

min2 = 0
hr = 0
hr = 0
min2 = 0

def on_forever():
    global min2, hr
    basic.pause(60000)
    if min2 < 59:
        min2 += 1
    else:
        min2 = 0
        if hr < 23:
            min2 += 1
        else:
            hr = 0
basic.forever(on_forever)

def on_forever2():
    global hr, min2
    hr = hr
    min2 = min2
    if hr == 8 and min2 == 30:
        music.start_melody(music.built_in_melody(Melodies.DADADADUM),
            MelodyOptions.FOREVER)
    if input.is_gesture(Gesture.SHAKE):
        music.stop_melody(MelodyStopOptions.FOREGROUND)
    if hr == 13 and min2 == 0:
        music.start_melody(music.built_in_melody(Melodies.DADADADUM),
            MelodyOptions.FOREVER)
    if input.is_gesture(Gesture.SHAKE):
        music.stop_melody(MelodyStopOptions.FOREGROUND)
    if hr == 18 and min2 == 30:
        music.start_melody(music.built_in_melody(Melodies.DADADADUM),
            MelodyOptions.FOREVER)
    if input.is_gesture(Gesture.SHAKE):
        music.stop_melody(MelodyStopOptions.FOREGROUND)
basic.forever(on_forever2)
