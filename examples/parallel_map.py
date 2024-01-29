#!/usr/bin/env python3


import concurrent.futures


class _Unpacker:
    """
    A helper class to unpack arguments passed to a function in parallel_map.
    """
    def __init__(self, func):
        self._func = func

    def __call__(self, packed_args):
        return self._func(*packed_args)


def parallel_map(func: callable,
        vals: list or tuple,
        starmap: bool = False,
        max_workers: int = None,
        run_type: str = 'processes') -> list:
    """
    Maps a function over an iterable of values in parallel.

    :param callable func: A callable to be run in parallel.
    :param list or tuple args: The values to be passed into the callable.
    :param bool starmap: A boolean of whether of not the args should be unpacked. This is needed if
    func takes multiple arguments.
    :param int max_workers: The number of child processes/threads to spawn.
    :param str run_type: The type of pool to create: processes (for CPU intensive tasks or working
    around the GIL) or threads (for IO bound tasks).
    :return list: A list of results in the order that the vals were passed.
    """
    if starmap:
        func = _Unpacker(func)
    if run_type == 'threads':
        executor = concurrent.futures.ThreadPoolExecutor
    if run_type == 'processes':
        executor = concurrent.futures.ProcessPoolExecutor
    else:
        raise ValueError('run_type must be one of "threads" or "processes"')
    with executor(max_workers=max_workers) as ex:
        return list(ex.map(func, vals))


