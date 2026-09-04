__version__ = "1.0.0"
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        layout.add_widget(
            Label(
                text="My name is Hama\nI am 25 years old",
                font_size=24
            )
        )

        layout.add_widget(
            Label(
                text="What is your name?",
                font_size=18
            )
        )

        self.name = TextInput(
            hint_text="Enter your name",
            multiline=False,
            font_size=18
        )
        layout.add_widget(self.name)

        layout.add_widget(
            Label(
                text="How old are you?",
                font_size=18
            )
        )

        self.age = TextInput(
            hint_text="Enter your age",
            multiline=False,
            input_filter="int",
            font_size=18
        )
        layout.add_widget(self.age)

        button = Button(
            text="Continue",
            font_size=20
        )
        button.bind(on_press=self.show_result)
        layout.add_widget(button)

        self.result = Label(
            text="",
            font_size=20
        )
        layout.add_widget(self.result)

        return layout

    def show_result(self, instance):
        name = self.name.text
        age = self.age.text

        if name and age:
            self.result.text = (
                f"Nice to meet you {name}!\n"
                f"I am {age} years old too."
            )


MyApp().run()
