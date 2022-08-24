# Phone-Number-Location-With-Python
Get Phone Number Location With Python
How To Track Phone Number Location With Python

Open PyCharm and create a new project
To create a new project, click on File at the top-left corner of your screen.

Select New Project.

Give your new project a name, then click Create. For example, the name of my project is tracking.

PyCharm will display your project name at the left side of the screen with its location. It will look like this: C:\Users\hp\PyCharmProject\tracking.

2. Right-click on the project name

Right-click on the project name. Then click New. Now click on Python file.

3. Give the Python file a name

Name the Python file. Ensure the name ends with .py. For example body.py. Press the keyboard — enter.

4. Go to Terminal

Below the screen at the bottom-left, you will see Terminal. Click on it. Now type the following:

pip install phonenumbers


Run it. This will install the Python phonenumbers library. Phonenumbers library is used for parsing, formatting, storing, and validating international phone numbers. Remember to add “s” at the end of phonenumbers.

The installation takes a few minutes. Close the Terminal when the library is installed successfully.

5. Write in main.py

Click on body.py or on the name you gave the file. Now write the following code:

import phonenumbers

6. Create another Python file

Again, right-click on the project name. Click New. Click Python file. Give your new file a different name — for instance, test.py. Let the name also end with .py. Press the keyboard enter.

The purpose of the new file is to store the number you want to track. You will see the full information below.

7. Write in test.py

In test.py (or the name you gave the file), write the number you want to track with the country code:

number = input("Please enter mobile number with +_____ :")

The variable — number — stores the phone number you want to track. Remember to include the country code starting with a +. The number above is just a random example.

8. Click on main.py

Write:

import phonenumbers
from test import number

from phonenumbers import geocoder

The first line of the code imports the phone number you want to track to the main.py file.

Geocoder here is a function in phonenumbers. It provides geographical coordinates corresponding to a location.

9. Get the history of the phone number from its country by parsing two parameters

In main.py file, write:

ch_nmber = phonenumbers.parse(number,"CH")

CH stands for Country History.

10. Run your code

Also in main.py, write:

print(geocoder.description_for_number(ch_nmber,"en"))

“en” means English. You want the info to display in English.

Note: don’t write “eng”. You will get a blank display.

Run the code. You will find the run option at the top of the screen. Click Run, then press the keyboard enter. Or click Run ‘body’.

You will see the country name of the phone number you tracked displayed below on your screen.

How To Track the Name of Network Provider
For every phone number, there is a network provider.

Include the below codes to find out the name of the network provider of the phone number.

Click on main.py
Write:

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_nmber,"en"))



Carrier is a function. It helps you get the name of the service provider of the phone number you’re tracking.

Run your code again. You will see the name of the service provider on your screen.


