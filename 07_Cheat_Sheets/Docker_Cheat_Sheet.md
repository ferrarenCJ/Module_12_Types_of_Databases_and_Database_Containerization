# Docker Cheat Sheet

## Show Images

```bash
docker images
```

## Show Containers

```bash
docker ps
```

## Show All Containers

```bash
docker ps -a
```

## Pull Image

```bash
docker pull mysql
```

## Start Container

```bash
docker run -d --name final_assignment \
-p 3300:3306 \
-e MYSQL_ROOT_PASSWORD=MyNewPass \
mysql
```

## Stop Container

```bash
docker stop final_assignment
```

## Remove Container

```bash
docker rm final_assignment
```

## Execute Command

```bash
docker exec -it final_assignment bash
```