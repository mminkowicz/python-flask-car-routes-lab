# Flatiron Cars - Flask Car Routes Lab

A Flask web application that serves car model information for the Flatiron Cars fleet catalog.

## Functionality

### Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Returns a welcome message |
| `/<model>` | GET | Looks up a car model in the fleet catalog |

### `/` - Default Route

Returns: `"Welcome to Flatiron Cars"`

### `/<model>` - Model Lookup Route

Accepts a car model name from the URL and checks it against the fleet catalog.

- **Model found:** `"Flatiron {model} is in our fleet!"`
- **Model not found:** `"No models called {model} exists in our catalog"`

**Available models:** Beedle, Crossroads, M2, Panique

## Screenshots

### Home Route (`/`)

![Home route](screenshots/home-route.png)

### Model Found (`/Crossroads`)

![Model found](screenshots/model-found.png)

### Model Not Found (`/Tesla`)

![Model not found](screenshots/model-not-found.png)

## Setup

1. Fork and clone this repository.
2. Install dependencies:
   ```bash
   pipenv install
   ```
3. Open a shell in the virtual environment:
   ```bash
   pipenv shell
   ```
4. Run the application:
   ```bash
   python server/app.py
   ```
5. Visit `http://127.0.0.1:5000` in your browser.

## Running Tests

```bash
pipenv run python -m pytest server/testing/app_test.py -v
```

## Tools and Resources

- [Flask Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)
