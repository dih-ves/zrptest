# define a imagem base
FROM debian:latest
# define o mantenedor da imagem
LABEL maintainer="BISCM: Diego Galves"
# Atualiza a imagem com os pacotes
RUN apt-get update && apt-get upgrade -y
# Instala o NGINX para testar
RUN apt-get install nginx -y
# Expoe a porta 5003
EXPOSE 5003
# Comando para iniciar o NGINX no Container
CMD ["app.py", "-g", "daemon off;"]