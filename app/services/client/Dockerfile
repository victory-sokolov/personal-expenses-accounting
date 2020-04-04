FROM node:latest

WORKDIR client

COPY package.json /client
RUN npm install --silent

COPY . /client

CMD ["npm", "start"]