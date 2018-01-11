import random


class EncodeAndDecode:
    # def __init__(self):
    #     #self._prefix = "http://tinyurl.com/"
    #     self._encoding = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    #     self.dict = {}
    #     self.key = ""
    encoding = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    dict = {}
    def GetRand(self):
        key=""
        for i in range(0,7):
            key = key + str(self.encoding[random.randint(0, 61)])
        return key

    def Encode(self, longUrl):
        key=self.GetRand()
        while (key in self.dict.keys()): # tiep tuc gen cho toi khi key ko ton tai o trong dict
            key = self.GetRand()
        self.dict[key] = longUrl
        return "http://tinyurl.com/" + key

    def Decode(self, shortUrl):
        shortUrl.replace("http://tinyurl.com/", "")
        return self.dict[shortUrl]


a = EncodeAndDecode()
a.Encode("fdafdafdafdafa")
print(a.dict)
print(a.Decode("http://tinyurl.com/chfnE2n"))

