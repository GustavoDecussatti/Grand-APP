from kivy.app import App
from kivy.uix.widget import Widget



class game(Widget):
    pass

class GameApp(App):
    def build(self):
        return game()




if __name__ == '__main__':
    GameApp().run()