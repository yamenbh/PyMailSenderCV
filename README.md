# PyMailSenderCV

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

PyMailSenderCV is a Python script designed to simplify the process of sending personalized emails with attached CVs to multiple recipients listed in a CSV file.

## Features

- **CSV Integration:** Reads email recipients' details from a CSV file, making it easy to manage a large list of contacts.
- **Customizable Email Content:** Allows customization of the email subject and body to personalize messages for each recipient.
- **CV Attachment:** Automatically attaches CV files to the emails based on the information provided in the CSV file.

## Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/PyMailSenderCV.git
    cd PyMailSenderCV
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Prepare your CSV file with the following columns: `Name`, `Email`, `CV_FileName`.
2. Customize the email template in the `email_template.txt` file.
3. Run the script:

    ```bash
    python send_emails.py --csv_file your_recipients.csv --email_template email_template.txt
    ```

### Options

- `--csv_file`: Specify the path to your CSV file containing recipient information.
- `--email_template`: Specify the path to your email template file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to modify the badges, structure, or content as needed for your specific project.
