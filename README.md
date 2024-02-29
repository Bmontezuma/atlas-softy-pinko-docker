# ***Docker***

## Author
***Brandon Montezuma***

- [Github](https://github.com/Bmontezuma)
- [LinkedIn](https://www.linkedin.com/in/brandon-montezuma-aaa461167/)

# Context

Docker is a platform that allows you to containerize your applications, meaning that you can package them into portable, self-contained environments which can run anywhere. This means that you can quickly move your application from one environment to another, such as from your local computer to a server, without worrying about dependencies or configuration issues. Docker achieves this by using containers, which are isolated environments that contain everything an application needs to run, such as libraries, dependencies, and configurations. Docker containers are lightweight and can be started and stopped quickly, making them ideal for modern software development and deployment. With Docker, you can also quickly scale your application by running multiple containers of the same application on different hosts (or the same host, as we will do in this project), and manage them using Docker Compose or other orchestration tools.

Ultimately, what you will create in this project is an infrastructure for an application that utilizes a reverse proxy, a load balancer, two application servers, and one front-end server.

Let’s consider the following design:

# High-level Design

In this design, there is a single server that acts as the entry point for your application. That server acts as a reverse proxy server, which routes traffic to either the API servers or the front-end static-content server; it also acts as a load balancer to balance traffic between the two API servers. When traffic comes in, the server will determine which service it needs to go to (either the front-end static-content server or the API server) and:
   
 If the request is to be routed to the front-end static-content server, it will do so and any static content that is returned from the front-end static-content server to the proxy server will then be sent to the client. The client isn’t directly communicating with the front-end static-content server.
   
   If the request is to be routed to the API server, then it will first go through a load-balancing algorithm to determine which API server to send the request to. We will be using the basic Round Robin load-balancing algorithm for our site. Once the request is routed to an API server and the response is sent back to the proxy server, it will then be sent to the client. The client isn’t directly communicating with either of the API servers.

# What You Need Before Starting
-   Install Docker Desktop on your local computer (not your sandbox)
    - https://www.docker.com/
    - For more detailed installation instructions, see:
    - [Windows](https://docs.docker.com/desktop/install/windows-install/)
    - [Mac](https://docs.docker.com/desktop/install/mac-install/)
    - [Linux](https://docs.docker.com/desktop/install/linux-install/)
    - [Chromebook](https://www.techrepublic.com/article/install-docker-chromeos/) - Note: this is the Docker engine, but not Docker Desktop. It is unclear how well this will work on a chromebook - you may want to use a Windows, Mac, or Linux machine or a machine on campus, instead.
Familiarize yourself with Docker
    - [Docker Tutorial](https://docs.docker.com/get-started/)
