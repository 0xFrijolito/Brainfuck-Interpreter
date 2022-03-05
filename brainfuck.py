import sys

VALID_INSTRUCTIONS = [">","<",".","[","]","+","-"]

def clean_code (raw_code):
  clean = []
  for i in raw_code:
    if i in VALID_INSTRUCTIONS:
      clean.append(i)

  return clean

# Load the instruction in memory
def main () -> None:
  brainfuck_code = clean_code(open(sys.argv[1]).read()) 

  MEMORY = [0] * 2**16  # Program memory 
  rptr = []             # Return pointer of a bucle 
  iptr = 0              # instruction pointer
  ptr = 0               # Current pointer 

  while iptr < len(brainfuck_code):
    instruction = brainfuck_code[iptr]

    if instruction == ">":
      ptr+=1
    elif instruction == "<":
      ptr-=1
    elif instruction == "+":
     if MEMORY[ptr] + 1 > 255:
       MEMORY[ptr] = 255
     else:
       MEMORY[ptr]+= 1 
    elif instruction == "-":
      if MEMORY[ptr] - 1 < 0:
        MEMORY[ptr] = 0
      else:
        MEMORY[ptr]-=1
        
    elif instruction == ".":
      print(chr(MEMORY[ptr]), end="")
    elif instruction == "[":
      rptr.append(iptr)
    
    elif instruction == "]":
      if MEMORY[ptr] == 0:
        rptr.pop()
      else:
        iptr = rptr[-1]

    iptr+=1

if __name__ == "__main__":
  main()
