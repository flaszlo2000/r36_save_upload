# Simple file uploader for the R36S

This little program was designed for the R36S console to share save files without removing the SD card.  
Out of the box it works with discord's webhooks which can help syncing saves between multiple devices.

## What does it do?
It grabs the latest save file from a given folder and sends it to a webhook url.

## How to install
How to add your own programs to the R36S: [dov's repo](https://github.com/dov/r36s-programming)   
<sub><sub>(little addition for it's ssh's fifth point: use vim instead :D )</sub></sub>
```
git clone https://github.com/flaszlo2000/r36_save_upload.git
cd r36_save_upload
touch config.json
python3 -m venv ./venv
pip3 install -r ./requirements.txt
python3 ./main.py
```

### If you have downloading errors
I encountered an error when I was able to connect to the device but couldn't pull from git. While git's error message wasn't really helpful, wget's was: `wget google.com` resulted this:

```
--2025-10-22 19:57:10--  http://google.com/
Resolving google.com (google.com)... failed: Temporary failure in name resolution.
wget: unable to resolve host address ‘google.com’
```

It's a DNS error!  
I don't know if this is a common error or not but here is -a temporary- fix:  
Change `/etc/resolv.conf`'s first line that was something like this for me: `nameserver 127.0.0.XX` to `nameserver 8.8.8.8` (google's dns).  
This will fix git and wget as well.

## Config
```
{
    "webhook_url": "YOUR_WEBHOOK_URL_COMES_HERE",
    "save_folder_path_str": "/ABSOLUTE_PATH/OF/THE_FOLDER/WHERE_YOUR_SAVE_FILES_LIVE",
    "save_file_extension": "FILE_EXTENSION"
}
```

Example configuration to sync the latest gb save on TF2:

```
{
    "webhook_url": "YOUR_WEBHOOK_URL_COMES_HERE",
    "save_folder_path_str": "/roms2/gb/Gambatte",
    "save_file_extension": "srm"
}
```

## Additional info
As for today's date (22.10.2025) the python version on the device is 3.7.5, be aware of this.

## TODO
- Visual folder and file picker
- Multiple file sending
