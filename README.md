# INFO801
project for the software architecture course

to run this project, install the dependencies first :


# python modules :
    sudo apt-get install memcached python-memcache

# memcached :

The Windows client can be found here : 
    * win32: http://downloads.northscale.com/memcached-win32-1.4.4-14.zip
    * win64: http://downloads.northscale.com/memcached-win64-1.4.4-14.zip

You'll need to install it from an elevated command prompt :
    c:\memcached\memcached.exe -d install (replace with actual location of your exe file)

Then, to start/stop the service : 
    c:\memcached\memcached.exe -d start
    c:\memcached\memcached.exe -d stop

By default the port for the sever will be 11211



