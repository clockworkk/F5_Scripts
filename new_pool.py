#Philip Middleton
#Create Load Balancing Pool with x members
#NOTE:  BigSuds creating and adding a pool with members does not prompt for authentication
#		which can be seen as a huge security flaw, as long as you have the F5 hostname, it will work

import bigsuds

#Configuration:
#Creating a VIP
configurations = [
		{
			#F5 HOST NAME
			'f5_hostname' : ''
		}
		{
			#General information
			'name' : '/Common/vip_name',
			'address' : 'IP ADDRESS',
			'port' : 'port_address',
			'protocol' : 'PROTOCOL'
		}
		{
			#wildmask
			'wildmasks' = 'WILDMASK_ADDRESS'
		}
		{
			#Resources to be used
			'type' : 'RESOURCE_TYPE_POOL',
			'default_pool_name' : '/Common/POOL_NAME'
		}
		{
			#Profiles to use
			'profile_context' : 'PROFILE_CONTEXT_TYPE_ALL',
			'profile_name' : '/Common/PROFILE_NAME' #example, /Common/tcp
		}
		{
			#Enable and Disable Pool Member:
			#STATE_ENABLED or STATE_DISABLED
			'state' : 'VALUE'
		}
		{
			#Load Balancing Methods	
			#Not Sure best way to do this.
	]
			



# Create a VIP
# definitions
# wildmask
# Resources
# Profiles
def create_a_vip(b):
	#Change for user input maybe? or possibly options with arguments?
	b.LocalLB.VirtualServer.create( \
	definitions = [{'name': '/Common/vip11', 'address': '11.1.1.1', 'port': 80, 'protocol': 'PROTOCOL_TCP'}], \
	wildmasks = ['255.255.255.255'], \
	resources = [{'type': 'RESOURCE_TYPE_POOL', 'default_pool_name': '/Common/testpool'}], \
	profiles = [[{'profile_context': 'PROFILE_CONTEXT_TYPE_ALL', 'profile_name': '/Common/tcp'}]] \
	)

#Disable a pools members
def enable_pool_member(b):
	#replace hard coded values with variables, dictionaries, and arrays, tested this in python, and worked.
	#array[0] = STATE_ENABLED
	b.LocalLB.Pool.set_member_session_enabled_state(['test3'], [[{'address': '1.1.1.1', 'port': 88}]], session_states = [array])
	pass

#Disable a pools members
def disable_pool_member(b):
	#replace same as above
	#make array[0] = STATE_DISABLED
	b.LocalLB.Pool.set_member_session_enabled_state(['test3'], [[{'address': '1.1.1.1', 'port': 88}]], session_states = [array])
	pass

#Add members to a pool, can add to multiple pools
def add_members_to_pool(array_life,list_of_pool_names,b):
	#Same as above, change the hard coded values to variables, but this works as tested.
	b.LocalLB.Pool.set_member_session_enabled_state(['test3'], [[{'address': '1.1.1.1', 'port': 88}]])



#Delete pools, add pools to array, list_of_pools_to_delete, to delete more than one.
def delete_a_pool(list_of_pools_to_delete,b):
	b.LocalLB.Pool.delete_pool(pool_names = list_of_pools_to_delete)

#Delete All Pools
def delete_all_pool(b):
	b.LocalLB.Pool.delete_all_pools()

#Gets the list of the pools that currently exist for the F5 host listed.
def get_list_of_pools(f5_hostname,b):
	#Start bigip session with host
	pool_lists = b.LocalLB.Pool.get_list()
	return pool_lists

#Create a LTM Pool within F5
#pool_name - is the name of the LTM Pool
#Load_balancing_method - is the load balancing method that is going to be used:
#	Examples include: LB_METHOD_LEAST_SESSIONS, LB_METHOD_ROUND_ROBIN, LB_METHOD_LEAST_CONNECTIONS_NODE etc.
#address_of_member - is the IP address of the member that you are adding to the pool
#port_used - is the port that traffic will be on for the member of the pool that you are adding.
def create_a_pool(b):
	#start bigip session with host

	#For the time being get user input for variables
	#In the future switch to possibly using options
	pool_name = raw_input("Please enter the name of the pool that you want to create: ")
	load_balancing_method = raw_input("Please enter the load balancing method (LB_METHOND_ROUND_ROBIN): ")
	address_of_member = raw_input("Please enter the IP address of the new pool member: ")
	port_used = raw_input("Please enter the port that is being used: ")
	pool_name = "/Common/" + pool_name
	
	#Create the pool and add the members
	b.LocalLB.Pool.create_v2([pool_name],[load_balancing_method],[[{'port':port_used, 'address':address_of_member}]])

#Needs Testing
def retrieve_all_health_information(b):
	health_inforamtion = b.LocalLB.Pool.get_all_statistics()
	return health_information

#Needs Testing
def retrieve_specified_health_information(b):
	#get_all_member_statistics takes in an array of strings, which represent the specified pools that you would like to retrieve statistics for.
	specified_health_information = b.LocalLB.Pool.get_all_member_statistics()
	return specified_health_information

	
def main():
	list_of_pools_to_delete = []

	#Get the name of the host that we are working with, this is the F5 Machine
	f5_hostname = raw_input("Please enter F5 hostname or IP address: ")
	
	#Start the session with the Host
	b = bigsuds.BIGIP(hostname = f5_hostname)

	#Check the list of pools (works)
	list = get_list_of_pools(f5_hostname,b)
	print(list)

	#To create a pool (works)
	create_a_pool(b)
	list = get_list_of_pools(f5_hostname,b)
	print(list)

	#Delete all pools (works)
	delete_all_pool(b)
	list = get_list_of_pools(f5_hostname,b)
	print(list)

	##Delete a pool (works)
	pool_name = raw_input("Please enter the pool name you want to delete: ")
	list_of_pools_to_delete.append(pool_name)
	delete_a_pool(list_of_pools_to_delete,b)
	list = get_list_of_pools(f5_hostname,b)
	print(list)

	#Get all pool statistics
	retrieve_all_health_information(f5_hostname,b)

	#Add a member to a pool
	#list_of_pool_names = []
	#list_of_ports = []
	#list_of_members = []
	#array_life = []
	#x = "1.1.1.1"
	#y = 80
	#z = 'test'
	#y = long(y)
	#list_of_members.append(x)
	#list_of_members.append(y)
	#array_life.append(list_of_members)
	#add_members_to_pool(array_life,list_of_pool_names,b)

	#create_a_vip(b)
	

if __name__ == '__main__':
	main()
