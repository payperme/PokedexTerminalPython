import pokebase as pb
import argparse
import requests

parser = argparse.ArgumentParser(description='Your python pokedex')
parser.add_argument('-n', '--name', type=str, help='name of the Pokemon')
args = parser.parse_args()

if args.name:
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{args.name}'
        response = requests.get(url)
        #pokemon = pb.pokemon(args.name)
        if response.status_code != 404:
            pokemon = pb.pokemon(args.name)
            print(f"Pokemon name: '{pokemon.name}'")
            print(f"Weight: '{pokemon.weight}'")
            print(f"Height: '{pokemon.height}'")
            print(f"id: '{pokemon.id}'")
            print("Available Pokemon Data")
        else:
            print(f"Error: Pokemon '{args.name}' not found")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("Please provide a valid Pokemon name using the -n or --name option")

