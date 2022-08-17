from pynput import keyboard

kc = keyboard.Controller()

keys = "1234567890qwertyuiopasdfghjkl;zxcvbnm,./"

def movepiece(moveright, rotate):
    for i in range(rotate):
        kc.press(keyboard.Key.up)
        kc.release(keyboard.Key.up)

    for i in range(10):
        kc.press(keyboard.Key.left)
        kc.release(keyboard.Key.left)

    for i in range(moveright):
        kc.press(keyboard.Key.right)
        kc.release(keyboard.Key.right)


def on_press(key):
    try:
        if(key.char in keys):
            moveright = keys.index(key.char) % 10
            rotate = keys.index(key.char) // 10
            movepiece(moveright, rotate)
    except AttributeError:
        pass


with keyboard.Listener(
        on_press=on_press,) as listener:
    listener.join()
 
