from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
import random

class GameScreen(Screen):
    feedback = StringProperty("")
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.feedback = ""

    def check_guess(self, guess):
        self.attempts += 1
        if guess < self.target_number:
            self.feedback = f"{guess} is too low! Try again."
        elif guess > self.target_number:
            self.feedback = f"{guess} is too high! Try again."
        elif guess == self.target_number:
            self.manager.current = 'win_screen'
        else:
            self.feedback = "Invalid input. Please enter a number between 1 and 100."