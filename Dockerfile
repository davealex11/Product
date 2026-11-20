FROM nginx:stable-alpine
ENV PORT=8080
COPY deploy/default.conf.template /etc/nginx/templates/default.conf.template
COPY outputs/netradyne-products.html /usr/share/nginx/html/index.html
COPY outputs/netradyne-products.html /usr/share/nginx/html/netradyne-products.html
COPY outputs/assets/d450-360.mp4 outputs/assets/d450-360-mobile.mp4 outputs/assets/dr40-360.mp4 outputs/assets/dr40-360-mobile.mp4 outputs/assets/d450-render.webp outputs/assets/dr40-1.webp /usr/share/nginx/html/assets/
EXPOSE 8080
