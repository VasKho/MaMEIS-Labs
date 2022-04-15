package main

import utils "cryptutils/cryptutils"
import "fmt"


func main() {
    a, b := utils.GenerateRSAKeys()

    // fmt.Println(a)
    // fmt.Println(b)

    var message string
    fmt.Print("Enter message to encrypt: ")
    fmt.Scanln(&message)

    enc := utils.EncryptRSA(message, a)

    fmt.Println(enc)
    fmt.Println(utils.DecryptRSA(enc, b))
}
