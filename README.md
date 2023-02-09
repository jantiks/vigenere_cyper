# Vigenre Cypher

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
`def encrypt(self, textToEncryipt, key)`<br />
Takes a plain text and a key as arguments and returns the decoded text<br />

`def decrypt(self, ciphertext, key)`<br />
Takes encrypted ciphertext and key as an argument, and returns encoded text. <br />

`def decryptWithoutKey(self, text)` <br />
Takes encrypted ciphertext and tries to hack it, returns 5 possible keys for the specified ciphertext.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
