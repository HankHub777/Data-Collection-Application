# data-collection-app/README.md

# Data Collection App

This project is a GUI-based data collection application designed to facilitate the collection of user input through a map layout. The application features a time display, input fields, checkbox selections, and a message box for user selections. It also includes buttons for map rotation and coloring, a clickable grid map, and functionality to record data to an SQL Server database.

## Features

- **Interactive Map**: Clickable grid map for user interaction.
- **Time Display**: Real-time display of the current time.
- **Input Forms**: Fields for user input and checkbox selections.
- **Data Recording**: Functionality to record collected data to an SQL Server database.
- **User Feedback**: Message box to display user selections.

## Project Structure

```
data-collection-app
├── src
│   ├── main.py
│   ├── gui
│   │   ├── __init__.py
│   │   ├── map_grid.py
│   │   ├── time_display.py
│   │   └── input_forms.py
│   ├── database
│   │   ├── __init__.py
│   │   ├── connection.py
│   │   └── queries.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── config
│       ├── __init__.py
│       └── settings.py
├── tests
│   ├── __init__.py
│   ├── test_gui.py
│   └── test_database.py
├── requirements.txt
└── README.md
```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To start the application, run the following command:

```
python src/main.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.