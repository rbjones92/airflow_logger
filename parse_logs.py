from pathlib import Path    
import os

log_dir=os.getcwd()
files = Path(log_dir).rglob('*.log')
file_list = []
for file in files:
    file_list.append(file)

def parse_logs(file_list):
    log_list = []
    for file in file_list:
        with open(file) as f:
            for line in f:
                if line.startswith("["):
                    errorMessage=[]
                    # Catch Errors
                    if line.split(" ")[3]=="ERROR":
                        log = line.split(" ")[0]+" "+line.split(" ")[1]+" "+line.split(" ")[2]+" "+line.split(" ")[3]
                        # Find Error Message and Join
                        for i in range(5,len(line.split(" "))):
                            errorMessage.append(line.split(" ")[i])
                        err_log=" ".join(errorMessage)
                        parsed_log=log+" - "+err_log
                        log_list.append(parsed_log)

    return log_list

errors = parse_logs(file_list)
print(f'There are {len(errors)} errors')


error_txt = []
for error in errors:
    error_txt.append(error)

# Write to txt file
with open(r'errors.txt','w') as error_file:
    error_file.write('\n'.join(error_txt))


