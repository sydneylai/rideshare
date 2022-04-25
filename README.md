# rideshare


## ridesharing-matching
In this sample project, we will create a decentralized database matching drivers and passengers based on their matching zip codes in their metro area.

MVP: Showcase publishing and subscribing within the terminal by creating the json files for the passengers and drivers.

## This project is divided into three distinct parts:

### Decentralized matching of passengers and drivers
1. Create a json file for each driver and each passenger
2. Matching the driver and passengers with the IPFS pubsub method via curl commands in the terminal to showcase peer to peer to matching

How to Use:

These json files require less code than a traditional python file with a centralized database. Every passenger would have their own JSON (JSON formmated payloads) file, so if this app had 20M passengers there would be 20M JSON files. So here you can see another perspective of having a decentralized database because you would need 20M individual JSON files rather than having 20M rows in a single database.

1. Create a Topic as a JSON file

2. Create a Passenger File

3. Create a Driver File

4. Publish passenger file to passenger topic

5. Publish driver file to driver topic

6. Subscribe to passenger topic to get location

At this point I've created JSON files for Passengers and Drivers.


### Create a database as an end point

How to Use:
1. Install the IPFS https://docs.ipfs.io/install/command-line/#official-distributions Once IPFS is installed you can call the daemon from the Command Line.

2. To store Drivers and Passengers, each profile would be json files in IPFS. - List of Drivers with zip codes as a file - List of Passengers with zip codes as a file Every file would be published with a curl command to the local host 127001. Each driver/passenger would publish their own request, and pull each other's profiles. Each file would be their own driver/passenger profile.

3. Start the daemon - Installing the IPFS is like building the post-office. Publishing a JSON file would be putting a letter in the mail.



#### Create a Topic and Publish


How to Use: 

1. Create a topic 

2. sub to the topic ```ipfs pubsub passengers```

3. publish to a topic ```ipfs pubsub pub passengers passengers/passenger1.json```

4. Publish to a Driver Topic

5. sub to the topic ```ipfs pubsub drivers```

6. publish to a topic ```ipfs pubsub pub drivers drivers/driver1.json```

## Credits

Official distributions https://docs.ipfs.io/install/command-line/#official-distributions
ipfs pubsub https://docs.ipfs.io/reference/cli/#ipfs-pubsub
ipfs pubsub Is https://docs.ipfs.io/reference/cli/#ipfs-pubsub-ls
