OPTIONS = {'display_width': 80}


class set_options(object):
    """Set global state within a controlled context

    Currently, the only supported option is ``display_width``, which has a
    default value of 80.

    You can use ``set_options`` either as a context manager:

    >>> ds = xray.Dataset({'x': np.arange(1000)})
    >>> with xray.set_options(display_width=40):
    ...     print(ds)
    <xray.Dataset>
    Dimensions:  (x: 1000)
    Coordinates:
      * x        (x) int64 0 1 2 3 4 5 6 ...
    Data variables:
        *empty*

    Or to set global options:

    >>> xray.set_options(display_width=80)
    """
    def __init__(self, **kwargs):
        self.old = OPTIONS.copy()
        OPTIONS.update(kwargs)

    def __enter__(self):
        return

    def __exit__(self, type, value, traceback):
        OPTIONS.clear()
        OPTIONS.update(self.old)
