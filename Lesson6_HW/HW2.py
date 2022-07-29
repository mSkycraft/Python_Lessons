import re

actions = {
  "^": lambda x, y: str(float(x)**float(y)),
  "*": lambda x, y: str(float(x) * float(y)),
  "/": lambda x, y: str(float(x) / float(y)),
  "+": lambda x, y: str(float(x) + float(y)),
  "-": lambda x, y: str(float(x) - float(y))
}
 
priority = r"\((.+?)\)"
action_reg = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
 
def arifmetic(line: str):
 
    while (True):
        search = re.search(priority, line)
        if search is not None:
            line = line.replace(search.group(0), arifmetic(search.group(1)))
        else: break
 
    for symbol, action in actions.items():
        while (True):
            search = re.search(action_reg.format(symbol), line)
            if(search is not None):
                line = line.replace(search.group(0), action(*search.groups()))
            else: break
    return line
 
 
exp = "(10*2)+1*(4+5)"
print(arifmetic(exp))