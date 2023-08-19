# Netstat Linux App

Network Monitoring App! This application allows you to analyze network connections and routing tables using the `netstat` utility. Below, you'll find instructions on how to install and run the app on your local machine.

## Installation Instructions

Follow these steps to set up the Network Monitoring App on your system:

1. **Clone the Repository and go to repo folder**

   ```bash
   cd /home/<username>/ mkdir python-clones
   cd python-clones
   git clone git@github.com:HansLanda96/netstat.git
   cd netstat
2. **Recommended to create venv**
   ```bash
   python -m venv venv
3. **Activate venv**

    *LINUX*:

        ```bash
        source venv/bin/activate

    *WINDOWS*:

        ```bash
        venv\Scripts\activate
4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
5. **Run the App**

   ```bash
   python app.py
6. **Access the App**

    Open your web browser and navigate to http://127.0.0.1:5000/ to view the Network Monitoring App.


>**To stop the app simply press CTRL+C in the terminal.**

# About the App
## The Network Monitoring App is a Python application that utilizes the Flask framework to provide a web-based interface for displaying network connection information and routing tables. It uses the netstat command-line tool to retrieve this information.

### I hope you find this app useful and informative!
