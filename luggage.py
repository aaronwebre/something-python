def packer(name=None, **kwargs):
    print(kwargs)

def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name!")

packer(name="Aaron", num=13, something_else=None)
unpacker(**{"last_name": "Webre", "first_name": "Aaron"})
