import socket
from threading import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from plyer import accelerometer

class Application(App):
    def build(self):
        global label

        boxLayout = BoxLayout()

        label = Label(text="Ok", font_size=30)
        
        boxLayout.add_widget(label)

        return boxLayout

def Socket():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.0.105", 7777))

    while True:
        #y = accelerometer.acceleration[1]
        client.send(str("ok").encode("utf-8"))

if __name__ == "__main__":
    socketTread = Thread(target=Socket)
    socketTread.start()

    Application().run()