# steganomon
Steganography using pokemon

Try the demo at http://pokemon.lp.gs/

### Deps

You need Go and Python to run the tools.

You need to install 2 libraries which are dependencies:

```sh
go get -u github.com/llgcode/draw2d

sudo pip install pokemonNames
# And probably you need to change the permission of the following file
# sudo chmod 666 /usr/local/lib/python2.7/dist-packages/pokemonNames/names.list
```

### Run the tool

```sh
echo "The quick brown fox jumps over the lazy dog" | go run testToCoords.go -t2e |\
python main.py | python decipher.py | go run testToCoords.go -ep2i >img.png
```
