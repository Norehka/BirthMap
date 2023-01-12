Natal Chart Generator
This project is a simple Tkinter GUI application that generates natal charts, transit charts, and composite charts based
 on user input.

Requirements
Python 3
Tkinter
kerykeion
Usage
Clone the repository
Copy code
git clone https://github.com/<username>/natal-chart-generator.git
Install the required libraries
Copy code
pip install -r requirements.txt
Run the script
Copy code
python natal_chart_generator.py
Input
The user is prompted to input their name, birthdate, birth time, and location, as well as the type of chart they want
to generate (natal, transit, or composite). For composite chart, the second person's data is also needed.

Output
The generated chart is displayed to the user via a message box. The chart is also saved in the current directory as
an SVG file.

Note
This project uses the kerykeion library, which is a python wrapper for the Swiss Ephemeris. The Swiss Ephemeris is
a high precision ephemeris based on the DE431 ephemeris from JPL.It provides position and speed of the planets, Moon,
and Sun, as well as additional celestial bodies like the four largest asteroids, Chiron, the Lunar Nodes, and more.

License
This project is licensed under the MIT License.