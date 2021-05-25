from datetime import datetime

import json

from evidently.analyzers.cat_target_drift_analyzer import CatTargetDriftAnalyzer
from evidently.profile_parts.base_profile_part import ProfilePart


class CatTargetDriftProfilePart(ProfilePart):
    def part_id(self) -> str:
        return 'cat_target_drift'

    def __init__(self):
        super().__init__()
        self.analyzers_types = [CatTargetDriftAnalyzer]

    def analyzers(self):
        return self.analyzers_types

    def calculate(self, analyzers_results):
        target_p_value = analyzers_results[CatTargetDriftAnalyzer].get('target_drift')
        prediction_p_value = analyzers_results[CatTargetDriftAnalyzer].get('prediction_drift')

        profile = {}
        profile['name'] = self.part_id()
        profile['datetime'] = str(datetime.now())
        profile['data'] = {}

        #if target_p_value:
        profile['data']['target_drift'] = {
            'target_type' : 'cat',
            'p_value' : target_p_value
        }

        #if prediction_p_value:
        profile['data']['prediction_drift'] = {
            'prediction_type' : 'cat',
            'p_value' : prediction_p_value
        }

        return profile