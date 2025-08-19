import requests  # Para consumir a API
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class JokeBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.label = Label(text="Clique no botão para ver uma piada!", font_size=20)
        self.add_widget(self.label)
        self.button = Button(text="Nova piada", size_hint=(1, 0.2), font_size=18)
        self.button.bind(on_release=self.show_joke)
        self.add_widget(self.button)

    def show_joke(self, instance):
        try:
            response = requests.get("https://official-joke-api.appspot.com/random_joke")
            joke = response.json()
            setup = joke.get('setup', '')
            punchline = joke.get('punchline', '')
            self.label.text = f"{setup}\n\n{punchline}"
        except Exception as e:
            self.label.text = "Erro ao carregar piada."

class JokeApp(App):
    def build(self):
        return JokeBox()

if __name__ == '__main__':
    JokeApp().run()