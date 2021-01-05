import kivy

from kivy.app import App
from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Loads kv config files
Builder.load_file('Login.kv')
Config.set('graphics', 'fullscreen', '0')

# Creates an object to manage multiple kv screens
sm = ScreenManager()

# Adding custom fonts
LabelBase.register(name='BlackJack', fn_regular='blackjack.otf')


class LoginScreen(Screen):
    pass


# Adds screens to the screen manager
sm.add_widget(LoginScreen(name='login'))


class LivingFree(App):
    def build(self):
        return sm


if __name__ == '__main__':
    LivingFree().run()
