# Vigenre Cipher

Vigenre Cypher is a Python implementation for famous Vigenre Cypher https://en.wikipedia.org/wiki/Vigenère_cipher

## Usage
Disclaimer!!! the algorithm for hacking the cipher works best with middle to long texts(from 30 words) and the key for the cipher should be less than `20`
1. install the repository by downloading it or pulling from 'main' branch
2. after go to the directory of the repo and run
```terminal
  python3 main.py
 ```
## Documentation
The main functionality of the program is written in `CipherEngine` class, which has 3 public methods:<br />
### Encryption
`def encrypt(self, textToEncryipt, key)`<br />
Takes a plain text and a key as arguments and returns the decoded text<br />
```
engine = CipherEngine()
decryptedText = engine.decrypt("encrypted message", "key")
```

### Decryption
`def decrypt(self, ciphertext, key)`<br />
Takes encrypted ciphertext and key as an argument, and returns encoded text. <br />

```
engine = CipherEngine()
encryptedText = engine.encrypt("secret message", "key")
```

### Decryption without a key
`def decryptWithoutKey(self, text)` <br />
Takes encrypted ciphertext and tries to hack it, returns 5 possible keys for the specified ciphertext.

```
engine = CipherEngine()
possible_keys = engine.decryptWithoutKey("encrypted message")
```
`def decryptWithoutKey(self, text)` function uses frequency analysis for finding the possible keys, which is done by private function `def __compareFrequencies(self, text):`.

The algorithm for hacking the cipher works best with middle to long texts(from 30 words) and the key for the cipher should be less than 20. <br />
It's worth noting that this technique is not foolproof, and may not work well for very short ciphertexts or ciphertexts that have been encrypted with a very random or complex key. However, it can be a useful tool for quickly breaking simple substitution ciphers like the Vigenere cipher.

### Note
* `encrypt` and `decrypt` methods accept two parameters: the text to be encrypted/decrypted, and the key.
* `decryptWithoutKey` method accepts only one parameter: the text to be decrypted.
* If an invalid key is passed to `encrypt` or `decrypt`, a `ValueError` will be raised with a message indicating the issue.
* If the text to be decrypted with `decryptWithoutKey` is too short, a message "Short text, can't decode" is printed, and an empty string is returned.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
