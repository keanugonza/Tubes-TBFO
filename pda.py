states = []
symbols = []
stackSymbols = []
stackStart = ""
startInput = "" 
startSymbol = ""
acceptableStates = []
acceptedConfig = [] 
productions = {}
acceptWith = ""
found = 0 

def start(fileName) :
	# Memulai membaca file untuk diparsing
	readPDA(fileName)

def process(arr) :
	# Memulai proses PDA setelah rule terbentuk pada variabel global dengan masukan yaitu grammar
	startInput = arr
	if not generate(startSymbol, startInput, startStack, [(startSymbol, startInput, startStack)]) :
		done()
	else :
		done()

def done() :
	# Mengembalikan hasil apakah grammar yang diproses valid (Accepted) atau tidak valid (Syntax error)
	if found :
		print ("\033[1mAccepted\033[0m\n")
	else :
		print ("\033[1mSyntax error\033[0m\n")

def readPDA(fileName) :
	# Membaca file pda atau memparsing file pda dan menyimpannya ke dalam varibel yang telah ada
	global productions
	global startSymbol
	global startStack
	global acceptableStates
	global acceptWith

	lines = [line.rstrip() for line in open(fileName)]

	startSymbol = lines[3]

	startStack = lines[4]

	acceptableStates.extend(lines[5].split())

	acceptWith = lines[6] 

	for i in range(7, len(lines)) :
		production = lines[i].split(" ")

		configuration = [(production[1], production[2], production[4], production[3])]

		if not production[0] in productions.keys() : 
			productions[production[0]] = []

		configuration = [tuple(s if s != "e" else "" for s in tup) for tup in configuration]

		productions[production[0]].extend(configuration)
	

def generate(state, input, stack, config) :
	# Fungsi yang membuat semua konfigurasi rule yang mungkin dari masukkan
	global productions
	global found

	total = 0

	if found :
		return 0

	if check(state, input, stack) :
		found = 1
		acceptedConfig.extend(config)
		return 1

	moves = next(state, input, stack, config)
	if len(moves) == 0 :
		return 0

	for i in moves :
		total = total + generate(i[0], i[1], i[2], config + [(i[0], i[1], i[2])])  

	return total

def next(state, input, stack, config) :
	# Menentukan apakah simbol yang diterima terminal atau non-terminal
	global productions

	moves = []

	for i in productions :

		if i != state :
			continue

		for j in productions[i] :
			current = j
			new = []

			new.append(current[3])

			if len(current[0]) > 0 :
				if len(input) > 0 and input[0] == current[0] :
					new.append(input[1 :])
				else :
					continue
			else :			
				new.append(input)

			if len(current[1]) > 0 :
				if len(stack) > 0 and stack[0] == current[1] :
					new.append(current[2] + stack[1 :])
				else :
					continue
			else :
				new.append(current[2])
			moves.append(new)
	
	return moves

def check(state, input, stack) :
	# Memeriksa hasil akhir yang berupa empty stack atau final state sudah benar
	global acceptWith
	global acceptableStates

	if len(input) > 0 : 
		return 0

	if acceptWith == "E" :
		if len(stack) < 1 : 
			return 1
		return 0
	else :
		for i in acceptableStates :
			if i == state : 
				return 1
		return 0


<<<<<<< Updated upstream
# checks if symbol is terminal or non-terminal
def done():
	if found:
		print ("Hurray! Input word \"" + start_input + "\" is part of grammar." )
	else:
		print ("Sorry! Input word \"" + start_input + "\" is not part of grammar." )



# UI
# here it should read automata in from file
filename = "pda.txt"
while not parse_file(filename):
	print ("File not found!")
	filename = input("Please enter your automata file again:\n")
print ("Automata built.")

start_input = input("Please enter your word:\n")
print ("Checking word \"" + start_input + "\" ...")


found = False
# magic starts here
if not generate(start_symbol, start_input, start_stack, [(start_symbol, start_input, start_stack)]):
	done()
else:
	print_config(accepted_config) # show list of configurations to acceptance
	done()

# start_input = input("Enter your next word (or n):\n")
print ("Checking word \"" + start_input + "\" ...")

	
=======
		
>>>>>>> Stashed changes
