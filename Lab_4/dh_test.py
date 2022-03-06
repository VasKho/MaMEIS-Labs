import dh_protocol
import random as rand

class Client:
    def generate_public_key(self) -> dict:
        self.__secret_value = rand.randint(1, 50)
        self.mod = 7351
        self.g = dh_protocol.generate(self.mod)
        public_key = pow(self.g, self.__secret_value) % self.mod
        return {"primitive": self.g, "mod": self.mod, "public": public_key}

    def generate_secret_key(self, public_value: int):
        self.__secret_key = pow(public_value, self.__secret_value) % self.mod
        del self.mod

    def print_secret(self):
        print(self.__secret_key)
    pass


class Server:
    def generate_secret_key(self, info: dict) -> int:
        self.__secret_value = rand.randint(1, 50)
        self.__secret_key = pow(info['public'], self.__secret_value) % info['mod']
        public_key = pow(info['primitive'], self.__secret_value) % info['mod']
        return public_key

    def print_secret(self):
        print(self.__secret_key)
    pass

if __name__ == "__main__":
    usr = Client()
    server = Server()

    info = usr.generate_public_key()
    info_1 = server.generate_secret_key(info)

    usr.generate_secret_key(info_1)

    usr.print_secret()
    server.print_secret()
