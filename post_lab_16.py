# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.boxlayout import BoxLayout

# class CounterApp(App):
#     def build(self):
#         self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)
#         self.counter = 0
#         self.label = Label(text=f"Counter: {self.counter}", font_size=32)
#         self.layout.add_widget(self.label)
#         self.button = Button(text="Click Me!", font_size=24)
#         self.button.bind(on_press=self.increment_counter)
#         self.layout.add_widget(self.button)

#         return self.layout

#     def increment_counter(self, instance):
#         self.counter += 1
#         self.label.text = f"Counter: {self.counter}"

# if __name__ == "__main__":
#     CounterApp().run()

#Question 2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        # Layout
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Text input field
        self.text_input = TextInput(hint_text="Type something here...", multiline=False, font_size=20)
        layout.add_widget(self.text_input)

        # Button
        button = Button(text="Show Text", font_size=20)
        button.bind(on_press=self.show_text)
        layout.add_widget(button)

        # Label to display text
        self.label = Label(text="Your text will appear here", font_size=24)
        layout.add_widget(self.label)

        return layout

    def show_text(self, instance):
        # Update label with text from input
        self.label.text = f"You typed: {self.text_input.text}"

if __name__ == "__main__":
    TextInputApp().run()

