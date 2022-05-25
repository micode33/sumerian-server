import os

def clear_terminal():
  _ = 'clear' if os.name == 'posix' else 'cls'
  os.system(_)