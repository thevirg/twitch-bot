import os
from audioplayer import AudioPlayer
from parky_bot.utils.file_manager import make_dir
from parky_bot.settings import BOT, SOUNDS_PATH, SETTINGS
from parky_bot.models.message import Message
from parky_bot.utils.logger import get_logger


LOGGER = get_logger()
SOUNDS = []


def scan_sounds_dir():
    sounds = []
    if os.path.isdir(SOUNDS_PATH):
        for file in os.listdir(SOUNDS_PATH):
            if file.endswith(('.wav', '.mp3')):
                sounds.append(file)
    else:
        make_dir(SOUNDS_PATH)
        LOGGER.debug('Created "%s" dir', SOUNDS_PATH)
    return sounds

def create_sounds(sounds: list):
    for sound in sounds:
        # NOTE: It's not possible to decorate a lambda function with arguments, so this approach is used.
        # Sound object is initialized when assigned to 's', avoiding parent variable search.
        # Don't -> lambda m: Class.method()
        # Do -> lambda m, o=Class(): o.method()
        #pylint: disable=cell-var-from-loop
        func = {'active': True,
                'function': lambda _, s=AudioPlayer(os.path.join(SOUNDS_PATH, sound)): play_sound(s),
                'commands': [f'!{sound[:-4].lower()}'],
                'regexp': '',
                'access': 0}
        BOT.handlers.append(func)
        LOGGER.debug('Sound: %s created.', func['commands'][0])

@BOT.decorator(['!sounds'])
def command_replysounds(message: Message):
    message = ''

    for sound in sorted(SOUNDS):
        message += f'!{sound[:-4].lower()}, '
    message = message[:-2] + ' KappaKappa'
    BOT.send_message(message)

def play_sound(sound: AudioPlayer) -> None:
    try:
        sound.volume = SETTINGS.get('volume', 100)
        sound.play()
    except Exception as err:
        LOGGER.error(err, exc_info=True)

SOUNDS = scan_sounds_dir()
create_sounds(SOUNDS)
