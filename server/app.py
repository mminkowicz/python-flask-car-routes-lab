# Flask Car Routes Application
# Serves car model information for the Flatiron Cars fleet catalog.

from flask import Flask

app = Flask(__name__)

# Available car models in the Flatiron fleet
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route('/')
def index():
    """Default route welcoming visitors to Flatiron Cars."""
    return 'Welcome to Flatiron Cars'


@app.route('/<model>')
def get_model(model):
    """Look up a car model and return whether it exists in the fleet."""
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    return f'No models called {model} exists in our catalog'


if __name__ == '__main__':
    app.run(debug=True)
