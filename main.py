import sys
import yaml

def main(type, area, user):
    path = f'folder-test/right_folder/this_folder/{area}.yaml'

    if type == 'insert':
        with open(path, 'r') as archive:
            dict_data = yaml.safe_load(archive)
            
        dict_data['spec']['values']['users'].append({'ferramenta' : user})
        yaml_archive = yaml.dump(dict_data, sort_keys=False)

        with open(path, 'w') as archive:
            archive.write(yaml_archive)
        archive.close()


    elif type == 'remove':
        with open(path, 'r') as archive:
            dict_data = yaml.safe_load(archive)

        dict_data['spec']['values']['users'].remove({'ferramenta' : user})
        yaml_archive = yaml.dump(dict_data, sort_keys=False)

        with open(path, 'w') as archive:
            archive.write(yaml_archive)
        archive.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
