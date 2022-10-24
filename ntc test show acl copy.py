from ntc_templates.parse import parse_output





def ntc_acl_parse(acl_config):
    with open(acl_config , 'r') as file:
        acl_output = file.read()
        acl_parsed = parse_output(platform="cisco_ios", command="show ip access-lists", data=acl_output)
        return acl_parsed



def parsed_acl_to_yaml(acl_parsed, new_acl_name):
    file2 = open(new_acl_name,"w")
    for i in range(len(acl_parsed)):
        x = acl_parsed[i]["acl_name"]
        for key, value in acl_parsed[i].items():
            if i == 0:
                continue
            if key == "acl_name" and i== 1:
                file2.write(f'- {key}: \'{value}\'\n')
                for key, value in acl_parsed[i].items():
                    if value != '':
                        if key == "acl_name" or key == "acl_type":
                            continue                
                        if key == "line_num":
                            file2.write(f'   {key}: \'{value}\'\n')
                            continue
                        if key == "action":
                            file2.write(f'    {key}: \'{value}\'\n')
                            continue 
                        if key == "protocol":
                            file2.write(f'     {key}: \'{value}\'\n')
                            continue           
                        else:
                            print(f'{key}: {value}')
                            file2.write(f'       {key}: \'{value}\'\n')
            if key == "acl_name" and x == acl_parsed[i]["acl_name"]:
                for key, value in acl_parsed[i].items():
                    if value != '':
                        if key == "acl_name" or key == "acl_type":
                            continue                
                        if key == "line_num":
                            file2.write(f'   {key}: \'{value}\'\n')
                            continue
                        if key == "action":
                            file2.write(f'    {key}: \'{value}\'\n')
                            continue 
                        if key == "protocol":
                            file2.write(f'     {key}: \'{value}\'\n')
                            continue           
                        else:
                            print(f'{key}: {value}')
                            file2.write(f'       {key}: \'{value}\'\n') 

    file2.close()

def main():
    acl_config = 'Test Scripts\mgmt_acl.txt'
    acl_parsed = ntc_acl_parse(acl_config)
    new_acl_name = 'Test Scripts\mgmt_acl.yml'
    parsed_acl_to_yaml(acl_parsed, new_acl_name)




main()

