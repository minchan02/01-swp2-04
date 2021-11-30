class LockString:
    # 암호화 함수
    def encryption(self, word, n):
        m = list(word)
        for i in range(len(m)):
            if m[i].isupper():
                m[i] = chr((ord(m[i]) - ord('A') + n) % 26 + ord('A'))
            elif m[i].islower():
                m[i] = chr((ord(m[i]) - ord('a') + n) % 26 + ord('a'))
        return ''.join(m)
    
    # 복호화 함수
    def decryption(self, word, n):
        m = list(word)
        for i in range(len(m)):
            if m[i].isupper():
                m[i] = chr((ord(m[i]) - ord('A') - n) % 26 + ord('A'))
            elif m[i].islower():
                m[i] = chr((ord(m[i]) - ord('a') - n) % 26 + ord('a'))
        return ''.join(m)
