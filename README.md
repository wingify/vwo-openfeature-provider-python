## VWO OpenFeature Provider Python

[![PyPI version](https://badge.fury.io/py/vwo-openfeature-provider-python.svg)](https://pypi.org/project/vwo-openfeature-provider-python)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0)

## Requirements

* Works with Python: 3.8+

## Installation

It's recommended you use [virtualenv](https://virtualenv.pypa.io/en/latest/) to create isolated Python environments.

```bash
pip install vwo-openfeature-provider-python
```

## Usage

```python
from openfeature import api
from vwo_provider.vwo_provider import VWOProvider
from openfeature.evaluation_context import EvaluationContext
from vwo import init

options = {
    'sdk_key': '32-alpha-numeric-sdk-key', # SDK Key
    'account_id': '123456' # VWO Account ID
}

# Initialize the VWO client
vwo_client = init(options)

# Initialize the VWO provider
vwo_provider = VWOProvider(vwo_client)

# Registering the default provider
api.set_provider(vwo_provider)

# A client bound to the default provider
default_client = api.get_client()

def start():
    print('BOOL', default_client.get_boolean_value('unique_feature_key', False, EvaluationContext(attributes={'id': 'user_id', 'key': 'boolean_variable'})))
    print('STRING', default_client.get_string_value('unique_feature_key', '', EvaluationContext(attributes={'id': 'user_id', 'key': 'string_variable'})))
    print('INTEGER', default_client.get_integer_value('unique_feature_key', 10, EvaluationContext(attributes={'id': 'user_id', 'key': 'number_variable'})))
    print('FLOAT', default_client.get_float_value('unique_feature_key', 10.0, EvaluationContext(attributes={'id': 'user_id', 'key': 'float_variable'})))
    print('OBJECT', default_client.get_object_value('unique_feature_key', {}, EvaluationContext(attributes={'id': 'user_id', 'key': 'json-variable'})))

start()
```

## Authors

* [Abhishek Joshi](https://github.com/Abhi591)

## Changelog

Refer [CHANGELOG.md](https://github.com/wingify/vwo-openfeature-provider-python/blob/master/CHANGELOG.md)

## Contributing

Please go through our [contributing guidelines](https://github.com/wingify/vwo-openfeature-provider-python/blob/master/CONTRIBUTING.md)


## Code of Conduct

[Code of Conduct](https://github.com/wingify/vwo-openfeature-provider-python/blob/master/CODE_OF_CONDUCT.md)

## License

[Apache License, Version 2.0](https://github.com/wingify/vwo-openfeature-provider-python/blob/master/LICENSE)

Copyright 2024 Wingify Software Pvt. Ltd.
