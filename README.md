# Portal GNTK

This project is a Python script that automatically logs into a captive portal. It continuously checks for an internet connection and, once available, opens a web browser to automatically click the login button.

## Features

*   Continuously checks for a connection to the portal.
*   Automatically opens a web browser (Edge or Firefox).
*   Automatically clicks the login button.
*   Displays a notification upon successful connection.

## Requirements

*   Python 3.x
*   The following Python libraries:
    *   `selenium`
    *   `webdriver-manager`
    *   `python-dotenv`

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/portal-gntk.git
    cd portal-gntk
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Run the driver installation script:
    ```bash
    python install_drivers.py
    ```

## Configuration

Create a `config.env` file in the root of the project with the following variables:

```
URL=http://10.31.0.5/portal/
BTN_LOGIN_ID=entrarbtn
CONFIRM_LABEL_ID=swal2-title
NAVEGATOR=edge
```

*   `URL`: The URL of the captive portal.
*   `BTN_LOGIN_ID`: The ID of the login button.
*   `CONFIRM_LABEL_ID`: The ID of the element that appears after a successful login.
*   `NAVEGATOR`: The browser to use (`edge` or `firefox`).

## Usage

Run the main script:

```bash
python portal_gntk.py
```

The script will run in the background, continuously checking for the portal and attempting to log in.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.