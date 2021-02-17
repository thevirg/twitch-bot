import time
from parky_bot.models.message import Message
from parky_bot.utils.logger import get_logger


class ParkyBot:
    def __init__(self, twitch=None, irc=None):
        self.twitch = twitch
        self.irc = irc
        self.handlers = []
        self.chatters = []
        self.is_pooling = True
        self._logger = get_logger()

    def pooling(self):
        if not self.irc:
            self._logger.info("IRC client not set, not pooling!")
            return

        data = ""
        self.irc.irc_sock.setblocking(0)
        self._logger.info("Now pooling...")

        while self.is_pooling:
            try:
                data = self.irc.irc_sock.recv(4096).decode('UTF-8')
            except (ConnectionAbortedError, OSError):
                try:
                    time.sleep(0.1)
                except KeyboardInterrupt:
                    self.is_pooling = False
                    break
                continue
            except KeyboardInterrupt:
                self.is_pooling = False
                break

            if data == "":
                self._logger.critical("IRC client received 0 bytes, stopping...")
                self.is_pooling = False
                break

            if data == "PING :tmi.twitch.tv\r\n":
                self.irc.send_pong()
                self._logger.debug('PONG')

            else:
                # BUG: If the sender decides to send '\n' midstring, their message will be split.
                for line in data.splitlines():
                    m = Message(line)
                    if m.sender:
                        self._logger.info(f'{m.sender}: {m.message}')
                    else:
                        self._logger.debug(m.string)

                    if m.sender not in self.chatters and m.sender:
                        self.chatters.append(m.sender)

                    self._filter(m)

            data = ""
        self._logger.info('Stopped pooling.')

    def _filter(self, message: Message):
        """This method filters through the handlers, and calls its respective function.

        Args:
            message (Message): Message object.
        """
        for decorator in self.handlers:
            if (message.command in decorator['commands'] and decorator['active']
            and self.has_permission(decorator['access'], message)):
                decorator['function'](message)

    def has_permission(self, func_perm_level: int, message: Message) -> bool:
        """
        Checks permission based on hierarchy level

        0 - Viewer
        1 - Vip
        2 - Moderator
        3 - Broadcaster
        """
        if not func_perm_level:
            return True

        perms = {
            'broadcaster': 3,
            'moderator': 2,
            'vip': 1,
            '': 0
        }

        # Finding out the numerical equivalent for the permission
        user_perm = 0
        for perm in perms:
            if perm in message.badges:
                user_perm = perms[perm]
                break
        print('user_perm:', user_perm, perm, 'func_perm:', func_perm_level)

        return user_perm >= func_perm_level

    def decorator(self, commands=[], regexp='', access=0):
        def wrapper(function):
            self._logger.debug(f'Decorating: {function.__name__}')

            func = {
                'active': True,
                'function': function,
                'commands': commands,
                'regexp': regexp,
                'access': access
                }

            self.handlers.append(func)
            return function
        return wrapper

    def send_message(self, string):
        self.irc.send_message(string)
