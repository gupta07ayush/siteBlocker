import datetime
import time
# You don't need to block your website forever. 
# Now you can give time duration for which this given website should block.

end_time = datetime.datetime(2023,4,28)

# List of websites, you want to block
site_block = ['www.lolly.com', 'www.facebook.com']

# hosts path where, where host file is. Hosts file records all the website url which we want to block.
host_path = 'C:/Windows/System32/drivers/etc/hosts'
redirect = '127.0.0.1'

while True:
    if datetime.datetime.now() < end_time:
        print('Start blocking the website...')
        with open(host_path, "r+") as host_file:
            host_file_content = host_file.read()
            for website in site_block:
                if website not in host_file_content:
                    host_file.write(redirect + " "+website+'\n')
                else:
                    pass
        
    else:
        # remove website name from hosts file because time is up
        with open(host_path, "r+") as host_file:
            host_file_content = host_file.readlines()
            # sending file reading pointer to start
            host_file.seek(0)
            
            for line in host_file_content:
                if not any(website in line for website in site_block):
                    host_file.write(line)
            host_file.truncate()
        
        time.sleep(5)
        