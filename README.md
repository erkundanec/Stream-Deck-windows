
# Stream Deck
[![CI](https://github.com/manish-jsx/stream-deck/actions/workflows/python-app.yml/badge.svg)](https://github.com/manish-jsx/stream-deck/actions/workflows/python-app.yml)

Create your own customizable Stream Deck using Flask, HTML/CSS with Flexbox, and JavaScript.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a simple implementation of a Stream Deck, a set of customizable buttons that trigger actions when pressed. The backend is powered by Flask, and the frontend utilizes HTML/CSS with Flexbox for layout and JavaScript to handle button clicks.

## Features

- Basic Stream Deck layout with customizable buttons.
- Easy integration of actions for each button using JavaScript.
- Responsive design using CSS Flexbox for different screen sizes.

## Prerequisites

Ensure you have the following installed before setting up the Stream Deck:

- [Python](https://www.python.org/) (>=3.6)
- [pip](https://pip.pypa.io/en/stable/)
- [Flask](https://flask.palletsprojects.com/)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/manish-jsx/Stream-Deck.git
    ```

2. Navigate to the project directory:

    ```bash
    cd stream-deck
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Customize the buttons and actions as needed.

## Customization

- **Button Actions**: Edit the `handleButtonClick` function in `index.html` to define actions for each button.

- **Styling**: Customize the appearance of the buttons by modifying the CSS in `static/styles.css`.

## Testing

To run tests, use the following command:

```bash
python -m unittest discover -s tests
```

## Contributing

Contributions are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

