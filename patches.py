import os
import shutil

def patchAll(path, patches_location):
    internal = os.listdir(patches_location)
    for file in internal:
        with open(os.path.join(patches_location, file)) as f:
            if file.endswith(".java"):
                location = f.readlines()[0].strip()
                location = location.strip("/ ").replace(".", "/")
                print("[PapyPatchy]: Patching file `{}` to `{}/{}`".format(file, location, file))
                shutil.copy(os.path.join(patches_location, file), os.path.join(path, "src", "main", "java", location, file))
    for file in internal:
        with open(os.path.join(patches_location, file)) as f:
            if file.endswith(".replace"):
                lines = f.readlines()
                location = lines[0].strip()
                location = location.strip("/ ").replace(".", "/") + ".java"
                target = "\n".join(lines[1:]).split("-split-")[0].strip()
                replacement = "\n".join(lines[1:]).split("-split-")[1].strip()
                with open(os.path.join(path, "src", "main", "java", location)) as f2:
                    print("[PapyPatchy]: Patching occurrence `{}` to `{}` in file `{}`".format(target, replacement, location))
                    data = f2.read()
                    data = data.replace(target, replacement)
                    open(os.path.join(path, "src", "main", "java", location), 'w').write(data)

    print("[PapyPatchy]: Finished file patching")
