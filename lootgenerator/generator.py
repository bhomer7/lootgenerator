
import json


def load_table(table_name):
	with open('./tables/' + table_name) as file:
		table = json.load(file)
	return table


def print_loot(loot):
	pass


def main():
	table = Generator.load_table('TreasureHoard0to4.json')
	loot = Generator.roll_loot(table)
	Generator.print_loot(loot)


if __name__=='__main__':
	main()
