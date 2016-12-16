import sys
import colored_traceback

colored_traceback.add_hook(always=True)

if len(sys.argv) <= 1:
    raise IOError("Missing python file argument. Please use `python -m colored_traceback somefile.py args...`")

file = sys.argv[1]
sys.argv = sys.argv[1:]

with open(file) as f:
    code = compile(f.read(), file, 'exec')
    exec(code)
