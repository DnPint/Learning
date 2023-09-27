#Specify a base image
FROM node:17-alpine3.15

#For development only
#USed with Volumes to automatically restart the container when the source code changes
RUN npm install -g nodemon

#Set working directory
#Needed for RUN npm install to work in the Container directory (/app) instead of dockerfile directory
WORKDIR /app

#Copy package.json to image
#Taking advantage of Docker caching
COPY package.json .

#Run commands inside the image
#Install dependencies specified in package.json
RUN npm install

#Copy source code to image
#image will be created in the same directory as the Dockerfile
#COPY SOURCE DESTINATION (here, . means /app directory), see Workdir
COPY . .

#Expose port 4000, must be the same as the port in app.js
#This is the port that the application will listen to
#This is not the host port, but the container port
#The host computer port can be mapped to this port
EXPOSE 4000

#Execute the application
#CMD is the default command to run when the container starts
#CMD [ "node", "app.js" ]
CMD [ "npm", "run", "dev" ]

#run the container with port mapping, volume mapping and remove container when stopped
#With nodemon, the container will restart automatically when the source code changes
#docker run --name myapp_c_nodemon -p 4000:4000 --rm -v "C:\Learning\More_Docker\api:/app"  myapp2:nodemon
