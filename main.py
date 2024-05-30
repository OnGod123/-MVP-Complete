from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
import requests

class ImageButton(ButtonBehavior, Image):
    pass

class ApplianceBox(BoxLayout):
    def __init__(self, appliance_type, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.appliance_type = appliance_type
        self.state = False
        self.icon = ImageButton(source=f'icons/{appliance_type}.png')
        self.icon.bind(on_press=self.fetch_and_toggle_state)
        self.state_label = Label(text='Off')
        self.add_widget(self.icon)
        self.add_widget(self.state_label)

    def fetch_and_toggle_state(self, instance):
        try:
            response = requests.get(f'http://127.0.0.1:5000/{self.appliance_type}')
            response_data = response.json()
            self.state = response_data['state']
            self.state_label.text = 'On' if self.state else 'Off'
            self.toggle_state(instance)
        except Exception as e:
            self.state_label.text = f'Error: {e}'

    def toggle_state(self, instance):
        new_state = not self.state
        try:
            response = requests.post(f'http://127.0.0.1:5000/{self.appliance_type}', json={'state': new_state})
            if response.status_code == 200:
                self.state = new_state
                self.state_label.text = 'On' if self.state else 'Off'
            else:
                self.state_label.text = 'Error'
        except Exception as e:
            self.state_label.text = f'Error: {e}'

class ApplianceControlApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        appliances = ['television', 'microwave', 'pumping_machine', 'light_bulb', 'electric_cooker']
        for appliance in appliances:
            box = ApplianceBox(appliance_type=appliance)
            button = Button(text=appliance.replace('_', ' ').capitalize())
            button.bind(on_press=box.fetch_and_toggle_state)
            layout.add_widget(box)
            layout.add_widget(button)
        return layout

if __name__ == '__main__':
    ApplianceControlApp().run()

