config = {
	#Set the F5 Server Host Name
	'f5_hostname' : '',

	#Set common variables for pool/member actions
	'vip_name' : '',
	'ip_address' : '',
	'port' : '',
	'protocol' : '',
	'wildmask': '',
	'pool_name' : '',

	#Resources to be used
	'type' : '', #RESOURCE_TYPE_POOL
	'default_pool_name' : '', #'/Common/POOL_NAME'

	#Profiles to use
	'profile_context' : '', #'PROFILE_CONTEXT_TYPE_ALL'
	'profile_name' : '', #"/Common/PROFILE_NAME" example, /Common/tcp

	#Enable and Disable Value
	#STATE ENABLED or STATE_DISABLED
	'state' : '',

	#Load Balancing Methods
	'load_balancing_method' : ['LB_METHOD_LEAST_SESSIONS', 
	'LB_METHOD_ROUND_ROBIN', 
	'LB_METHOD_LEAST_CONNECTIONS_NODE', 
	'LB_METHOD_RATIO_MEMBER', 
	'LB_METHOD_LEAST_CONNECTION_MEMBER', 
	'LB_METHOD_OBSERVED_MEMBER', 
	'LB_METHOD_PREDICTIVE_MEMBER', 
	'LB_METHOD_RATIO_NODE_ADDRESS',
	'LB_METHOD_LEAST_CONNECTION_NODE_ADDRESS',
	'LB_METHOD_FASTEST_NODE_ADDRESS',
	'LB_METHOD_OBSERVED_NODE_ADDRESS',
	'LB_METHOD_PREDICTIVE_NODE_ADDRESS',
	'LB_METHOD_DYNAMIC_RATIO',
	'LB_METHOD_FASTEST_APP_RESPONSE',
	'LB_METHOD_LEAST_SESSIONS',
	'LB_METHOD_DYNAMIC_RATIO_MEMBER',
	'LB_METHOD_L3_ADDR',
	'LB_METHOD_UNKOWN',
	'LB_METHOD_WEIGHTED_LEAST_CONNECTION_MEMBER',
	'LB_METHOD_WEIGHTED_LEAST_CONNECTION_NODE_ADDRESS',
	'LB_METHOD_RATIO_SESSION',
	'LB_METHOD_RATIO_LEAST_CONNECTION_MEMBER',
	'LB_METHOD_RATIO_LEAST_CONNECTION_NODE_ADDRESS'
	]

	#List of Pools
	'list_of_pools' : []
}