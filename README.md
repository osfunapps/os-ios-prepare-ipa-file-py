Introduction
------------

This module aim to assist with an iOS/OSX app buildup.

To use, create an XML file with your app properties and run.

## Installation
Install via pip:

    pip install os-ios-app-automation

## Usage:

Will build an XCode project by a predefined xml file.

- [xml example 1](/example/example_1.xml):
```xml
<xcode_props>

    <!-- will hold all of the project properties -->
    <project_properties>
        <project_root>/path/to/xcode/project</project_root>
        <root_dir_name>my_root_dir_name</root_dir_name>
        <xcodeproj_file_name>my_root_dir_name.xcodeproj</xcodeproj_file_name>
        <bundle_identifier>com.mybundleid</bundle_identifier>
        <product_name>app name</product_name>

        <!-- toggle to call pod install -->
        <install_pods>true</install_pods>

        <!-- NOTICE: you will need to create a copy of the .plist file you want to use and set the path here. It will be copied to your project on startup -->
        <plist_path>$app_path/files/res/Info.plist</plist_path>

        <!-- the path to the AppIcon.appiconset directory, contains all of the logo files -->
        <app_icon.appiconset>$app_path/files/res/AppIcon.appiconset</app_icon.appiconset>
    </project_properties>

    <!-- the extensions of the added files (you don't need to add .plist or .swift)-->
    <added_files_extensions>
        <extension>.zip</extension>
        <extension>.xml</extension>
    </added_files_extensions>

    <!-- the next segment will divide the actions to steps -->

    <!-- first, in step one, we will unlink all of the previously used resources -->
    <step_1>

        <!-- remove a linked directory which was previously added-->
        <unlink type="dir" delete="false">my_root_dir_name/rel/path/to/dir</unlink>

        <!-- remove a linked file which was previously added-->
        <unlink type="file" delete="false">my_root_dir_name/GoogleService-Info.plist</unlink>
    </step_1>


    <!-- in step two, we will link all of the resources and files we want in the project-->
    <step_2>

        <!-- copy google services -->
        <link>
            <file_src path_type="search">

                <search_path>path/in/computer/to/look/for</search_path>
                <full_name>GoogleService-Info.plist</full_name>
            </file_src>

            <file_dst>
                <path>my_root_dir_name/GoogleService-Info.plist</path>
            </file_dst>
        </link>

         <!-- look for a directory in the computer and add it -->
        <link>
            <dir_src path_type="search">
                <search_path>path/in/computer/search</search_path>
                <full_name>dir_to_search</full_name>
            </dir_src>

            <dir_dst>
                <path>my_root_dir_name/Dynamic Resources/Main</path>
            </dir_dst>
        </link>

        <!-- copy a file -->
        <link>
            <dir_src>
                <path>path/to/text/file.txt</path>
            </dir_src>

            <dir_dst>
                <path>my_root_dir_name/Dynamic Resources/Main/copied_text_file.txt</path>
            </dir_dst>
        </link>


    </step_2>


    <!-- in step 3, we will add the pods and the frameworks -->
    <step_3>

        <!-- pods add -->
        <pods action="append">  <!-- set to 'clear_and_append' if you want to remove the old pods -->
            <pod_line>use_frameworks!</pod_line>
            <pod_line>platform :ios, '10.0'</pod_line>
            <pod_line>source 'https://github.com/CocoaPods/Specs.git'</pod_line>
            <pod_line>pod 'Zip', '~> 1.1'</pod_line>
            <pod_line>pod 'SWXMLHash', '~> 5.0.0'</pod_line>
        </pods>

        <!-- frameworks add -->
        <frameworks>

            <!-- custom framework-->
            <amazon_fling_framework>
                <path>path/to/amazon/fling.framework</path>
                <type>custom</type>
            </amazon_fling_framework>


            <!-- generic system frameworks-->
            <external_accesory>
                <path>ExternalAccessory.framework</path>
                <type>system</type>
            </external_accesory>

            <audio_toolbox>
                <path>AudioToolbox.framework</path>
                <type>system</type>
            </audio_toolbox>

            <store_kit>
                <path>StoreKit.framework</path>
                <type>system</type>
            </store_kit>


        </frameworks>

    </step_3>

    <!-- add more steps here... -->

</xcode_props>
```

