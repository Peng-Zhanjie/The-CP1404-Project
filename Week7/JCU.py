from kivy.app import App
from kivy.lang import Builder

class JCUApp(App):
    def build(self):
        self.title = "JCU"
        self.root = Builder.load_file('JCU.kv')
        return self.root

    def handle_jugment(self):
        value = self.get_validated_miles()
        if value<60 and value>=0: result="Fail"
        elif value>=60 and value<65:result="Pass"
        elif value>=65 and value<75: result="Good"
        elif value>=75 and value<=100: result="Satisfy"
        else: result="Invalid number"
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_jugment()

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

JCUApp().run()