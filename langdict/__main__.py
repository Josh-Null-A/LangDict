import sys
from .langdict import main

if len(sys.argv) > 1:
    main(*sys.argv)
else:
    raise ValueError("Expected args to be passed to LangDict")
