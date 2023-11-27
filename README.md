# Daily Email Report Automation Script

This Python script (`daily_mails.py`) automates the process of sending daily email reports using the `smtplib` and `schedule` libraries. It is a simple template that you can customize to fit your specific use case.

## Prerequisites

- Python 3.x
- `schedule` library (install using `pip install schedule`)

## Installation

1. Clone the repository or download the `daily_mails.py` file.

    ```bash
    git clone https://github.com/yourusername/daily-email-reports.git
    ```

2. Navigate to the project directory.

    ```bash
    cd daily-email-reports
    ```

3. Install the required dependencies.

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Update the following variables in the `daily_mails.py` script:

    - `sender_email`: Your email address from which the report will be sent.
    - `receiver_email`: The recipient's email address.
    - `subject`: The subject of the email.
    - `body`: The body of the email report.

2. Configure email server settings:

    - If you are using Gmail:
        - Update the SMTP server to `"smtp.gmail.com"` and the port to `587`.
        - Enable "Less secure app access" in your Google Account settings or use an App Password for authentication.

3. Set the scheduled time for the daily report email:

    - Adjust the time in the `schedule.every().day.at("08:00").do(send_email)` line according to your preferred time.

## Usage

1. Run the script using a Python interpreter:

    ```bash
    python daily_mails.py
    ```

2. Keep the script running, and it will automatically send the daily email report at the scheduled time.

## Important Note

- Ensure that you handle sensitive information like email passwords securely. Consider using environment variables or a configuration file.

## Author

- Manuel Dinis Junior

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
