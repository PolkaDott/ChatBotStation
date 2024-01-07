from examples.bot_with_tasks.controllers.basic_controller import (
    BasicController,
)
from examples.bot_with_tasks.views.basic_view import SimpleView
from swiftbots import initialize_app


def main():
    app = initialize_app()

    app.add_bot(SimpleView, [BasicController])

    app.run()


if __name__ == '__main__':
    main()
