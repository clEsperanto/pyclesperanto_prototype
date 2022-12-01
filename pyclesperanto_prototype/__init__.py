from ._tier0 import *
from ._tier1 import *
from ._tier2 import *
from ._tier3 import *
from ._tier4 import *
from ._tier5 import *
from ._tier6 import *
from ._tier8 import *
from ._tier9 import *
from ._tier10 import *
from ._tier11 import *

__version__ = "0.19.4"
__common_alias__ = "cle"

# array API interoperability
import numpy as np
# bool = np.bool
uint8 = np.uint8
uint16 = np.uint16
uint32 = np.uint32
uint64 = np.uint64
int8 = np.int8
int16 = np.int16
int32 = np.int32
int64 = np.int64
float32 = np.float32
