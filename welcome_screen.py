from kivy.uix.screenmanager import Screen

class WelcomeScreen(Screen):
    def start_game(self):
        self.manager.current = 'game_screen'