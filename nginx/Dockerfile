FROM nginx:stable-alpine
COPY ./nginx.conf /etc/nginx/templates/nginx.conf.template
CMD ["nginx", "-g", "daemon off;"]

#Probably better way to use volume instead of copy