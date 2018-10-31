# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
SkipFilter
"""

__all__ = ["SkipFilter"]


from sklearn.base import TransformerMixin

from ...base_transform import BaseTransform
from ...internal.core.preprocessing.filter._skipfilter import \
    SkipFilter as core
from ...internal.utils.utils import trace


class SkipFilter(core, BaseTransform, TransformerMixin):
    """

    Skip the first N rows of the dataset, allowing limiting input to a
    subset of rows.

    :param columns: a string representing the column name to perform the
        transformation on.

        * Input column type: numeric.
        * Output column type: numeric.

        The << operator can be used to set this value (see
        `Column Operator </nimbusml/concepts/columns>`_)

        For example
         * SkipFilter(columns='age')
         * SkipFilter() << {'age'}

        For more details see `Columns </nimbusml/concepts/columns>`_.

    :param count: number of rows to skip from the beginning of the dataset.

    :param params: Additional arguments sent to compute engine.

    .. index:: transform, random

    Example:
       .. literalinclude:: /../nimbusml/examples/SkipFilter.py
              :language: python
    """

    @trace
    def __init__(
            self,
            count=0,
            columns=None,
            **params):

        if columns:
            params['columns'] = columns
        BaseTransform.__init__(self, **params)
        core.__init__(
            self,
            count=count,
            **params)
        self._columns = columns

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)