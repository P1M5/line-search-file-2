from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import *

class TextSendPortion(BoxLayout):

    def __init__(self, **kwargs):
        super(TextSendPortion, self).__init__(**kwargs)
        type = TextInput(size_hint = (0.9 , 0.1))
        send = Button(text=">", size_hint = (0.1, 0.1))
        self.add_widget(type)
        self.add_widget(send)

class ChatViewLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(ChatViewLayout, self).__init__(**kwargs)
        chat = Label(text="Chat")
        bot = TextSendPortion()
        self.add_widget(chat)
        self.add_widget(bot)

class OptionsMain(BoxLayout):

    def __init__(self, **kwargs):
        super(OptionsLayout, self).__init__(**kwargs)
        main_btn = Button()
        fold_btn = Button()
        sec_btn = Button()

class OptionsFolders(BoxLayout):

    def __init__(self, **kwargs):
        super(OptionsLayout, self).__init__(**kwargs)

class OptionsSecret(BoxLayout):

    def __init__(self, **kwargs):
        super(OptionsLayout, self).__init__(**kwargs)

class OptionsLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(OptionsLayout, self).__init__(**kwargs)


class ParentLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(ParentLayout, self).__init__(**kwargs)
        self.add_widget(ChatViewLayout(orientation="vertical"))
        self.add_widget(OptionsLayout())


class lsf2(App):

    def build(self):
        return ParentLayout()


if __name__ == "__main__":
    lsf2().run()
