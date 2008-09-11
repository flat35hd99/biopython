# Copyright (C) 2002, Thomas Hamelryck (thamelry@binf.ku.dk)
# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.  

try:
    from Numeric import sqrt, argmin, argmax, sum, power, concatenate, array, Float0
except ImportError:
    from numpy.oldnumeric import (sqrt, argmin, argmax, sum, power,
            concatenate, array, Float0)
import os

# My Stuff
from Entity import Entity

__doc__="Model class, used in Structure objects."


class Model(Entity):
    """
    The object representing a model in a structure. In a structure
    derived from an X-ray crystallography experiment, only a single 
    model will be present (with some exceptions). NMR structures 
    normally contain many different models. 
    """

    def __init__(self, id):
        """
        Arguments:
        o id - int
        """
        self.level="M"
        Entity.__init__(self, id)

    # Private methods

    def _sort(self, c1, c2):
        """Sort the Chains instances in the Model instance.

        Chain instances are sorted alphabetically according to
        their chain id. Blank chains come last, as they often consist
        of waters.

        Arguments:
        o c1, c2 - Chain objects
        """
        id1=c1.get_id()
        id2= c2.get_id()
        # make sure blank chains come last (often waters)
        if id1==" " and not id2==" ":
            return 1
        elif id2==" " and not id1==" ":
            return -1
        return cmp(id1, id2)

    # Special methods

    def __repr__(self):
        return "<Model id=%s>" % self.get_id()

    # Public

    def get_residues(self):
        for c in self:
            for r in c:
                yield r

    def get_atoms(self):
        for r in self.get_residues():
            for a in r:
                yield a

