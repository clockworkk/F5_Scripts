#Philip Middleton
#Create, Modify, and Delete: VIPs, Pools, and Pool Members

import bigsuds
from config import config
from optparse import OptionParser

#Creates a VIP to be used by pools
def create_a_vip(b):
	b.LocalLB.VirtualServer.create( \
		definitions = [{'name' : config['vip_name'], \
		'address' : config['ip_address'], \
		'port' : config['port'], \
		'protocol' : config['protocol']\
		}], \
		wildmasks = [config['wildmask']], \
		resources = [{'type' : config['type'], \
        'default_pool_name' : config['default_pool_name']}], \
        profiles = [[{'profile_context' : config['profile_context'], 'profile_name' : config['profile_name']}]] \
		)

#Enables pool member
def enable_pool_member(b):
    b.LocalLB.Pool.set_member_session_enabled_state(config['vip_name'], [[{'address' : config['ip_address'], 'port' : config['port']}]], session_states = [config['state']])
    
#Disables pool Member
def disable_pool_member(b):
    b.LocalLB.Pool.set_member_session_enabled_state(config['vip_name'], [[{'address' : config['ip_address'], 'port' : config['port']}]], session_states = [config['state']])

#Adds one or multiple members to one or many pools
def add_members_to_pool(b):
    pass

#Deletes all pools and their information
def delete_all_pools(b):
    lb.LocalLB.Pool.delete_all_pools()
    print("All Pools have been deleted.")
    
#Deletes Specified pools and all of their information
def delete_specified_pools(b):
    b.LocalLB.Pool.delete_pool(pool_names = config['list_of_pools'])
    
#Returns a list of pools and their members
def get_list_of_pools(b):
    pool_lists = b.LocalLB.Pool.get_list()
    print(pool_lists)

def create_a_pool(b):
	#Look at config['load_balancing_method'] because it is already an array, and it might not have to be an array inside of an array
    #Loop Thru config['load_balancing_method'] for the one being used. or specify
    lb_method = ''
    b.LocalLB.Pool.create_v2([config['pool_name']],[config['load_balancing_method'],[[{'port': config['port'], 'address' : config['ip_address']}]])
    print("Successfully created %s with Load Balancing Method: %s, IP Address: %s, and Port Number: " ,config['pool_name'], lb_method, config['ip_address'], config['port'])

def main(options):
    #Start the session with the host
    b = bigsuds.BIGIP(hostname = hostname)

	#Hostname
    hostname = config['f5_hostname']
    
    #Fix parameters of everything
    if options.add_pool_member:
        add_members_to_pool(b)
    elif options.create_a_vip:
        create_a_vip(b)
    elif options.enable_pool_member:
        enable_pool_member(b)
    elif options.disable_pool_member:
        disable_pool_member(b)
    elif options.delete_all_pools:
        delete_all_pools(b)
    elif options.delete_specified_pool:
    	delete_specified_pools(b)
    elif options.create_a_pool:
        create_a_pool(b)
    elif options.get_list_pools:
        get_list_of_pools(b)
    elif options.add_pool_members:
        get_list_of_pools(b)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("--apm", action = "store_true", dest= "add_pool_member", help = "Add Pool Member")
    parser.add_option("--cv", action = "store_true", dest = "create_a_vip", help = "Create a VIP")
    parser.add_option("--ep", action = "store_true", dest = "enable_pool_member", help = "Enable Pool Member")
    parser.add_option("--dp", action = "store_true", dest = "disable_pool_member", help = "Disable Pool Member")
    parser.add_option("--dap", action = "store_true", dest = "delete_all_pools", help = "Delete All Pools")
    parser.add_option("--dsp", action = "store_true", dest = "delete_specified_pool", help = "Delete Specified Pools")
    parser.add_option("--cp", action = "store_true", dest = "create_a_pool", help = "Create a Pool")
    parser.add_option("--l", action = "store_true", dest = "get_list_pools", help = "Get List of Pools and Members")
    parser.add_option("--atp", action = "store_true", dest = "add_pool_members", help = "Add members to pool")

    (options, args) = parser.parse_args()

    main(options)