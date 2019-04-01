"""Example: Find all servers per group"""

from cbw_api_toolbox.cbw_api import CBWApi

API_KEY = ''
SECRET_KEY = ''
API_URL = ''

CLIENT = CBWApi(API_URL, API_KEY, SECRET_KEY)

CLIENT.ping()

SERVERS = CLIENT.get_detailed_servers()

CATEGORY_BY_GROUPS = {}

# append each server to a group by category dict
for server in SERVERS:
    if server and server.groups:
        for group in server.groups:
            if group.name not in CATEGORY_BY_GROUPS:
                CATEGORY_BY_GROUPS[group.name] = {}

            concerned_group = CATEGORY_BY_GROUPS[group.name]

            if server.category not in concerned_group:
                concerned_group[server.category] = []

            concerned_group[server.category].append(server)

for group in CATEGORY_BY_GROUPS:
    print("--- GROUP : {0} ---".format(group))

    for category in CATEGORY_BY_GROUPS[group]:
        print("** CATEGORY : {0} **".format(category))

        for computer in CATEGORY_BY_GROUPS[group][category]:
            print("{0} with hostname : {1}".format(category, computer.hostname))