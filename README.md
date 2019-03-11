# TCP_Pickle
Use TCP to coordinate between a host and a server. The host will send a pickled object and the python source to the server. The server will run the python source with the pickle and return the results.

Be sure to use the same port. Execute pickleHost.py after executing pickleServer.py. The recieved message should be "4".
