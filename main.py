from utils.startup import initialize_app

from gui.dashboard import Dashboard

def main():

    # Initialize backend system...
    initialize_app()

    # Start GUI
    app = Dashboard()

    app.run()

if __name__ == "__main__":
    main()