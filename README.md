﻿# MultithreadProxy

A basic proxy server written in Golang. The server establishes a connection to the destination (target) service whenever a client connects to the proxy service.

This implementation offers fundamental functionality, allowing for extension such as filtering and connection timeouts. It's important to note that the proxy receives data from the client and forwards it to the target service until it encounters EOF (indicating the termination of the connection from the client).

## Building

- Clone the project
- Run `go build`

## Running

```
Usage of MultithreadProxy:
  -destIp string
        proxy target IP (default "127.0.0.1")     
  -destPort string
        proxy target port (default "6666")
  -srcIp string
        proxy source IP (default "127.0.0.1")
  -srcPort string
        proxy source port (default "4444")
```

Example run

`./MultithreadProxy -srcIp 127.0.0.1 -srcPort 4444 -destIp 127.0.0.1 -destPort 6666`

## Testing

To test, we can use the `test.py` file for testing. The Python test file is dependent on the [pwntools Python library](https://github.com/Gallopsled/pwntools)
