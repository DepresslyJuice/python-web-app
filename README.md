# Python Web Application

This is a simple Python web application that replicates the functionality of a JavaScript server application. It is built using Flask and is configured to load environment variables.

## Project Structure

```
python-web-app
├── app
│   ├── __init__.py
│   ├── main.py
│   └── config
│       └── settings.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd python-web-app
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the root directory of the project and set the following environment variable:

```
PORT=5000
```

## Running the Application

To run the application, execute the following command:

```
python -m app.main
```

The application will start on the port specified in the `.env` file.

## License

This project is licensed under the MIT License.