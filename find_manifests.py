import os

potential_manifests = []

for path, directories, files in os.walk("."):
    for file in files:
        if file.endswith(".yaml"):
            potential_manifests.append(os.path.join(path, file))

likely_manifests = []

for file in potential_manifests:
    with open(file, "r") as potential_manifest:
        contents = potential_manifest.read()

        if "apiVersion:" in contents:
            # File is likely a k8s manifests
            likely_manifests.append(file)

print("::set-output name=files::" + "%0A".join(likely_manifests))
