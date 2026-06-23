from kivy.uix.screenmanager import Screen

class WinScreen(Screen):
    def restart_game(self):
        self.manager.current = 'game_screen'