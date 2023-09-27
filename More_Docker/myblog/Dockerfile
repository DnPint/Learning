FROM node:17-alpine

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

# required for docker desktop port mapping
#default port 
EXPOSE 3000 

CMD ["npm", "start"]