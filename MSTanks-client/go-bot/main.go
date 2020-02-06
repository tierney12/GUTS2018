package main

import (
    "fmt"
    "net"
)

var HOSTNAME = "127.0.0.1"
var PORT = "8052"
var NAME = "ThiccThonkerGo"

func main() {
    fmt.Println("This is my go bot")

    // Connect to server
    tcpAddr, err := net.ResolveTCPAddr("tcp", HOSTNAME+":"+PORT)
    if err != nil {
        fmt.Println(err)
    }

    conn, err := net.DialTCP("tcp", nil, tcpAddr)
    if err != nil {
        fmt.Println(err)
    }

    fmt.Println(conn)

    sendTestMessage(conn)

    //createTankMessage := &CreateTankMessage{Name: NAME}
    //bytes, err := json.Marshal(createTankMessage)
    //if err != nil {
    //    fmt.Println(err)
    //}
    //fmt.Println(string(bytes))
    //
    //var byte1 uint8
    //byte1 = 1
    //var byte2 uint8
    //byte2 = uint8(len(bytes))
    //
    //finalBytes := make([]byte, 0)
    //finalBytes = append(finalBytes, byte1)
    //finalBytes = append(finalBytes, byte2)
    //finalBytes = append(finalBytes, bytes...)
    //
    //fmt.Println(string(finalBytes))
    //
    //fmt.Fprintf(conn, string(finalBytes))
}

func sendTestMessage(conn *net.TCPConn) {
    var testByte byte
    testByte = 0

    bytes := make([]byte, 0)
    bytes = append(bytes, testByte)
    bytes = append(bytes, testByte)

    _, err := conn.Write(bytes)
    if err != nil {
        fmt.Println(err)
    }
    fmt.Println("message sent")

    reply := make([]byte, 2)
    _, err = conn.Read(reply)
    if err != nil {
        fmt.Println(err)
    }

    fmt.Println("reply:", string(reply))
}
