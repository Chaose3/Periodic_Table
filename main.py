element_symbols = {
	'H': 'Hydrogen', 'He': 'Helium', 'Li': 'Lithium', 'Be': 'Beryllium', 'B': 'Boron',
	'C': 'Carbon', 'N': 'Nitrogen', 'O': 'Oxygen', 'F': 'Fluorine', 'Ne': 'Neon',
	'Na': 'Sodium', 'Mg': 'Magnesium', 'Al': 'Aluminum', 'Si': 'Silicon', 'P': 'Phosphorus',
	'S': 'Sulfur', 'Cl': 'Chlorine', 'Ar': 'Argon', 'K': 'Potassium', 'Ca': 'Calcium',
	'Sc': 'Scandium', 'Ti': 'Titanium', 'V': 'Vanadium', 'Cr': 'Chromium', 'Mn': 'Manganese',
	'Fe': 'Iron', 'Co': 'Cobalt', 'Ni': 'Nickel', 'Cu': 'Copper', 'Zn': 'Zinc',
	'Ga': 'Gallium', 'Ge': 'Germanium', 'As': 'Arsenic', 'Se': 'Selenium', 'Br': 'Bromine',
	'Kr': 'Krypton', 'Rb': 'Rubidium', 'Sr': 'Strontium', 'Y': 'Yttrium', 'Zr': 'Zirconium',
	'Nb': 'Niobium', 'Mo': 'Molybdenum', 'Tc': 'Technetium', 'Ru': 'Ruthenium', 'Rh': 'Rhodium',
	'Pd': 'Palladium', 'Ag': 'Silver', 'Cd': 'Cadmium', 'In': 'Indium', 'Sn': 'Tin',
	'Sb': 'Antimony', 'Te': 'Tellurium', 'I': 'Iodine', 'Xe': 'Xenon', 'Cs': 'Cesium',
	'Ba': 'Barium', 'La': 'Lanthanum', 'Ce': 'Cerium', 'Pr': 'Praseodymium', 'Nd': 'Neodymium',
	'Pm': 'Promethium', 'Sm': 'Samarium', 'Eu': 'Europium', 'Gd': 'Gadolinium', 'Tb': 'Terbium',
	'Dy': 'Dysprosium', 'Ho': 'Holmium', 'Er': 'Erbium', 'Tm': 'Thulium', 'Yb': 'Ytterbium',
	'Lu': 'Lutetium', 'Hf': 'Hafnium', 'Ta': 'Tantalum', 'W': 'Tungsten', 'Re': 'Rhenium',
	'Os': 'Osmium', 'Ir': 'Iridium', 'Pt': 'Platinum', 'Au': 'Gold', 'Hg': 'Mercury',
	'Tl': 'Thallium', 'Pb': 'Lead', 'Bi': 'Bismuth', 'Po': 'Polonium', 'At': 'Astatine',
	'Rn': 'Radon', 'Fr': 'Francium', 'Ra': 'Radium', 'Ac': 'Actinium', 'Th': 'Thorium',
	'Pa': 'Protactinium', 'U': 'Uranium', 'Np': 'Neptunium', 'Pu': 'Plutonium',
	'Am': 'Americium', 'Cm': 'Curium', 'Bk': 'Berkelium', 'Cf': 'Californium',
	'Es': 'Einsteinium', 'Fm': 'Fermium', 'Md': 'Mendelevium', 'No': 'Nobelium',
	'Lr': 'Lawrencium', 'Rf': 'Rutherfordium', 'Db': 'Dubnium', 'Sg': 'Seaborgium',
	'Bh': 'Bohrium', 'Hs': 'Hassium', 'Mt': 'Meitnerium', 'Ds': 'Darmstadtium',
	'Rg': 'Roentgenium', 'Cn': 'Copernicium', 'Fl': 'Flerovium', 'Lv': 'Livermorium',
	'Ts': 'Tennessine', 'Og': 'Oganesson'
}

element_symbols_lower = {k.lower(): (k, v) for k, v in element_symbols.items()}

def fuzzy_spell(word, max_mismatches=2):
	word = word.lower()
	best_result = {'matches': [], 'unmatched': '', 'mismatches': len(word) + 1}

	def backtrack(index, path, unmatched, mismatches):
		nonlocal best_result

		if mismatches > max_mismatches:
			return

		if index >= len(word):
			if mismatches < best_result['mismatches']:
				best_result = {
					'matches': path[:],
					'unmatched': unmatched,
					'mismatches': mismatches
				}
			return

#Change these values for how far apart they can be, ex (1,2,3)
		for i in (1, 2, 3):
			chunk = word[index:index+i]
			if chunk in element_symbols_lower:
				path.append(element_symbols_lower[chunk])
				backtrack(index+i, path, unmatched, mismatches)
				path.pop()

		# Skip current letter as a mismatch
		backtrack(index+1, path, unmatched + word[index], mismatches + 1)

	backtrack(0, [], "", 0)
	return best_result

def main():
	word = input("Enter a word: ").strip()
	result = fuzzy_spell(word)

	if result['matches']:
		symbols = ''.join(sym for sym, _ in result['matches'])
		names = ', '.join(f"{sym} ({name})" for sym, name in result['matches'])
		print(f"\nClosest match found ({result['mismatches']} letter{'s' if result['mismatches'] != 1 else ''} off):")
		print(f"{symbols}")
		print(f"Elements: {names}")
		if result['unmatched']:
			print(f"Unmatched letters: {result['unmatched']}")
	else:
		print("No good matches.")

if __name__ == "__main__":
	main()
