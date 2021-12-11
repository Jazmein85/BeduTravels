DROP DATABASE IF EXISTS Tours;
CREATE DATABASE Tours;
GRANT ALL PRIVILEGES ON Tours.* TO Tours@'%' IDENTIFIED BY 'Tours';
GRANT ALL PRIVILEGES ON Tours.* TO Tours@'localhost' IDENTIFIED BY 'Tours';
# docker exec -i pythonsql mysql -hlocalhost -uBiblioteca -pBiblioteca Biblioteca < sql/tabla-libro.sql