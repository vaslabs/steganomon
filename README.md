# steganomon
Steganography using pokemon

Try the demo at http://pokemon.lp.gs/

```sh
echo "The quick brown fox jumps over the lazy dog" | go run testToCoords.go -t2e |\
python main.py | python decipher.py | go run testToCoords.go -ep2i >img.png
```
