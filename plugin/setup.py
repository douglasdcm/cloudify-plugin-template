########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.


from setuptools import setup

# Replace the place holders with values for your project

setup(

    # Do not use underscores in the plugin name.
    # The name of the egg-info file (the package name)
    name='custom-plugin-test-stp-name',
    version='1.0',
    author='John Doe',
    author_email='jdoe@mail.com',
    description='Demo plugin',

    # This must correspond to the actual packages in the plugin.
    # This is the folder to be built
    packages=['custom-plugin-test'],

    license='LICENSE',
    zip_safe=False,
    install_requires=[
        # Necessary dependency for developing plugins, do not remove!
        "cloudify-common>=5.0.5.1"
    ]
)
