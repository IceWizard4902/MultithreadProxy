package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"net"
)

// Method to filter payload
func filter(payload string) bool {
	// To be changed
	return len(payload) > 10
}

// Handle the incoming connection
func handleConnection(c net.Conn, target string) {
	fmt.Printf("Serving %s\n", c.RemoteAddr().String())

	// Open a TCP connection to the target application
	dest, err := net.Dial("tcp", target)

	if err != nil {
		fmt.Println(err)
		return
	}

	// Wait for data to come line by line
	for {
		netData, err := bufio.NewReader(c).ReadString('\n')
		if err != nil {
			fmt.Println(err)
			break
		}

		payload := string(netData)

		// Filtering on each line
		if filter(payload) {
			dest.Write([]byte(payload))
		} else {
			// If this does not pass the filter, then close the connection
			c.Close()
			dest.Close()
		}
	}

	// Cleanup after everything is done
	dest.Close()
	c.Close()
}

func main() {
	sourceIp := flag.String("srcIp", "127.0.0.1", "proxy source IP")
	sourcePort := flag.String("srcPort", "4444", "proxy source port")
	destIp := flag.String("destIp", "127.0.0.1", "proxy target IP")
	destPort := flag.String("destPort", "6666", "proxy target port")

	flag.Parse()

	// Obtain the source and the destination
	source := *sourceIp + ":" + *sourcePort
	dest := *destIp + ":" + *destPort

	l, err := net.Listen("tcp", source)

	if err != nil {
		log.Fatal(err)
	}
	defer l.Close()

	// Busy wait for the connections from the client
	for {
		c, err := l.Accept()
		if err != nil {
			log.Fatal(err)
		}
		go handleConnection(c, dest)
	}
}
