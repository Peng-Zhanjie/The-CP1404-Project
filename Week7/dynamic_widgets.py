from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
Subject=["English","Math","Science","Geography","Information technology"]

class Dynamic(App):
    def build(self):
        self.title = "Dynamic"
        self.root = Builder.load_file('dynamic_widgets.kv')
        return self.root
    def create_widgets(self):
        for i in Subject:
            temp_label = Label(text=i)
            self.root.ids.entries_box.add_widget(temp_label)
    def clear_widgets(self):
            self.root.ids.entries_box.clear_widgets()


Dynamic().run()