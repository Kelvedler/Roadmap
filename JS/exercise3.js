function sleepIn(weekday, vacation){
    if (weekday === false || vacation === true){
        return true
    } else{
        return false
    }
}

function monkeyTrouble(aSmile, bSmile){
    if (aSmile === bSmile){
        return true
    } else{
        return false
    }
}

function stringTimes(str, times = 1){
    var count = 0
    var strAdd = ""
    while (count < times){
        strAdd = strAdd + str
        count += 1
    }
    return strAdd
}

function luckySum(a, b, c){
    sum = 0
    if (a !== 13){
        sum = a
        if (b !== 13){
            sum = a + b
            if (c !== 13){
                sum = a + b + c
                return sum
            } else return sum
        } else return sum
    } else return sum
}

function caughtSpeeding (speed, birthday){
    if (birthday === true){
        speed = speed - 5
    }
    if (speed <= 60){
        return 0
    } else if (speed > 60 && speed <= 80){
        return 1
    } else if (speed > 80){
        return 2
    }
}

function makeBricks(small, big, goal){
    var bricks = 0
    for (var i = 0; i < big; i += 1){
        if (goal - bricks >= 5){
            bricks += 5
        }
    }
    for (var i = 0; i < small; i += 1){
        if (bricks < goal){
            bricks += 1
        }
    }
    if (goal === bricks){
        return true
    } else return false
}