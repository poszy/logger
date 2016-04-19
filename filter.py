# Read log file
# filter file to readable Format
log_file = '/tmp/xorg.0.log'

def filterText():
    
    search = open(log_file)
    next = search.readline()
    while next =="space":
        print next
        next = f.readline()
    search.close()
