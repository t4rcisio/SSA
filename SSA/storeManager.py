
import pickle
import rsa
import os
import jwt

class StoreManager:


    def __init__(self, TOKEN):
        
        self.jwToken = TOKEN
        self.__loadKeys()


    def broadcast(self, path, data=False):

        return self.__dataManager(path, data)


    def __loadKeys(self, pub_Key=False, priv_key=False):

        if pub_Key == False or priv_key==False:
            
            if os.path.exists("./.env"):
                dataFile = self.__jwDecode(open("./.env", "r", encoding="UTF-8").read())["payload"]
                self.publicKey = rsa.PublicKey.load_pkcs1(dataFile)
                self.privateKey = rsa.PrivateKey.load_pkcs1(dataFile)
            else:
                self.publicKey, self.privateKey = rsa.newkeys(512)
                data = self.__jwEncode(self.publicKey.save_pkcs1().decode('utf-8') + "\n" + self.privateKey.save_pkcs1().decode('utf-8'))
                open("./.env", "w", encoding="UTF-8").write(data)


    def __encript(self, data):

        obj = pickle.dumps(data)
        return rsa.encrypt(obj, self.publicKey)

    def __decrypt(self, data):

        return rsa.decrypt(data.encode('latin1'), self.privateKey)
    

    def __jwEncode(self, data):

        return jwt.encode({"payload": data}, self.jwToken, algorithm="HS512")
    
    def __jwDecode(self, data):
        return jwt.decode(data, self.jwToken, algorithms=["HS512"])
    

    def __dataManager(self, path, data=False):


        if data == False:

            encoded = open(path, "r", encoding="UTF-8").read()
            jwData = self.__jwDecode(encoded)
            obj =  self.__decrypt(jwData["payload"])
            return pickle.loads(obj)
        
        else:

            data = self.__encript(data).decode('latin1')
            paylaod = self.__jwEncode(data)
            open(path, "w", encoding="UTF-8").write(paylaod)



ab = StoreManager("abc")
ab.broadcast("./teste.txt", {"teste": "teste"})
print(ab.broadcast("./teste.txt"))
