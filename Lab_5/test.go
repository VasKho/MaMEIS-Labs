package main

import utils "cryptutils/cryptutils"
import "fmt"

func main() {
	a, b := utils.GenerateRSAKeys()

	var message string
	fmt.Print("Enter message to encrypt: ")
	fmt.Scanln(&message)

	enc := utils.EncryptRSA(message, a)

	fmt.Println("Encrypted", enc)
	fmt.Println("Decrypted", utils.DecryptRSA(enc, b))

	signed := utils.Create_sign(message, b)
	fmt.Println(utils.Check_sign(signed, a))
}
