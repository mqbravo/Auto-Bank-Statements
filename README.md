# Automatic bank statements extractor and analyzer

With this project you will be able to automatically extract, store and analyze monthly statements via the extensible extraction from any bank source!

## Built with

This project was built using the following frameworks and technologies:

- Python
- MySQL
- Hadoop (TBD)
- Hive (TBD)
- Apache Airflow (TBD)

## Environment creation

This section contains the details of the creation of the development environment. **Note:** This guide assumes a Linux system is used, specifically, a Debian based (e.g. Ubuntu).

### MySQL

#### MySQL Installation

To install MySQL server run the following commands. Do note again that this is for a Debian based distro.

```bash
sudo apt-get update
sudo apt-get install mysql-server
```

**(Tip)** If an installation helper doesn't show up, issue the following command:

```bash
sudo mysql_secure_installation utility
```

#### Starting the server

To start the server run

```bash
sudo systemctl start mysql
```

**(Recommended)** If you want to start the server on startup, run:

```bash
sudo systemctl enable mysql
```

#### Accessing server instance

Now that MySQL is installed, you can access the CLI. Use the password you set in the installation step:

```bash
mysql -u root -p
```

You will see the prompt changed to `mysql>`, to exit, run:

```bash
quit
```

For more settings such as port configuration, remote access and more visit the useful links section below.

#### Database creation

From the root of the project (not in MySQL) run:

```bash
mysql -u root -p < database/mysql/DB_Creation.sql
```

**(Optional)** Run the following command to populate the DB. Change the values accordingly.

```bash
mysql -u root -p < database/mysql/DB_Populate.sql
```

## Python

### Python Installation

You can install Python with apt or from source (see useful links section)

Using the easier way (apt) run:

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.9
```

Verify the installation using

```bash
python3 --version
```

### Environment

This project uses PyPi as the package index, create an virtual environment anywhere using:

```bash
python3 -m venv <virtual_env_name>
```

Access the environment using:

```bash
source <virtual_env_name>/bin/activate
```

Finally, from the project's root, install the packages:

```bash
pip3 install -r requirements.txt
```

## Useful links

- [MySQL Installation Guide](<https://docs.rackspace.com/support/how-to/install-mysql-server-on-the-ubuntu-operating-system/>)
- [Python Installation Guide](<https://phoenixnap.com/kb/how-to-install-python-3-ubuntu>)
- <https://phoenixnap.com/kb/install-hive-on-ubuntu>
- <https://phoenixnap.com/kb/install-hadoop-ubuntu>
