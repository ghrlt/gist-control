# Gist Control

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![](https://komarev.com/ghpvc/?username=ghrlt-gist-control&color=brightgreen&label=Views) 

Use this module to interact with (mostly yours) gists!

## Installation
Require Python >=3.6 (f-strings)

`pip3 install gist-control`


## Usage
```python
# app.py

import os
from dotenv import load_dotenv
load_dotenv()

from gist_control import Gist


gctrl = Gist( os.getenv("oauth-token") )
```
```env
# .env
oauth-token=ghp_bozbegz...ege
```

Check examples [here](https://github.com/ghrlt/gist-control/tree/master/examples/complete.py)
