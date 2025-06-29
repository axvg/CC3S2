from typing import Dict, Any


class MockBucketAdapter:
    def __init__(self, null_block: Dict[str, Any]):
        null_resource_section = null_block["resource"][0]["null_resource"][0]
        self.name = list(null_resource_section.keys())[0]
        self.triggers = null_resource_section[self.name][0].get("triggers", {})

    def to_bucket(self) -> Dict[str, Any]:
        bucket_resource = {
            "resource": {
                "mock_cloud_bucket": {
                    self.name: {
                        "name": self.name
                    }
                }
            }
        }
        bucket_resource["resource"]["mock_cloud_bucket"][self.name].update(
            self.triggers)
        return bucket_resource
