from ntc_templates.parse import parse_output
import sys



with open('Test Scripts\ACL.txt' , 'r') as file:
        acl_output = file.read()
        acl_parsed = parse_output(platform="cisco_ios", command="show ip access-lists", data=acl_output)


file2 = open("Test Scripts\ACL_2.yml","w")


for i in range(len(acl_parsed)):
    #file2.write(' - ACL_ITEMS')
    for key, value in acl_parsed[i].items():
        if i == 0:
            continue
        if key == "acl_name":
            file2.write(f'- {key}: \'{value}\'\n')
            for key, value in acl_parsed[i].items():
                if value == '':
                    continue
                if key == "acl_name":
                    continue
                if key == "acl_type":
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
                    file2.write(f'      {key}: \'{value}\'\n')



file2.close()






