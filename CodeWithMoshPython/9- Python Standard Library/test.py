# 2
"""
from pathlib import Path

Path(r'C:\Program Files\Microsoft')
Path('')

"""
# 3
"""
from pathlib import Path

path = Path('../8- Modules/')

paths = [p for p in path.iterdir()]
path.glob("*.py")
print(paths)
"""
# 4
"""
from pathlib import Path
from time import ctime

path = Path('../8- Modules/ecommerce/__init__.py')
path.exists()
path.rename('init.txt')
path.unlink()
path.stat()
"""