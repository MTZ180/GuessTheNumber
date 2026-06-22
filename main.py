from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
import welcome_screen
import game_screen

class Main(ScreenManager):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.add_widget(welcome_screen.WelcomeScreen(name='welcome_screen'))
        self.add_widget(game_screen.GameScreen(name='game_screen'))

class GuessTheNumberApp(App):
    def build(self):
        return Main()
    
if __name__ == '__main__':
    GuessTheNumberApp().run()