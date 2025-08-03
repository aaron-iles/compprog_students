# Container Basics

## Description
In this assignment, you'll run your very first Docker containers! You'll learn how to pull images, run containers in the foreground and background, interact with them, and explore volumes for data persistence.

## Instructions

1. **Pull a Docker image:**
    ```bash
    docker pull ubuntu
    ```

2. **Run a container to print a message:**
    ```bash
    docker run --rm ubuntu echo "hello world"
    ```

3. **Run a background container:**
    ```bash
    docker run -d --name sleeping_forever ubuntu sleep infinity
    ```

4. **Attach to the container using an interactive shell:**
    ```bash
    docker exec -it sleeping_forever bash
    ```

5. **Exit the container shell:**
    ```bash
    exit
    ```

6. **Check if the container is still running:**
    ```bash
    docker container ls
    ```

7. **Stop the container:**
    ```bash
    docker stop sleeping_forever
    ```

8. **Remove the stopped container:**
    ```bash
    docker rm sleeping_forever
    ```

9. **Write to disk inside a container (this won't persist to host):**
    ```bash
    docker run --rm ubuntu bash -c 'echo "hey there" > /tmp/foo'
    ```

10. **Write to disk and persist it on the host using a volume:**
    ```bash
    docker run --rm -v /tmp/data:/tmp/data ubuntu bash -c 'echo "hey there" > /tmp/data/foo'
    ```

11. **On the host machine, verify the content:**
    ```bash
    cat /tmp/data/foo
    ```

## Submission Checklist

- [ ] You've pulled and run the Ubuntu container.
- [ ] You've run a container in the background and attached to it.
- [ ] You've written a file using Docker and verified persistence with a volume.
- [ ] You've pushed a short write-up or terminal transcript of your steps to your repo (optional).
- [ ] Submit your GitHub URL or a screenshot as proof of completion.

## Resources

- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/cli/)
- [Docker Volumes](https://docs.docker.com/storage/volumes/)
