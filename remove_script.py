import sys

def main(key, type, area, user):
    path = f'folder-test/right_folder/this_folder/{area}.yaml'

    if True:
        modification = '      - ferramenta: ' + user + '\n'
        with open(path, 'r') as archive:
            lines = archive.readlines()

            for count, line in enumerate(lines):
                if user in line:
                    lines[count] = ''
            archive.close()

        with open(path, 'w') as archive:
            archive.writelines(lines)
        
            archive.close()
        with open(path, 'r') as archive:
            print(archive.read())
        print("OK")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    


