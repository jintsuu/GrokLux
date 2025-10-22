import os

from Bot.app import App

if __name__ == '__main__':
    app = App()
    app.run(token=os.environ['TOKEN'])