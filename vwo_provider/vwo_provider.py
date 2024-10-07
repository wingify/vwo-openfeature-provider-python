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

from typing import List, Optional, Union

from openfeature.evaluation_context import EvaluationContext
from openfeature.flag_evaluation import FlagResolutionDetails
from openfeature.hook import Hook
from openfeature.provider import AbstractProvider, Metadata
from vwo_provider.utils.function_util import convert_to_vwo_context

class VWOProvider(AbstractProvider):
    def get_metadata(self) -> Metadata:
        return Metadata(name="vwo-openfeature-provider-python-provider")

    def get_provider_hooks(self) -> List[Hook]:
        return []
    
    # create constructor
    def __init__(self, vwoClient):
        """
        Constructor for VWOProvider class

        :param vwoClient: VWO client object
        """
        try:
            self.vwoClient = vwoClient
        except Exception as e:
            print('Encountered unrecoverable initialization error: ', e)
       

    def resolve_boolean_details(
        self,
        flag_key: str,
        default_value: bool,
        evaluation_context: Optional[EvaluationContext] = None,
    ) -> FlagResolutionDetails[bool]:
        """
        Resolves the boolean value for the given feature flag based on the provided evaluation context.

        :param flag_key: The key for the feature flag to be resolved.
        :param default_value: The default boolean value to return if no flag value is found.
        :param evaluation_context: An optional EvaluationContext object that contains attributes for evaluation.
        :return: A FlagResolutionDetails object containing the resolved flag value.
        """
        try:
            # Convert OpenFeature EvaluationContext to VWO Context
            vwo_context = convert_to_vwo_context(evaluation_context)

            # Get flag value from VWO
            get_flag = self.vwoClient.get_flag(flag_key, vwo_context)
            # Get all variables
            variables = get_flag.get_variables()

            # If variable key is provided in evaluation_context, get the value of the key
            if evaluation_context.attributes.get('key'):
                result = next(
                    (val for val in variables if val.get('type') == 'boolean' and val.get('key') == evaluation_context.attributes.get('key')),
                    None
                )
                return FlagResolutionDetails(
                        value=result.get('value', default_value) if result else default_value
                    )
    
            # If no context key, fall back to get_flag_enabled
            return FlagResolutionDetails(
                value=get_flag.is_enabled()
            )

        except Exception as e:
            print('Encountered unrecoverable error: ', e)
            return FlagResolutionDetails(
                value=False
            )

    def resolve_string_details(
        self,
        flag_key: str,
        default_value: str,
        evaluation_context: Optional[EvaluationContext] = None,
    ) -> FlagResolutionDetails[str]:
        """
        Resolves the string value for the given feature flag based on the provided evaluation context.

        :param flag_key: The key for the feature flag to be resolved.
        :param default_value: The default string value to return if no flag value is found.
        :param evaluation_context: An optional EvaluationContext object that contains attributes for evaluation.
        :return: A FlagResolutionDetails object containing the resolved flag value.
        """
        try:
            # Convert OpenFeature EvaluationContext to VWO Context
            vwo_context = convert_to_vwo_context(evaluation_context)

            # Get flag value from VWO
            get_flag = self.vwoClient.get_flag(flag_key, vwo_context)
            # Get all variables
            variables = get_flag.get_variables()

            # loop through all variables and get the value of the key
            result = next(
                (val for val in variables if val.get('type') == 'string' and val.get('key') == evaluation_context.attributes.get('key')),
                None
            )

            # return the value of the key
            return FlagResolutionDetails(
                value=result.get('value', default_value) if result else default_value
            )

        except Exception as e:
            print('Encountered unrecoverable error: ', e)
            return FlagResolutionDetails(
                value=default_value
            )

    def resolve_integer_details(
        self,
        flag_key: str,
        default_value: int,
        evaluation_context: Optional[EvaluationContext] = None,
    ) -> FlagResolutionDetails[int]:
        """
        Resolves the integer value for the given feature flag based on the provided evaluation context.

        :param flag_key: The key for the feature flag to be resolved.
        :param default_value: The default integer value to return if no flag value is found.
        :param evaluation_context: An optional EvaluationContext object that contains attributes for evaluation.
        :return: A FlagResolutionDetails object containing the resolved flag value.
        """
        try:
            # Convert OpenFeature EvaluationContext to VWO Context
            vwo_context = convert_to_vwo_context(evaluation_context)

            # Get flag value from VWO
            get_flag = self.vwoClient.get_flag(flag_key, vwo_context)
            # Get all variables
            variables = get_flag.get_variables()

            # loop through all variables and get the value of the key
            result = next(
                (val for val in variables if val.get('type') == 'integer' and val.get('key') == evaluation_context.attributes.get('key')),
                None
            )

            # return the value of the key
            return FlagResolutionDetails(
                value=result.get('value', default_value) if result else default_value
            )

        except Exception as e:
            print('Encountered unrecoverable error: ', e)
            return FlagResolutionDetails(
                value=default_value
            )

    def resolve_float_details(
        self,
        flag_key: str,
        default_value: float,
        evaluation_context: Optional[EvaluationContext] = None,
    ) -> FlagResolutionDetails[float]:
        """
        Resolves the float value for the given feature flag based on the provided evaluation context.

        :param flag_key: The key for the feature flag to be resolved.
        :param default_value: The default float value to return if no flag value is found.
        :param evaluation_context: An optional EvaluationContext object that contains attributes for evaluation.
        :return: A FlagResolutionDetails object containing the resolved flag value.
        """
        try:
            # Convert OpenFeature EvaluationContext to VWO Context
            vwo_context = convert_to_vwo_context(evaluation_context)

            # Get flag value from VWO
            get_flag = self.vwoClient.get_flag(flag_key, vwo_context)
            # Get all variables
            variables = get_flag.get_variables()
            # loop through all variables and get the value of the key
            result = next(
                (val for val in variables if val.get('type') == 'double' and val.get('key') == evaluation_context.attributes.get('key')),
                None
            )

            # return the value of the key
            return FlagResolutionDetails(
                value=result.get('value', default_value) if result else default_value
            )

        except Exception as e:
            print('Encountered unrecoverable error: ', e)
            return FlagResolutionDetails(
                value=default_value
            )

    def resolve_object_details(
        self,
        flag_key: str,
        default_value: Union[dict, list],
        evaluation_context: Optional[EvaluationContext] = None,
    ) -> FlagResolutionDetails[Union[dict, list]]:
        """
        Resolves the variable value of type json for the given feature flag based on the provided evaluation context.

        :param flag_key: The key for the feature flag to be resolved.
        :param default_value: The default value to return if no flag value is found.
        :param evaluation_context: An optional EvaluationContext object that contains attributes for evaluation.
        :return: A FlagResolutionDetails object containing the resolved flag value.
        """
        try:
            # Convert OpenFeature EvaluationContext to VWO Context
            vwo_context = convert_to_vwo_context(evaluation_context)

            # Get flag value from VWO
            get_flag = self.vwoClient.get_flag(flag_key, vwo_context)
            # Get all variables
            variables = get_flag.get_variables()
            # loop through all variables and get the value of the key
            if 'key' in evaluation_context.attributes and evaluation_context.attributes.get('key'):
                result = next(
                    (val for val in variables if val.get('type') == 'json' and val.get('key') == evaluation_context.attributes.get('key')),
                    None
                )

                # return the value of the key
                return FlagResolutionDetails(
                    value=result.get('value', default_value) if result else default_value
                )
            
            # if no key is provided, return all variables
            return FlagResolutionDetails(
                value=variables
            )


        except Exception as e:
            print('Encountered unrecoverable error: ', e)
            return FlagResolutionDetails(
                value=default_value
            )
    
