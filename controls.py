from pynput.keyboard import Key, Controller

keyboard = Controller()

# State tracking variables
current_key = None
space_pressed = False

def _release_space():
    """Helper to release spacebar if pressed"""
    global space_pressed
    if space_pressed:
        keyboard.release(Key.space)
        space_pressed = False

def _release_current_key():
    """Helper to release current movement key"""
    global current_key
    if current_key is not None:
        keyboard.release(current_key)
        current_key = None

def do_nothing():
    global current_key, space_pressed
    _release_space()
    _release_current_key()

def move_left():
    global current_key, space_pressed
    _release_space()
    if current_key != 'a':          # only switch if not already moving left
        _release_current_key()
        current_key = 'a'
        keyboard.press(current_key)  # single press instead of 100x loop

def move_right():
    global current_key, space_pressed
    _release_space()
    if current_key != 'd':          # only switch if not already moving right
        _release_current_key()
        current_key = 'd'
        keyboard.press(current_key)  # single press instead of 100x loop

def jump():
    global current_key, space_pressed
    _release_current_key()
    if not space_pressed:           # only press if not already jumping
        keyboard.press(Key.space)
        space_pressed = True