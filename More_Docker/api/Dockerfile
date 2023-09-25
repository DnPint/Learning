#Specify a base image
FROM node:17-alpine3.15

#Set working directory
#Needed for RUN npm install to work in the Container directory (/app) instead of dockerfile directory
WORKDIR /app

#Copy source code to image
#image will be created in the same directory as the Dockerfile
#COPY SOURCE DESTINATION (here, . means /app directory), see Workdir
COPY . .

#Run commands inside the image
#Install dependencies specified in package.json
RUN npm install

#Expose port 4000, must be the same as the port in app.js
#This is the port that the application will listen to
#This is not the host port, but the container port
#The host computer port can be mapped to this port
EXPOSE 4000

#Execute the application
#CMD is the default command to run when the container starts
CMD [ "node", "app.js" ]
