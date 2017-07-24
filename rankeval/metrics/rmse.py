# Copyright (c) 2017, All Contributors (see CONTRIBUTORS file)
# Authors: Cristina Muntean <cristina.muntean@isti.cnr.it>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import numpy as np

from rankeval.metrics import Metric, MSE


class RMSE(Metric):
    """
    Root mean squared error

    """
    def __init__(self, name='RMSE', cutoff=None):
        """

        Parameters
        ----------
        name
        cutoff
        """
        super(self.__class__, self).__init__(name)
        self.cutoff = cutoff
        self._mse = MSE(cutoff=cutoff)

    def eval(self, dataset, y_pred):
        """

        Parameters
        ----------
        dataset
        y_pred

        Returns
        -------

        """
        return super(self.__class__, self).eval(dataset, y_pred)

    def eval_per_query(self, y, y_pred):
        """

        Parameters
        ----------
        y
        y_pred

        Returns
        -------

        """
        mse = self._mse.eval_per_query(y, y_pred)
        return np.sqrt(mse)

    def __str__(self):
        s = self.name
        if self.cutoff is not None:
            s += "@{}".format(self.cutoff)
        return s



