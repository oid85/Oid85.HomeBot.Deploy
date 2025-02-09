import oid85_homebot
import oid85_homebot_resource_store

if __name__ == '__main__':
    switcher = 3

    if switcher == 1:
        oid85_homebot.deploy()

    if switcher == 3:
        oid85_homebot_resource_store.deploy()
