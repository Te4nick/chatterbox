import tkinter
from rich import print
from rich.panel import Panel
from rich.console import Group
from rich.layout import Layout
import os


class Window:
    origin_width = os.get_terminal_size().columns
    origin_height = os.get_terminal_size().lines
    height = 0
    width = 0

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def close(self):
        self.clear()
        os.system(f"mode con: cols={self.origin_width} lines={self.origin_height}")

    def create(self, width: int, height: int):
        self.width, self.height = width, height
        self.clear()
        os.system(f"mode con: cols={self.width} lines={self.height}")


class UILayout:
    chats = True
    messages = False
    profile = False
    user_in = False
    emoji = False
    positions = [chats, messages, messages,
                 profile, user_in, emoji]

    layout = Panel("Layout", width=120, height=30)

    def setPanel(self, layout: Layout):
        self.layout = Panel(layout, title="chatterbox", subtitle="[bold red]Alpha v.0.0.1[/]", width=120, height=30)

    def mainView(self):
        layout = Layout(size=20)
        layout.split_row(Layout(name='left', size=30), Layout(name='right'))
        layout["left"].split(
            Layout(Panel("Chats list here", title="Chats"), name="leftTop"),
            Layout(Panel("Username\nstatus\ntime?", title="Profile"), name="leftBottom", size=10)
        )
        layout["right"].split(
            Layout(Panel("Messages here"), name="rightTop"),
            Layout(name="rightBottom", size=5)
        )
        layout["rightBottom"].split_row(
            Layout(Panel("Messages here", title="Message"), name="rightBottomLeft"),
            Layout(Panel(")))", title="Emoji"), name="rightBottomRight", size=10),
        )
        self.setPanel(layout)
        return self.layout


window = Window()
window.create(120, 31)
layout = UILayout()
print(layout.mainView())
input("Enter any key to continue...")
window.close()
