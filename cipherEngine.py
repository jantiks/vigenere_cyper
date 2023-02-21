import itertools
import string

class CipherEngine:
    # From https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
    __englishLetterFreq = (0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772,
    0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978,
    0.02360, 0.00150, 0.01974, 0.00074)
    
    minKeySize = 1
    maxKeySize = 20

        
    def encrypt(self, textToEncryipt, key):
        key = key.lower()
        if not all(k in string.ascii_lowercase for k in key):
            raise ValueError("Invalid key {!r}; the key should not contain spaces in between and should only consist of English letters".format(key))
        keyIndex = 0
        result = []
        for letter in textToEncryipt.lower():
            if letter in string.ascii_lowercase:
                keyOffset = ord(key[keyIndex]) - ord('a')
                letterOffset = ord(letter) - ord('a')
                encryptedOffset = (keyOffset + letterOffset) % 26
                encryptedLetter = chr(ord('a') + encryptedOffset)
                result.append(encryptedLetter)
                keyIndex = (keyIndex + 1) % len(key)
            else:
                result.append(letter)
        return ''.join(result)

    def decrypt(self, ciphertext, key):
        key = key.lower()
        if not all(k in string.ascii_lowercase for k in key):
            raise ValueError("Invalid key {!r}; the key should not contain spaces in between and should only consist of English letters".format(key))
        inverseKey = "".join(chr(ord('a') + ((26) - (ord(k) - ord('a'))) % 26) for k in key)
        return self.encrypt(ciphertext, inverseKey)

    def decryptWithoutKey(self, text):
        best_keys = []

        text_letters = [c for c in text.lower() if c in string.ascii_lowercase]

        for keyLength in range(self.minKeySize, self.maxKeySize):
            key = [None] * keyLength
            for keyIndex in range(keyLength):
                letters = ""
                i = keyIndex
                while i < len(text_letters):
                    letters += text_letters[i]
                    i += keyLength
                shifts = []
                if not letters:
                    print("Short text, can't decode")
                    return ""

                for key_char in string.ascii_lowercase:
                    shifts.append(
                        (self.__compareFrequencies(self.decrypt(letters, key_char)), key_char)
                    )
                
                key[keyIndex] = min(shifts, key=lambda x: x[0])[1]
            best_keys.append("".join(key))

        best_keys.sort(key=lambda key: self.__compareFrequencies(self.decrypt(text, key)))
        return best_keys[:5]


    #MARK: Private
    def __compareFrequencies(self, text):
        if not text:
            return None
        text = [t for t in text.lower() if t in string.ascii_lowercase]
        freq = [0] * 26
        total = float(len(text))
        for l in text:
            freq[ord(l) - ord('a')] += 1
        return sum(abs(f / total - el) for f, el in zip(freq, self.__englishLetterFreq))