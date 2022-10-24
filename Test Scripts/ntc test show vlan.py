from ntc_templates.parse import parse_output

vlan_output = (
        "VLAN Name                             Status    Ports\n"
        "---- -------------------------------- --------- -------------------------------\n"
        "1    default                          active    Gi0/1\n"
        "10   Management                       active    \n"
        "50   VLan50                           active    Fa0/1, Fa0/2, Fa0/3, Fa0/4, Fa0/5,\n"
        "                                                Fa0/6, Fa0/7, Fa0/8\n")

vlan_parsed = parse_output(platform="cisco_ios", command="show vlan", data=vlan_output)


def get_vlan_info(vlan_id):

    for i in range(len(vlan_parsed)):

        for key, value in vlan_parsed[i].items():
            if value == vlan_id:
                for key, value in vlan_parsed[i].items():
                    if isinstance(value ,list):
                        print(key,':')
                        for int in range(len(value)):
                            print(value[int])
                    else:
                        print(f'{key} : {value}')





    print('')


get_vlan_info('50')
