Introduction
------------

This module aim to prepare an .ipa file for distribution in an HTTPS server.  

It will create a .plist and .html files.  
Afterwards, these files should be stored in a server (together with the .ipa file) to be downloaded from an iPad or iPhone.

## Installation
Install via pip:

    pip install os-ios-prepare-ipa-file

## Usage:


```python
from os_ios_prepare_ipa_file import ipa_preparer as ip

ip.prepare_ipa_file(ipa_file_path="path/to/ipa_file.ipa",
                    ipa_file_path_in_server= "www.my_website.com/storage/ipa_file.ipa",
                    html_file_path_in_server="www.my_website.com/pages/download_latest_version/download.html",
                    bundle_identifier="com.app.bundleidentifier",
                    app_name="MyAppName")
```

That's it. 




## Links
[GitHub - osapps](https://github.com/osfunapps)

[GitHub - os-android-app-automation](https://github.com/osfunapps/os-android-app-automation-py)

## Licence
ISC