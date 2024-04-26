# Pokedex Terminal Python
## PTP (Pokedex Terminal in Python)

Simple code based on Python to use on Terminal
> [!IMPORTANT]
> On Debian or any Linux Distro you must to create a virtual environment.
### How to install
Easy, create a virtual environment on Python
```
$ python3 -m venv PTP
$ source /path/to/your/virtual/environment
$ pip install pokebase argparse requests
```

### Usage
```
$ python3 pokemon.py --help
Your python pokedex
options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  name of the Pokemon
```

### Example
```
$ python3 pokemon.py -n pikachu
Pokemon name: 'pikachu'
Weight: '60'
Height: '4'
id: '25'
Available Pokemon Data
```
