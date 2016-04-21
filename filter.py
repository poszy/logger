# Read log file
# filter file to readable Format


def filterText():

    log_file = '/tmp/xorg.0.log'
    log_file2 = '/tmp/Xorg.1.log'



        # Read in the file
    filedata = None
    with open('/tmp/xorg.0.log', 'r') as file :
      filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('testspace', 'abcd')

    # Write the file out again
    with open('file.txt', 'w') as file:
      file.write(filedata)



def main():


    log_file = '/tmp/xorg.0.log'

    # Read in the file
    filedata = None
    with open(log_file, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('space', ' ')

    # Write the file out again
    with open(log_file, 'w') as file:
        file.write(filedata)


if __name__ == "__main__":
    main()
