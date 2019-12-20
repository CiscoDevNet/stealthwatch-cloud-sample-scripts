# Stealthwatch Cloud API Sample Scripts
This repository contains sample Python scripts related to Cisco Stealthwatch Cloud APIs. It is available for use by the Cisco DevNet community through Code Exchange.
For more information on the Stealthwatch Cloud REST API, please see the following link: https://developer.cisco.com/docs/stealthwatch-cloud

## Installation
1. Ensure Python 3 is installed.
   * To download and install Python 3, please visit https://www.python.org.
2. Ensure the Python `requests` module is installed.
   * For more information on the Python `requests` module, please visit https://pypi.org/project/requests/.
3. Download the `.py` files located in the [python](python) directory.

*Alternatively, advanced users can also use git to checkout / clone this project.*

## Configuration
Open the desired `.py` file that you intend to run and enter the following values where specified:
* `PORTAL_URL = ""`
* `API_USER = ""`
* `API_KEY = ""`

*(Note: additional fields may also be required)*

#### **Obtaining API Credentials**
To obtain API credentials for Stealthwatch Cloud, please do the following:

* Login to your Stealthwatch Cloud portal
    * For a free 60-day trial of Stealthwatch Cloud, please visit: https://www.cisco.com/c/en/us/products/security/stealthwatch/stealthwatch-cloud-free-offer.html
* Click the *User* icon in the top-right corner, and select `Your Settings`
* Click the button to `Generate New Key`
* An API `key` will be created and associated for the `user` listed

## Usage
<!--
Show users how to use the code. Be specific. Use appropriate formatting when showing code snippets or command line output. If a particular [DevNet Sandbox](https://developer.cisco.com/sandbox/) or [Learning Lab](https://developer.cisco.com/learning-labs/) can be used in to provide a network or other resources to be used with this code, call that out here.
-->
1. Identify the path to your Python 3 executible. 
    * Depending how Python 3 was installed, this might be as simple as just calling the command `python` or `python3`.
2. Run the Python script with the following command:
    * `$ <PYTHON-PATH> <PYTHON-SCRIPT-PATH>`
    * Example: `$ /usr/bin/python ./get_alerts.py`

## Known issues
No known issues.

## Getting help
Use this project at your own risk (support not provided). *If you need technical support with Cisco Stealthwatch APIs, do one of the following:*

#### Browse the Forum
Check out our [forum](https://community.cisco.com/t5/custom/page/page-id/customFilteredByMultiLabel?board=j-disc-dev-security&labels=stealthwatch) to pose a question or to see if any questions have already been answered by our community. We monitor these forums on a best effort basis and will periodically post answers. 

#### Open A Case
* To open a case by web: http://www.cisco.com/c/en/us/support/index.html
* To open a case by email: tac@cisco.com 
* For phone support: 1-800-553-2447 (U.S.)
* For worldwide support numbers: www.cisco.com/en/US/partner/support/tsd_cisco_worldwide_contacts.html
* *If you don't have a Cisco service contract, send an email to swatchc-support@cisco.com describing your problem.*

## Getting involved
Contributions to this code are welcome and appreciated. See [CONTRIBUTING](CONTRIBUTING.md) for details. Please adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) at all times.

## Licensing info
This code is licensed under the BSD 3-Clause License. See [LICENSE](LICENSE) for details. 

