import sys
from pynput.keyboard import Key, Listener


def shift(arg_string, val):
	ret_str = ""
	for char in arg_string:
		ret_str += chr((ord(char) + val) % 256) 
	return ret_str

def erase_prev():
	sys.stdout.write("\r")

def print_stdout(arg_string):
	sys.stdout.write(arg_string)
	sys.stdout.flush()
	
def on_press(key):
	global contents
	global shift_total
	if (key == Key.left or key == Key.right):
		
		if key == Key.left:
			shift_total -= 1
					
		elif key == Key.right:
			shift_total += 1
		
		print("SHIFTED: [{}]".format(shift_total),end="")
		print_stdout(shift("\n"+contents,shift_total))
		
		
def on_release(key):
	if key == Key.esc:
		return False

if len(sys.argv) < 3:
	print("""
		NOT ENOUGH Arguments:
		Usage: "python3 <input_file> <output_file>"
	""")
	sys.exit(-1)
	
input_file = sys.argv[1]	
output_file = sys.argv[2]
shift_total = 0
contents = ""

with open(input_file, "r") as rf:	
	contents = rf.read()
			
with Listener(on_release=on_release, on_press=on_press) as listener:
	listener.join()

