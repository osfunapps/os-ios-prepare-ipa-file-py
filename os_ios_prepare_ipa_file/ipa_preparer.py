import os.path

from os_file_stream_handler import file_stream_handler as fsh
from os_file_handler import file_handler as fh


def prepare_ipa_file(ipa_file_path,
                     ipa_file_path_in_server,
                     html_file_path_in_server,
                     bundle_identifier,
                     app_name):
    """
    Will prepare an .ipa file for distribution. Which means:

    1) Create a .plist file
    2) Create an .html file

    Args:
        ipa_file_path: the path to your ipa file
        ipa_file_path_in_server: the path of the .ipa file in your server
        html_file_path_in_server: the path of the .html file in your server
        bundle_identifier: the app's bundle identifier
        app_name: the app's name
    """

    # gather resources
    ipa_file_name = fh.get_file_name_from_path(ipa_file_path, with_extension=False)
    parent_path = fh.get_parent_path(ipa_file_path)
    output_path = os.path.join(parent_path, ipa_file_name)

    # create an output path
    fh.create_dir(output_path)

    output_html_file_path = os.path.join(output_path, f'{ipa_file_name}.html')
    output_plist_file_path = os.path.join(output_path, f'{ipa_file_name}.plist')
    output_ipa_file_path = os.path.join(output_path, f'{ipa_file_name}.ipa')
    fh.copy_file("../res/dummy_html.html", output_html_file_path)
    fh.copy_file("../res/dummy_plist.plist", output_plist_file_path)
    fh.copy_file(ipa_file_path, output_ipa_file_path)

    fsh.replace_text_in_file(output_html_file_path, output_html_file_path, "$https_plist_file_path", html_file_path_in_server)

    replace_dicts = {"$https_ipa_file_path": ipa_file_path_in_server,
                     "$bundle_identifier": bundle_identifier,
                     "$app_title": app_name}
    fsh.replace_texts_in_file(output_plist_file_path, output_plist_file_path, replace_dicts)
