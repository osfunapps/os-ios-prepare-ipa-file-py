
from os_ios_prepare_ipa_file import ipa_preparer as ip

ip.prepare_ipa_file(ipa_file_path="path/to/ipa_file.ipa",
                    ipa_file_path_in_server= "www.my_website.com/storage/ipa_file.ipa",
                    html_file_path_in_server="www.my_website.com/pages/download_latest_version/download.html",
                    bundle_identifier="com.app.bundleidentifier",
                    app_name="MyAppName")