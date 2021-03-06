config = {
	#Set the F5 Server Host Name
	'f5_hostname' : '',

	#Set common variables for pool/member actions
	'vip_name' : '',
	'ip_address' : '',
	'port' : '',
	'protocol' : '',
	'wildmask' : '',
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
	],

	#List of Pools
	'list_of_pools' : [''],

	#Create Template Settings
	'template_name' : '',
	'template_type' : 'TTYPE_HTTP', #if only using ping/get for the health chekc use TTYPE_HTTP
 	'parent_template' : 'http', #If only using ping/get for the health check use http
	'interval' : '',
	'timeout': '',
	'tempalte_address_type' : 'ATYPE_UNSET',
	'template_address' : '0.0.0.0',
	'template_port' : long(80),
	'template_is_read_only' : '', #True or False
	'template_is_directly_readable' : '', #True or False

	#Assign Template Settings
	'assing_template_name' : '',
	'assign_address_type' : 'ATYPE_STAR_ADDRESS_STAR_PORT', #Leave this
	'assign_address' : '',
	'assign_port' : '' #Make sure this is a long(port_number)

}