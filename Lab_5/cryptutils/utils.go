package cryptutils

import (
	"crypto/rand"
	"math/big"
)


type PublicKey struct {
    Exponent *big.Int
    N *big.Int
}


type PrivateKey struct {
    D *big.Int
    N *big.Int
}


func Powmod(base, exponent, mod *big.Int) *big.Int {
    res := big.NewInt(1)
    for exponent.Cmp(big.NewInt(0)) != 0 {
        if big.NewInt(0).Mod(exponent, big.NewInt(2)).Cmp(big.NewInt(1)) == 0  {
            res = big.NewInt(0).Mod(big.NewInt(0).Mul(res, base), mod)
            exponent = big.NewInt(0).Sub(exponent, big.NewInt(1))
        } else {
            base = big.NewInt(0).Mod(big.NewInt(0).Mul(base, base), mod)
            exponent = big.NewInt(0).Div(exponent, big.NewInt(2))
        }
    }
    return res
}


func gcd(num_1, num_2 *big.Int) *big.Int {
    num_1_cp := new(big.Int).Set(num_1)
    num_2_cp := new(big.Int).Set(num_2)
    for num_1_cp.Cmp(big.NewInt(0)) != 0 && num_2_cp.Cmp(big.NewInt(0)) != 0 {
        if num_1_cp.Cmp(num_2_cp) == 1 {
            num_1_cp.Mod(num_1_cp, num_2_cp)
        } else {
            num_2_cp.Mod(num_2_cp, num_1_cp)
        }
    }
    return big.NewInt(0).Add(num_1_cp, num_2_cp)
}


func getExp(phi *big.Int) *big.Int {
    var exponent *big.Int
    for exponent = big.NewInt(2); exponent.Cmp(phi) == -1; exponent.Add(exponent, big.NewInt(1)) {
        if gcd(exponent, phi).Cmp(big.NewInt(1)) == 0 { break }
    }
    return exponent
}


func GenerateRSAKeys() (PublicKey, PrivateKey) {
    prime_1, _ := rand.Prime(rand.Reader, 1024)
    prime_2, _ := rand.Prime(rand.Reader, 1024)
    n := big.NewInt(0).Mul(prime_1, prime_2)
    phi := big.NewInt(0).Mul(big.NewInt(0).Sub(prime_1, big.NewInt(1)), big.NewInt(0).Sub(prime_2, big.NewInt(1)))
    exponent := getExp(phi)
    d := big.NewInt(0).ModInverse(exponent, phi)
    return PublicKey{exponent, n}, PrivateKey{d, n}
}


func EncryptRSA(message string, key PublicKey) string {
    byte_msg := new(big.Int)
    byte_msg.SetBytes([]byte(message))
    enc := Powmod(byte_msg, key.Exponent, key.N)
    return string(enc.Bytes())
}


func DecryptRSA(encrypted string, key PrivateKey) string {
    byte_msg := new(big.Int)
    byte_msg.SetBytes([]byte(encrypted))
    dec := Powmod(byte_msg, key.D, key.N)
    return string(dec.Bytes())
}
