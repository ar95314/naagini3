def do_stuff(input):
	v,c = [int(x) for x in input.split(" ")]
	print(c-v)
while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) # next line was found 
  except (EOFError):
    break #end of file reached
