from letter import alphabetical_list, getRandomKey
from test import str1, str2, str3, str4, str5, str6


class Encryption:
    def __init__(self, letter, key):
        self.l = letter
        self.k = key
        self.lk = list(key)

    def check_validation(self, plaintext):
        list_key = list(self.k)
        check=True
        for i in list_key:
            if i < 'a' and i > 'z':
                check = False
        if check is True:
            return self.encrypt_algo(plaintext)
        else:
            return;

    def encrypt_algo(self, plaintext):
        ciper_table = {}
        cipher_text = ''
        for items in range(len(self.l)):
            ciper_table[self.l[items]] = self.lk[items]
        for i in ciper_table:
            print(i+':'+ciper_table[i])
        for elements in plaintext:
            if elements not in ciper_table.keys():
                cipher_text += elements
            else:
                cipher_text += ciper_table[elements]
        return cipher_text


class Decryption:
    def __init__(self, fre_text):
        self.t = self.frequency_calculation(fre_text)

    def frequency_calculation(self, text):
        count_list = []
        temp_list = []
        result = ''

        for items in text:
            if items not in temp_list and items >= 'a' and items <= 'z':
                temp_list.append(items)
                count_list.append([text.count(items), items])
        count_list = sorted(count_list, reverse=True)
        cl = []
        for i in range(len(count_list) - 1):
            if count_list[i] not in cl:
                if count_list[i][0] != count_list[i + 1][0]:
                    cl.append(count_list[i])
                else:
                    d = []

                    while (i < len(count_list) - 1) and (count_list[i][0] == count_list[i + 1][0]):
                        d.append(count_list[i])
                        i += 1
                    d.append(count_list[i])

                    d = sorted(d)

                    for v in d:
                        cl.append(v)
        if len(cl) != 0:
            if len(cl) != len(count_list) and count_list[len(count_list) - 1] not in cl:
                for i in range(len(cl) - 1, len(count_list)):
                    cl.append(count_list[i])
            return cl
        return count_list

    def decrypt_algo(self, text):
        count_list = self.frequency_calculation(text)
        for i in range(len(text)):
            v = -1
            for j in range(len(count_list)):
                if count_list[j][1] == text[i]:

                    v = j
                    break
            if text[i] >= 'a' and text[i] <= 'z' and v != -1:

                text = text.replace(text[0:i+1], text[0:i] + self.t[v][1],1)

        print(text)


if __name__ == "__main__":
    print('Exercise 1:')
    original_data = str3
    original_data = original_data.lower()
    print(alphabetical_list)

    exchange_key = getRandomKey()
    sender = Encryption(alphabetical_list, exchange_key)

    print(list(exchange_key))
    print(sender.check_validation(original_data))
    print('--------------------------------------------------')
    print('Exercise 2:')
    encrypt_message = str5
    encrypt_message = encrypt_message.lower()

    f = open("frequency_source.txt", encoding='utf-8')
    text = f.read()
    receiver = Decryption(text)
    print(receiver.t)
    receiver.decrypt_algo(encrypt_message)
    