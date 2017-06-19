# Traefik as a load balancer

What would we need?

 - docker installed
 - docker compose installed

The proxy or load balancer will point to the domain `docker.localhost` and create an internal test network using the bridge network driver in Docker, we will use the `docker-compose.yml` file in the proxy file. Important lines are commented in the file, go and check it out.

Start the load balancer going to the `proxy` folder and start with `docker compose`

```
docker-compose up -d
```

For see how it is balanced, just scale up the whoami with:

```
docker-compose scale whoami=2
```

To see the ECS options check [the documentation](https://docs.traefik.io/toml/#ecs-backend)
