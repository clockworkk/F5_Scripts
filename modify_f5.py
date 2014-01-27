#!/usr/bin/env python
#Philip Middleton
#Create, Modify, and Delete: VIPs, Pools, and Pool Members

import bigsuds
from config import config
from optparse import OptionParser

#Global Variables
hostname = config['f5_hostname']    
b = bigsuds.BIGIP(hostname = hostname)


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
    b.LocalLB.Pool.delete_all_pools()
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
    b.LocalLB.Pool.create_v2([config['pool_name']],config['load_balancing_method'],[[{'port': config['port'], 'address' : config['ip_address']}]])
    print("Successfully created %s with Load Balancing Method: %s, IP Address: %s, and Port Number: %s" ,config['pool_name'], lb_method, config['ip_address'], config['port'])

#Prints the current list of templates, user created templates are at the bottom of the list by default
def get_hc_templates(b):
    current_templates = b.LocalLB.Monitor.get_template_list()
    print(current_templates)

#Templates run on interval times, so there is no need to call it into action, just assign a template to a pool
def create_hc_template(b):
    #wildly insane paramters to create a template
    template_attributes = { 
        'parent_template' : config['parent_template'], #This is the parent template of the example
        'interval' : config['interval'], #This is a time in seconds
        'timeout': config['timeout'], #This is a time in seconds
        'dest_ipport' : { 'address_type' : config['template_address_type'], 'ipport' : { 'address' : config['template_address'], 'port' : config['template_port']}}, 
        'is_read_only' : config['template_is_read_only'], 
        'is_directly_usable' : config['template_is_directly_usable']
    }    

    #ping_test is the name of the template
    #use TTYPE_HTTP
    template_name = {
        'template_name': config['template_name'], 
        'template_type': config['template_type']
    }

    #Creates a HTTP template that sends a GET ping to all of the address in whatever pool you assign it to
    #Should be a replica of the email that was sent to me prior
    b.LocalLB.Monitor.create_template([template_name], [template_type])

#Sets the destination IP:port values for the specified templates. 
#NOTE: This should only be done when the monitor templates in "template_names" have NOT been associated to any node addresses or pool members. 

#So in the API theres a couple of different functions that could potentially be used, and each outside the scope of my realm
#Pool.set_member_monitor_rule
#Monitor.set_template_destination - Figured out mehh

#This will be in the event of Monitor.set_template_destination
def assign_template(b):
    #insert template names in place of ping_test
    #Obviously can move any hard_coded variables here

    destination = {
        'address_type': config['assign_address_type'],
        'ipport': {'address': config['assign_address'], 'port': config['assign_port']}
        }

    template_names = [config['assign_template_name']]

    b.LocalLB.Monitor.set_template_destination([template_names], [destinations])
    print("Template %s assigned to member at IP: %s" % template_names[0], destination['ipport'])

#Main: takes the options and runs the correct definition
def main(options):
    
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
    elif options.create_hc_template:
        create_hc_template(b)
    elif options.get_hc_templates:
        get_hc_templates(b)
    elif set_template_destination:
        set_template_destination(b)

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("--apm", action = "store_true", dest= "add_pool_member", help = "Add Pool Member, can add many members to many pools")
    parser.add_option("--cv", action = "store_true", dest = "create_a_vip", help = "Create a VIP")
    parser.add_option("--ep", action = "store_true", dest = "enable_pool_member", help = "Enable Pool Member")
    parser.add_option("--dp", action = "store_true", dest = "disable_pool_member", help = "Disable Pool Member")
    parser.add_option("--dap", action = "store_true", dest = "delete_all_pools", help = "Delete All Pools")
    parser.add_option("--dsp", action = "store_true", dest = "delete_specified_pool", help = "Delete Specified Pools")
    parser.add_option("--cp", action = "store_true", dest = "create_a_pool", help = "Create a Pool")
    parser.add_option("--l", action = "store_true", dest = "get_list_pools", help = "Get List of Pools and Members")
    parser.add_option("--atp", action = "store_true", dest = "add_pool_members", help = "Add members to pool")
    parser.add_option("--ct", action = "store_true", dest = "create_hc_template", help = "Create a Health Check Template")
    parser.add_option("--gt", action = "store_true", dest = "get_hc_templates", help = "Get current Health Check Templates")
    parser.add_option("--st", action = "store_true", dest = "set_template_destination", help = "Set Template Destination")

    (options, args) = parser.parse_args()

    main(options)