After your created the xml file, call it from code, to build your XCode project.
```python
from os_ios_app_automation import app_automation as xm
 
xm.set_xcode_project_by_xml('/path/to/your/xml_file.xml',
                                place_holder_map = {'$app_path': '/path/to/a/dynamic/directory'})
```

## Advanced usage

You can also extend an XML file to another one. 

Inheritance in this sense can help you if you're interested in sharing a behaviour between a bunch of XML files.  

- [child xml](/example/example_2.xml):
```xml
<!-- this example shows how to extend an xcode_props file from another xcode_props file -->
<xcode_props extension_mapper_path="./shared_mapper.xml">

    <!-- will hold all of the project properties -->
    <project_properties>
        <bundle_identifier>com.my_identifier</bundle_identifier>
        <product_name>My cool app</product_name>
    </project_properties>

    <step_4>
        <pods action="append"><!-- we will set this <pods> to 'append' cause we want to add the pods to the pods we set initially, in the extension mapper file -->
            <pod_line>pod 'AnotherPod'</pod_line>
            <pod_line>pod 'AndAnotherPod'</pod_line>
        </pods>
    </step_4>


    <!-- the extended code will be implemented here during runtime -->
</xcode_props>
```


- [parent xml](/example/shared_mapper.xml):

```xml
 <!-- this is just an extension mapper to the example_2.xml file -->
<xcode_extension_props>

    <project_properties>
        <project_root>path/to/project/root</project_root>
        <root_dir_name>projects_root_dir_name</root_dir_name>
        <xcodeproj_file_name>projects_root_dir_name.xcodeproj</xcodeproj_file_name>
        <plist_path>$app_path/files/res/Info.plist</plist_path>
        <app_icon.appiconset>$app_path/files/res/AppIcon.appiconset</app_icon.appiconset>
    </project_properties>

    <!-- the extensions of the added files (you don't need to add .plist or .swift-->
    <added_files_extensions>
        <extension>.zip</extension>
        <extension>.xml</extension>
    </added_files_extensions>



    <!-- in step one, we will unlink all of the previously used resources -->
    <step_1>
        <unlink type="dir" delete="false">projects_root_dir_name/Dynamic Resources</unlink>
        <unlink type="file" delete="false">projects_root_dir_name/GoogleService-Info.plist</unlink>
    </step_1>

    <!-- in step 2, add pods and frameworks -->
    <step_2>
        <pods action="clear_and_append">
            <pod_line># reachability, to get wifi events</pod_line>
            <pod_line>use_frameworks!</pod_line>
            <pod_line># os libraries</pod_line>
            <pod_line>pod 'OsUIViews'</pod_line>
            <pod_line>pod 'OsTools'</pod_line>
        </pods>

        <frameworks>

            <!-- add some system frameworks (no need to add Pods_ framework here) -->
            <framework>
                <path>audiotoolbox.framework</path>
                <type>system</type>
            </framework>

            <framework>
                <path>externalaccessory.framework</path>
                <type>system</type>
            </framework>
            <framework>
                <path>storekit.framework</path>
                <type>system</type>
            </framework>
        </frameworks>

    </step_2>

    <!-- step 3 is an example of running an external text mapper to do additional changes. read about the text mappers to study more! -->
    <!-- in step 3 we will run the text mapper to do any changes in the project files (in this example, substitute texts) after we will set the project -->
    <step_3>
        <run_text_mapper>
            <file_src>
                <path>./path/to/text/mapper.xml</path>
            </file_src>

            <!-- if the text mapper file requires place holders, they will be set using the <arg> tags -->
            <!-- NOTICE: we can also pass place holder values, like so:
            <arg>
                    <key>$project_path</key>
                    <value>$project_path</value> - the $project_path value will be passed
            </arg>
            -->
            <place_holder_map>
                <arg>
                    <key>$project_path</key>
                    <value>path/to/project/root</value>
                </arg>
            </place_holder_map>
        </run_text_mapper>
    </step_3>


</xcode_extension_props>
```

That's it. 




## Links
[GitHub - osapps](https://github.com/osfunapps)

[GitHub - os-android-app-automation](https://github.com/osfunapps/os-android-app-automation-py)

## Licence
ISC