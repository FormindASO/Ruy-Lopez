with open('dlls.txt', 'r') as dlls_file:
  for line in dlls_file:
    if line == '\n': continue
    whole_line = ""
    if '#' not in line:
      whole_line = "{ "
      for char in line.strip():
        whole_line = whole_line + "'" + char + "'" + ","
      whole_line = whole_line + " 0 },"
      print(whole_line)

print('==========')


def generate_variable(dll_name):
  return f'char {dll_name.replace(".", "")}[] = "{dll_name}";'

def generate_condition(dll_name):
  return f'(StrStrIA((char*)lpFilename, (char*){dll_name.replace(".", "")}))'

whole_line = "if ( "
variables = []
conditions = []
with open('dlls.txt', 'r') as dlls_file:
  for line in dlls_file:
    line = line.strip()
    if line == '': continue
    if line == '\n': continue
    if '#' not in line:
      variables.append(generate_variable(line))
      conditions.append(generate_condition(line))

output = ""
for variable in variables:
  output = output + variable + '\n'

output = '\n' + output + "if (\n"
for condition in conditions:
  output = output + condition + ' || \n'

output = output + ') {'

print(output)
