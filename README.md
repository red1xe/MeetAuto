# MeetAuto - Meeting Automation Tool :robot: :calendar:

MeetAuto is a Streamlit web application that allows you to manage and automate your meetings. You can add meetings along with their details, and MeetAuto will help you keep track of them.

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Dependencies](#dependencies)
4. [Usage](#usage)
5. [Features](#features)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

MeetAuto is a simple yet powerful tool for organizing your meetings efficiently. With its user-friendly interface, you can add your meetings, including the meeting name, link, day, time, and type. The application will display your current meetings and allow you to delete them when they are no longer needed.

## Getting Started

To get started with MeetAuto, follow these steps:

1. Clone the repository:
   `git clone https://github.com/red1xe/MeetAuto.git`
2. Install the dependencies (see [Dependencies](#dependencies))
3. Run the application:
   `streamlit run app.py`
4. Fill in the meeting details and click on the "Add Meeting" button
5. Run the automation script:
   `python main.py`

## Dependencies

MeetAuto requires the following dependencies:

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [pickle](https://docs.python.org/3/library/pickle.html)
- [datetime](https://docs.python.org/3/library/datetime.html)

## Usage

Run the app.py file to start the Streamlit app.
The application will open in your default web browser.
Add your meetings by providing the necessary details in the input widgets.
Click the "Add Meeting" button to save the meeting details.
Your added meetings will be displayed in a table below the input widgets.
To delete a meeting, click the "Delete" button next to the corresponding meeting in the table.
Finally, run the main.py file to start the automation script.

## Features

- Add meetings with name, link, day, time, and type.
- Display the list of current meetings with the option to delete them.
- Automatic saving of meetings data to a file for future reference.
- User-friendly interface for easy interaction.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the application, feel free to create a pull request.

Fork the repository.
Create a new branch for your feature or bug fix.
Make changes and commit them with descriptive commit messages.
Push your changes to your fork.
Create a pull request against the main repository.

## License

The code in this repository is licensed under the MIT License. Feel free to use and modify the code as per the terms of the license.
