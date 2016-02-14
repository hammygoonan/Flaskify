"""Basic app file."""

from flaskify import create_app


if __name__ == "__main__":
    app = create_app('config.Test')
    app.run()
