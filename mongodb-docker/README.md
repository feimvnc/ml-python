# check and remove previous mongo db docker instance
docker ps
docker rm mongo

# start docker mongodb 
docker run -d -p 27017:27017 --name mongodb mongo

