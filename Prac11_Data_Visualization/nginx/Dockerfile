# Use an official Nginx image as a parent image
FROM nginx:alpine

# Copy nginx configuration file to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80

# Copy the built React app to the Nginx html directory
COPY --from=react-builder /app/build /usr/share/nginx/html

# Run Nginx
CMD ["nginx", "-g", "daemon off;"]