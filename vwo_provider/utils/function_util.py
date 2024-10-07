# Copyright 2024 Wingify Software Pvt. Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Optional
from openfeature.evaluation_context import EvaluationContext

def convert_to_vwo_context(evaluation_context: Optional[EvaluationContext]) -> dict:
    """
    Converts an OpenFeature EvaluationContext object to a dictionary that can be used as a VWO Context object.

    :param evaluation_context: An optional EvaluationContext object that contains attributes for evaluation.
    :return: A dictionary containing the context data.
    """
    if evaluation_context is None or evaluation_context.attributes.get('id') is None or evaluation_context.attributes.get('id') == '':
        return {}

    # Extract required values from evaluation_context (assuming it behaves like a dictionary)
    context_data = {
        'id': evaluation_context.attributes.get('id'),
        'user_agent': evaluation_context.attributes.get('user_agent'),
        'ip_address': evaluation_context.attributes.get('ip_address'),
        'custom_variables': evaluation_context.attributes.get('custom_variables', {}),
        'variation_targeting_variables': evaluation_context.attributes.get('variation_targeting_variables', {}),
    }

    return context_data

