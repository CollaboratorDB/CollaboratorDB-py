<!-- These are examples of badges you might want to add to your README:
     please update the URLs accordingly

[![Built Status](https://api.cirrus-ci.com/github/<USER>/collaboratordb.svg?branch=main)](https://cirrus-ci.com/github/<USER>/collaboratordb)
[![ReadTheDocs](https://readthedocs.org/projects/collaboratordb/badge/?version=latest)](https://collaboratordb.readthedocs.io/en/stable/)
[![Coveralls](https://img.shields.io/coveralls/github/<USER>/collaboratordb/main.svg)](https://coveralls.io/r/<USER>/collaboratordb)
[![PyPI-Server](https://img.shields.io/pypi/v/collaboratordb.svg)](https://pypi.org/project/collaboratordb/)
[![Conda-Forge](https://img.shields.io/conda/vn/conda-forge/collaboratordb.svg)](https://anaconda.org/conda-forge/collaboratordb)
[![Monthly Downloads](https://pepy.tech/badge/collaboratordb/month)](https://pepy.tech/project/collaboratordb)
[![Twitter](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter)](https://twitter.com/collaboratordb)
-->

[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)

# Python client to CollaboratorDB

Minimum working example:

```python
import collaboratordb as cdb
obj = cdb.fetch_object("scRNAseq:ZeiselBrainData@2023-08-08")
## Class SummarizedExperiment with 20006 features and 3005 samples
##   assays: ['counts']
##   row_data: ['featureType']
##   col_data: ['tissue', 'group #', 'total mRNA mol', 'well', 'sex', 'age', 'diameter', 'cell_id', 'level1class', 'level2class']
```

## Note

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
