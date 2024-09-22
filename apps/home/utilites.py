from .models import Profile

def get_user_profile_details(username):
    profile = Profile.objects.get(user__username=username)
    #port range
    port_range_str = profile.port_range
    start, end = map(int, port_range_str.split('-'))
    port_list = list(range(start, end + 1))
    port_list = [str(element) for element in port_list]
    #max ram
    max_ram = profile.max_ram
    ram_list = list(range(1, max_ram+1))
    ram_list = [str(element) for element in ram_list]
    return {'port_list': port_list, 'max_ram': max_ram, 'ram_list': ram_list}

def get_user_profile(username):
    return  Profile.objects.get(user__username=username)


def calculate_used_memory(data): #calculates memory from server data
    running_servers = data[0]
    total_memory = 0
    if running_servers==[]:
        return total_memory
    for item in running_servers:
        memory = item['memory'].split('G')[0] # Split the string at 'G' and keep the first part
        # Convert the string to an integer
        memory_value = int(memory)
        total_memory += memory_value
    return total_memory

