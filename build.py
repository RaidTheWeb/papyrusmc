import patches
import sys

if len(sys.argv) == 1:
    patches.patchAll(".", "patches")
    sys.exit(0)
elif len(sys.argv) == 2:
    patches.patchAll(sys.argv[1], "patches")
    sys.exit(0)

patches.patchAll(sys.argv[1], sys.argv[2])
