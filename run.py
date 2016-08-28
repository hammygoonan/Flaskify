"""Basic app file."""

from project import create_app


if __name__ == "__main__":
    app = create_app('config.Test')
    app.run()
