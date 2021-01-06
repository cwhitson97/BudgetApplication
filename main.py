import kivy

from kivy.app import App
from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Loads config files
Builder.load_file('Login.kv')
Builder.load_file('menu.kv')
Config.set('graphics', 'fullscreen', '0')

# Creates an object to manage multiple kv screens
sm = ScreenManager()

# Adding custom fonts
LabelBase.register(name='BlackJack', fn_regular='blackjack.otf')


class LoginScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


# Adds screens to the screen manager
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MenuScreen(name='menu'))


class LivingFree(App):
    def build(self):
        return sm


if __name__ == '__main__':
    LivingFree().run()
