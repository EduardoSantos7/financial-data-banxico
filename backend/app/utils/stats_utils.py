class StatsUtils:

    @staticmethod
    def max_min_avg(_list):
        """Return tthe max, min element and the everage of an numeric list.
        The idea off this func is to only iterate once.

        Args:
            _list ([int]): [example: UDIS]
        """
        _max = 0
        _min = float('inf')
        avg = 0
        for elem in _list:
            _max = max(_max, elem or 0)
            _min = min(_min, elem or 0)
            avg += elem

        return _max, _min, (avg/len(_list) if len(_list) else 0)
