<h1>"Coding Activity Tracker"</h1>
<br />
</br>

<h2>Description</h2>
This Python application allows users to track their daily coding activity. Using the Pixela API, it creates a graph that visually represents the hours spent on coding each day. 
It's a simple yet effective tool for anyone looking to monitor and improve their coding habits over time.
<br />


<h2>Features</h2>

- **User Account Creation on Pixela:** Automates the process of creating a Pixela account.
- **Graph Creation**: Enables users to create a custom graph for tracking coding hours.
- **Daily Tracking:** Allows adding data points to the graph for each day's coding hours.
- **Interactive Input:** Users can input the number of hours spent coding directly through the terminal.
- **Data Visualization:** Provides a visual representation of coding activity over time.

<h2>Prerequisites </h2>
<h3>To run this project, you will need:</h3>

+ **Python:** The application is written in Python, a recent version of [Python](https://www.python.org/downloads/).
+ **Pip:** Python's package installer, pip, should be installed for managing Python packages. It usually comes with Python installation.
+ **Pixela account token** stored in an environment variable (PIXELA_TOKEN).

<h2>Installation</h2>

- **Clone the Repository:** git clone https://github.com/SonnyGU/Kayne.West.git
-  **Navigate to the Project Directory:** cd habit-tracker
- **Install the Requests library using pip:** pip install requests
- **Run the Application:** python main.py
- **Set Environment Variables:** Store your Pixela token in an environment variable PIXELA_TOKEN.
<h2>Usage</h2>

<h3>Upon execution:</h3>

- If it's your first time, the script will create a new Pixela user and graph (ensure you uncomment the relevant sections).
- Each execution will prompt you to enter the number of hours you coded that day, which will be added as a data point on your Pixela graph

<h2>Customization</h2>

- You can customize the graph ID, name, unit, type, and color by modifying the graph_config dictionary.
- Change the USERNAME to your Pixela username.

<h2>Program walk-through:</h2>

<p align="center">
Launch the utility: <br/>
<img src="https://i.imgur.com/cdssZW7.png" height="80%" width="80%" alt="Habit Tracker Steps"/>
<br />
<br />
You Will Be Prompted to Enter the Time spent on habit (7 hours in this case for me):  <br/>
<img src="https://i.imgur.com/seXSKN3.png" height="50%" width="50%" alt="Habit Tracker Steps"/>
<br />
<br />
The output will be on your graph: <br/>
<img src="https://i.imgur.com/f9g41x1.png" height="80%" width="80%" alt="Habit Tracker Steps"/>
<br />
<br />




<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
