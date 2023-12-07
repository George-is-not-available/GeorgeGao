function config() {
    let canvas = document.querySelector('.runner-canvas')
    let context = canvas.getContext('2d')
    let checkPoint = {
        x: canvas.width * 0.2,
        y: canvas.height * 0.75,
    }
    return {
        canvas,
        context,
        checkPoint,
    }
}

function pixelData(checkPoint) {
    let data = config().context.getImageData(checkPoint.x, checkPoint.y, 1, 1)
    return {
        r: data.data[0],
        g: data.data[1],
        b: data.data[2],
    }
}

function isObstruction(pixelData) {
    let {r, g, b} = pixelData
    if (r === 83 && g === 83 && b === 83) {
        return true
    } else {
        return false
    }
}

function isObstructionComing() {
    let point = config().checkPoint
    let data = pixelData(point)
    let check = isObstruction(data)
    return check
}

function keyEvent(type, keyCode) {
    let event = document.createEvent('Events')
    event.initEvent(type, true, true)
    event.keyCode = keyCode
    event.which = keyCode
    document.dispatchEvent(event)
}

function jump() {
    keyEvent('keydown', 32)
}

function check() {
    if (isObstructionComing()) {
        jump()
    }
}

function __main() {
    setInterval(check, 1)
}
__main()