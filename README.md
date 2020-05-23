# BOT API

This is a boot find a message at MongoDB, after send at Whatsapp


## REQUIRIMENTS for Windows 10

### Is madatory to run this project with mongoDB
#### At the near future I will add a new version with a mongo in docker configuration
For configure the database variables uncomment in main.py the line 5 and the follow code:

```
config = ConfigParser()
config["MONGO"] = { "host":"$host$",
                    "port":"$port$",
                    "username":"$username$",
                    "password":"$password$",
                    "authSource":"$authSource$",
                    "db":"$db$",
                    "collection":"$collection$"}
with open('./mongo.conf', 'w') as configfile:
    config.write(configfile)
```

After set your database configurations and run python main.py, right after close and comment again.

### To run the project is necessary use python 3.6.+ and the pip installed

You did run :

```
    pip install requirements.txt
```

With this, all libs will be instaled

### Boot run in chrome at version 81.0.4044.138 using the chomedriver.exe



## Run the project

After install requirements run main.py 

```
    python  main.py
```

## Use BOT

After start bot, you need scan QRcode of webwhatsapp and left the chrome open.
The bot will find mesages at database and send to contacts.