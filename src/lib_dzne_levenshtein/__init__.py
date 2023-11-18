import numpy as _np


def get_matrix(*, args):
    """Utilizing the levenshtein program. """
    if len(args) == 0:
        return _np.matrix()
    
    ref = list()
    data = list()
    for i, a in enumerate(args):
        for j, b in enumerate(args[:i]):
            ref.append((i, j))
            data.append((a, b))

    outfilelines = get_lines(data)

    ans = _np.zeros((len(args), len(args)))
    for outfileline, (i, j) in zip(outfilelines, ref):
        ans[i][j] = outfileline
        ans[j][i] = outfileline
    return ans










 
 
