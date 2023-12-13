FROM node

COPY . /src
WORKDIR /src

RUN npm install
RUN npm install axios
RUN npm install --save-dev @babel/plugin-proposal-private-property-in-object --legacy-peer-deps

CMD ["npm", "run", "start"]