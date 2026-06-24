FROM node:18-alpine

WORKDIR /usr/src/app

# Copy the package.json configuration file first
COPY package.json ./

# Let npm handle the fresh installation completely inside Docker
RUN npm install

# Copy the rest of your application code (including your new index.js)
COPY . .

# Expose the application port 
EXPOSE 3000

# Run the web server
CMD [ "node", "index.js" ]