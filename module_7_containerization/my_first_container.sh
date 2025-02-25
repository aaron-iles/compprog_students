# Let's try pulling an image down
docker pull ubuntu

# Now let's try running the container and have it print a simple message.
docker run --rm ubuntu echo "hello world"

# Now start up a container and have it run in the background.
docker run -d --name sleeping_forever ubuntu sleep infinity

# Attach to the container.
docker exec -it sleeping_forever bash

# Exit the container
exit

# Now check if the container is still running
docker container ls

# Now stop the container
docker stop sleeping_forever

# Finally, remove it.
docker rm sleeping_forever

# Let's start up a container and have it write to disk.
docker run --rm ubuntu bash -c 'echo "hey there" > /tmp/foo'

# Notice how /tmp/foo doesn't exist. This is because it was written inside the container not the host!
# Now let's make it write to the host
docker run --rm  -v /tmp/data:/tmp/data ubuntu bash -c 'echo "hey there" > /tmp/data/foo'

# Now try to see what is inside /tmp/data/foo on your host machine.
