#Philip Middleton
#Create Load Balancing Pool with x members
#NOTE:  BigSuds creating and adding a pool with members does not prompt for authentication
#		which can be seen as a huge security flaw, as long as you have the F5 hostname, it will work

import bigsuds

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
#						Examples include: LB_METHOD_LEAST_SESSIONS, LB_METHOD_ROUND_ROBIN, LB_METHOD_LEAST_CONNECTIONS_NODE etc.
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
	
def main():
	list_of_pools_to_delete = []

	#Get the name of the host that we are working with, this is the F5 Machine
	f5_hostname = raw_input("Please enter F5 hostname or IP address")
	
	#Start the session with the Host
	b = bigsuds.BIGIP(hostname = f5_hostname)

	#Check the list of pools
	list = get_list_of_pools(f5_hostname,b)
	print(list)

	#To create a pool
	#create_a_pool(b)
	list = get_list_of_pools(f5_hostname,b)
	print(list)

	#Delete all pool
	#delete_all_pool(b)
	list = get_list_of_pools(f5_hostname,b)
	print(list)

	#Delete a pool
	pool_name = raw_input("Please enter the pool name you want to delete: ")
	list_of_pools_to_delete.append(pool_name)
	delete_a_pool(list_of_pools_to_delete,b)
	list = get_list_of_pools(f5_hostname,b)
	print(list)

	

if __name__ == '__main__':
	main()