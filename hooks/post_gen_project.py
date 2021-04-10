import os
import shutil
import yaml
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

MANIFEST =  "manifest.yml"

def delete_resources_for_disabled_features():
    with open(MANIFEST) as manifest_file:
        manifest = yaml.load(manifest_file)
        for feature in manifest['features']:
            if not feature['enabled']:
                print("removing resources for disabled feature {}...".format(feature['name']))
                for resource in feature['resources']:
                    delete_resource(resource)
    print("cleanup complete, removing manifest...")
    delete_resource(MANIFEST)


def delete_resource(resource):
    if os.path.isfile(resource):
        print("removing file: {}".format(resource))
        os.remove(resource)
    elif os.path.isdir(resource):
        print("removing directory: {}".format(resource))
        shutil.rmtree(resource)

if __name__ == "__main__":
    delete_resources_for_disabled_features()
    os.system("./setup.sh")