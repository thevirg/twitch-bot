from parky_bot.settings import BOT
from parky_bot.models.message import Message
from time import sleep


# @BOT.decorator(['!game'])
# def command_updategame(message: Message):
#     prefix = len(message.command) + 1
#     if not message.message[prefix:]:
#         return BOT.send_message(f'Currently playing: "{BOT.twitch.game}"')
#
#     if 'broadcaster' in message.badges:
#         result = BOT.twitch.update_stream(game_title=message.message[prefix:])
#         if result:
#             BOT.send_message(f'Game set to: "{BOT.twitch.game}"')
#         else:
#             BOT.send_message(f'Twitch API failed to update game!')
#
#
# @BOT.decorator(['!status', '!title'])
# def command_updatestatus(message: Message):
#     prefix = len(message.command) + 1
#     if not message.message[prefix:]:
#         return BOT.send_message(f'Status: "{BOT.twitch.status}"')
#
#     if 'broadcaster' in message.badges:
#         result = BOT.twitch.update_stream(
#             stream_title=message.message[prefix:])
#         if result:
#             BOT.send_message(f'Title set to: "{BOT.twitch.status}"')
#         else:
#             BOT.send_message(f'Twitch API failed to update status!')
#
#
@BOT.decorator(['!raffle', '!raffle :whites69Awk:', '!sraffle'])
def command_uptime(message: Message):
    sleep(5)
    BOT.send_message(f'!join')
