input.onButtonPressed(Button.A, function () {
    if (hr < 23) {
        hr += 1
    } else {
        hr = 0
    }
})
input.onButtonPressed(Button.AB, function () {
    if (min2 < 10 && hr < 10) {
        basic.showString("0" + ("" + hr) + ":" + "0" + ("" + min2))
    } else if (min2 < 10) {
        basic.showString("" + hr + ":" + "0" + ("" + min2))
    } else if (hr < 10) {
        basic.showString("0" + ("" + hr) + ":" + ("" + min2))
    } else {
        basic.showString("" + hr + ":" + ("" + min2))
    }
})
input.onButtonPressed(Button.B, function () {
    if (min2 < 59) {
        min2 += 1
    } else {
        min2 = 0
    }
})
let min2 = 0
let hr = 0
hr = 0
min2 = 0
basic.forever(function () {
    hr = hr
    min2 = min2
    if (hr == 8 && min2 == 30) {
        music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Forever)
    }
    if (input.isGesture(Gesture.Shake)) {
        music.stopMelody(MelodyStopOptions.Foreground)
    }
    if (hr == 13 && min2 == 0) {
        music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Forever)
    }
    if (input.isGesture(Gesture.Shake)) {
        music.stopMelody(MelodyStopOptions.Foreground)
    }
    if (hr == 18 && min2 == 30) {
        music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Forever)
    }
    if (input.isGesture(Gesture.Shake)) {
        music.stopMelody(MelodyStopOptions.Foreground)
    }
})
basic.forever(function () {
    basic.pause(60000)
    if (min2 < 59) {
        min2 += 1
    } else {
        min2 = 0
        if (hr < 23) {
            min2 += 1
        } else {
            hr = 0
        }
    }
})
