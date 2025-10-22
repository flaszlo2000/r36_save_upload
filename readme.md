# Simple file uploader for the R36S

This little program was designed for the R36S console to share save files without removing the SD card.  
This can help syncing saves between multiple devices.


## What does it do?
It grabs the latest save file from a given folder and sends it to a webhook url.

## How to install
How to add your own programs to the R36S: [dov's repo](https://github.com/dov/r36s-programming)  

```
git clone https://github.com/flaszlo2000/r36_save_upload.git  
cd r36_save_upload  
touch config.json  
pip install -r ./requirements.txt  
python3 ./main.py
```

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

## TODO
- Visual folder and file picker
- Multiple file sending
