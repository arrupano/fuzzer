name: wordpress
services:
  wordpress:
    image: wordpress:latest
    container_name: wordpress-web
    environment:
        WORDPRESS_DB_HOST: wordpress-db:3306
        WORDPRESS_DB_USER: root
        WORDPRESS_DB_PASSWORD: wordpress
    ports:
        - 8080:80
    depends_on:
      - mysql
  mysql:
    image: mysql:latest
    container_name: wordpress-db
    environment:
        MYSQL_ROOT_PASSWORD: wordpress
        MYSQL_DATABASE: wordpress
        MYSQL_PASSWORD: wordpress