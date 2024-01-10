FROM node

COPY . /src

WORKDIR /src

RUN npm install
RUN npm install axios
RUN npm install --save-dev @babel/plugin-proposal-private-property-in-object --legacy-peer-deps

COPY . .

EXPOSE 3000

ENV CHOKIDAR_USEPOLLING=true

CMD ["npm", "run", "start"]