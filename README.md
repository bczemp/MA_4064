Since this is not a full python module, you must add this to the top of any file attempting to import from the [lib](lib) directory.
``` Python
import sys
from os import expanduser, abspath

GIT_DIR = <git directory path>
sys.path.append(abspath(expanduser(GIT_DIR + '/lib')))
```
Note: The path to the git directory can be a relative path and be referenced from the home directory.
