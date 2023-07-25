# Odin SDK for Python

The Odin SDK for Python allows you to easily interact with the Odin API and access various cybersecurity services, certificate information, and more.

## Installation

To use the Odin SDK in your Python project, you need to install it using pip:

```bash
pip install odin-cyble
```
## Usage

Import the package into your Go code and create an instance of the `odin.APIClient` by providing the base API URL and your API key:
```python
from odin.odin_client import OdinClient

client = OdinClient("https://api.getodin.com/v1", "<APIKey>")
```

## Examples

In the "example.py", you can find various usage examples demonstrating how to interact with the Odin API using the `odin-sdk` package.

Each example is a standalone Go program that showcases specific functionalities of the SDK.

```
# Example for using get_certificate_count
def ex_certificate_count():
    try:
        response = client.get_certificate_count("string")
        print(response.success)
        print(response.data.count)
    except APIException as e:
        print(e.status_code)
        print(e.message)
```

Make sure to replace `<APIKey>` with your actual Odin API key. 


Thank you for using the Odin SDK for Go. If you encounter any issues, find a bug, or want to contribute, feel free to open an issue or submit a pull request. Your feedback and contributions are highly appreciated!

For more information about our other projects and services, visit our website at https://www.getodin.com.