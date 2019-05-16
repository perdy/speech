# Validation of ML services

Here is the source code of the service and tests used in this talk.

There is a make script to ease the process of building the service and tests containers (both are dockerized) and also 
to simplify the execution.

## Requirements

* [Python] 3.6+
* [Clinner]

## Build

```console
$ python3 make build
```

## Run

```console
$ python3 make run
```

## Test

It's necessary to start the service before run the tests.

```console
$ python3 make test
```

[Python]: https://www.python.org
[Clinner]: https://github.com/perdy/clinner
