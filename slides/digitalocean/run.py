token = os.environ['DO_SECRET_KEY']
manager = digitalocean.Manager(token=token)
keys = manager.get_all_sshkeys()

for i in []
droplet = digitalocean.Droplet(token=token,
                               name="indycode-%s"%i,
                               region='ams3', # Amster
                               image='ubuntu-14-04-x64', # Ubuntu 14.04 x64
                               size_slug='512mb',  # 512MB
                               ssh_keys=keys, #Automatic conversion
                               backups=False)
droplet.create()