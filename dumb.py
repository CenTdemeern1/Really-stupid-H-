import os,sys

def dumb(lines):
	out=""
	for line in lines:
		if line=="q":
			break
		else:
			out+=interpretline(line)+"\n"
	out=Cify(out)
	return out

def Cify(text):
	return """#include <stdio.h>
int main() {
	printf(\""""+repr(text)[1:-1]+"""\");
	return 0;
}"""

def interpretline(line):
	return "Hello, Hello!" if line=="hh" else "World, World!" if line=="ww" else "Hello, World!" if line=="hw" else "World, Hello!" if line=="wh" else "Hello!" if line=="h" else "World!" if line=="w" else line

if __name__=="__main__":
	if len(sys.argv)<=1:
		print("""Usage:
python3 dumb.py [flags] filename

Flags are currently unimplemented (Not that I have any to add right now). This isn't supposed to be good anyway.
Output goes to filename+".exe" and filename+".c", not much more to it.
Since it's just a printf statement you can just remove the file extension from the .exe and make it executable for it to work on Linux or whatever.
Make sure you have GCC installed!""")
		sys.exit()
	filename = sys.argv[-1]
	with open(filename,"r") as file:
		with open(filename+".c","w") as outfile:
			outfile.write(dumb(file.read().split("\n")))
	os.system(f"gcc {filename+'.c'} -Os -o {filename+'.exe'}")
