from letter import alphabetical_list, getRandomKey
from frequency import frequency


# class Encryption:
#     def __init__(self, letter, key):
#         self.l = letter
#         self.lk = list(key)
#
#     def check_validation(self, plaintext):
#         check = True
#         for i in self.lk:
#             if i < 'a' and i > 'z':
#                 return;
#         return self.encrypt_algo(plaintext)
#     def encrypt_algo(self, plaintext):
#         cipher_text = ''
#         for i in plaintext:
#             if i >= 'a' and i<='z':
#                 cipher_text+=self.lk[self.l.index(i)]
#             else:
#                 cipher_text+=i
#         return cipher_text


class Decryption:
    def __init__(self, fre_table):
        self.t = fre_table

    def decrypt_algo(self, text):
        count_list = []
        temp_list = []
        result = ''

        for items in text:
            if items not in temp_list and items >= 'a' and items <= 'z':
                temp_list.append(items)
                count_list.append([text.count(items), items])
        count_list = sorted(count_list, reverse=True)
        cl=[]
        for i in range(len(count_list)-1):
            if count_list[i] not in cl:
                if count_list[i][0]!=count_list[i+1][0]:
                    cl.append(count_list[i])
                else:
                        d=[]

                        while(i < len(count_list)-1) and (count_list[i][0]==count_list[i+1][0]):
                            d.append(count_list[i])
                            i+=1
                        d.append(count_list[i])

                        d=sorted(d)

                        for v in d:
                            cl.append(v)

        if cl[len(cl)-1]!=count_list[len(count_list)-1]:
            cl.append(count_list[len(count_list)-1])
        count_list=cl
        print(count_list)
        for i in range(len(text)):
            v = -1
            for j in range(len(count_list)):
                if count_list[j][1] == text[i]:

                    v = j
                    break
            if text[i] >= 'a' and text[i] <= 'z' and v != -1:

                text=text.replace(text[0:i+1], text[0:i] + frequency[v][0],1)


        print(text)


if __name__ == "__main__":
    # original_data = 'Hello World'
    # original_data = original_data.lower()
    # print(alphabetical_list)
    #
    # exchange_key = getRandomKey()
    # sender = Encryption(alphabetical_list, exchange_key)
    #
    # print(list(exchange_key))
    # print(sender.check_validation(original_data))

    encrypt_message = 'aaaaaaaaaaaaaaaaaaa'
    encrypt_message = encrypt_message.lower()

    receiver = Decryption(frequency)
    receiver.decrypt_algo(encrypt_message)
