FastAPI & MongoDB Template
---------------------------
Use this to quickly start a project with FastAPI and MongoDB through Docker. 
Clone the repo, then add a .env file to the top-level directory.
In the .env file, add the two following lines, replacing "<your_stuff_here>" with your values:
db_username=<your_stuff_here>
db_password=<your_stuff_here>
When you build the docker image file, it will pull in your authentication values and bake them in the image while keeping them out of your repo.
Make sure you have Docker Desktop installed, then open a terminal and navigate to the repo folder.
Build the image/run the containers with "docker-compose up --build".
Open your browser and navigate to 127.0.0.1:8000, and you should see {"msg":"Hello World!"}

You can build out the application from there.
