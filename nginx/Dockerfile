FROM nginx:stable-alpine
RUN ls
COPY ./nginx.conf /etc/nginx/templates/nginx.conf.template
CMD ["nginx", "-g", "daemon off;"]