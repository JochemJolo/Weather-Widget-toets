# Weather-Widget-toets
It is a very basic Weather widget that just works localy now
it is the basic of the basic for now where you put in a city or region name to see what weather there is and it saves what you already have searched for and puts that first before trying to overwrite and make a new file to stop it form using up the api pulls


To start this program
1. Get an API key from the weatherapi.com website
2. Create an .env file and put there API_KEY=YOUR_API_KEY
3. Go to cmd and to the file location. Use the command: python test.py
4. Click or copy the link that it has generated and there you have the website

Problems:
1. i was trying to make the application delete the .json files inside the Weather-Log folder automaticly.
    The first part of the python file is there to try and delete it every 30 minutes, but doesnt work.
2. was trying to make a website next to it to make it look better but didnt have enough time to implement that.

Programs:
1. Html and JavaScript are used to make the frontend and to take the information from the backend/send information to the backend
2. Python is used to get the api information from the site into a json file that the frontend can read.
3. Scss is being used as the styling for this project.