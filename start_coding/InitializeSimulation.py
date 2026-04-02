import os
import numpy as np
from Prepare import Prepare
from Utilities import Utilities


class InitializeSimulation(Prepare, Utilities):
    def __init__(self,
                *args,
                **kwargs,
                ):
        super().__init__(*args, **kwargs)
