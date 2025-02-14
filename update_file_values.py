#This code will update of the value of a key in file
def update_file(file_name,key,value):
    with open(file_name,'r') as file:
        values=file.readlines()
    with open(file_name,'w') as file:
        for i in values:
            if key in i:
                file.write(key+"="+value+"\n")
            else:
                file.write(i)
folder="server.conf"
var="MAX_CONNECTIONS"
sub="100"
update_file(folder,var,sub)
