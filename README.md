[![Docker Image CI](https://github.com/samuel-kuhn/MM-Dashboard/actions/workflows/docker-image.yml/badge.svg)](https://github.com/samuel-kuhn/MM-Dashboard/actions/workflows/docker-image.yml)





# Minecraft Manager - Dashboard

This dashboard built on django uses the [Minecraft Manager - API](https://github.com/samuel-kuhn/minecraft-manager-api) to help you manage minecraft servers easily.

## Installation

There are two ways how you can start the webserver:

### 1. Docker

```
docker run -d --name MM-Dashboard -p 8000:8000 stubble1749/minecraft-manager
```

### 2. Docker Compose (Recommended)

Modify the docker-compose.yml file and run the following command:

```
docker compose up -d
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
