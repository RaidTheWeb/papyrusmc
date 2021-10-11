import patches
import sys
import os

if len(sys.argv) == 1:
    patches.patchAll(".", "patches")
    sys.exit(0)
elif len(sys.argv) == 2:
    patches.patchAll(sys.argv[1], "patches")
    sys.exit(0)

for dir in ["src/main/java/net/minecraft/server/plugin"]:
    if os.path.exists(dir):
        print("[PapyPatchy]: Skipping directory creation of `" + dir + "`")
        continue
    print("[PapyPatchy]: Creating directory `" + dir + "`")
    os.mkdir(dir)

patches.patchAll(sys.argv[1], sys.argv[2])
