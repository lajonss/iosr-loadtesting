# Configuration

Provide your iosr-loadbalancer address as target in [locust.config.json](scripts/locust.config.json).


# Testing

To run the tests use

```
$ docker-compose up
$ docker-compose scale locust-worker=5
```

Locust will be available at http://127.0.0.1:8089
