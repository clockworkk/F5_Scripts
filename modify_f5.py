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
    pass

def disable_pool_member(b):
    pass

def add_members_to_pool(b):
    pass

def delete_all_pools(b):
    pass

def delete_specified_pools(b):
    pass

def get_list_of_pools(b):
    pass

def create_a_pool(b):
    pass

def main(options):
    #Start the session with the host
    b = bigsuds.BIGIP(hostname = hostname)

    #options.insert_help

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
        disable_pool_member(b):
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

if __name__ = '__main__':
    parser = OptionParser()
    parser.add_option("-apm", action = "store_true", dest= "add_pool_member", help = "Add Pool Member")
    parser.add_option("-cv", action = "store_true", dest = "create_a_vip", help = "Create a VIP")
    parser.add_option("-ep", action = "store_true", dest = "enable_pool_member", help = "Enable Pool Member")
    parser.add_option("-dp", action = "store_true", dest = "disable_pool_member", help = "Disable Pool Member")
    parser.add_option("-dap", action = "store_true", dest = "delete_all_pools", help = "Delete All Pools")
    parser.add_option("-dsp", action = "store_true", dest = "delete_specified_pool", help = "Delete Specified Pools")
    parser.add_option("-cp", action = "store_true", dest = "create_a_pool", help = "Create a Pool")
    paresr.add_option("-l", action = "store_true", dest = "get_list_pools", help = "Get List of Pools and Members")
    parser.add_option("-atp", action = "store_true", dest = "add_pool_members", help = "Add members to pool")

    (options, args) = parser.parse_args()

	main(options)