import pytest
from iac_patterns.singleton import ConfigSingleton
from iac_patterns.factory import NullResourceFactory
from iac_patterns.prototype import ResourcePrototype
from iac_patterns.adapter import MockBucketAdapter


@pytest.fixture(autouse=True)
def reset_singleton_instance():
    if ConfigSingleton in ConfigSingleton._instances:
        del ConfigSingleton._instances[ConfigSingleton]


def test_singleton_instance_same():
    instance1 = ConfigSingleton("env1")
    instance2 = ConfigSingleton("env2")

    assert instance1 is instance2
    assert instance1.env_name == "env1"
    assert instance2.env_name == "env1"


def test_prototype():
    base_resource = NullResourceFactory.create("base_app")
    prototype = ResourcePrototype(base_resource)

    def add_dev_trigger(data):
        path = data["resource"][0]["null_resource"][0]["base_app"][0]
        path["triggers"]["env"] = "dev"

    def add_prod_trigger(data):
        path = data["resource"][0]["null_resource"][0]["base_app"][0]
        path["triggers"]["env"] = "production"

    clone1 = prototype.clone(add_dev_trigger).data
    clone2 = prototype.clone(add_prod_trigger).data

    clone1_path = clone1["resource"][0]["null_resource"][0]["base_app"][0]
    clone2_path = clone2["resource"][0]["null_resource"][0]["base_app"][0]

    clone1_triggers = clone1_path["triggers"]
    clone2_triggers = clone2_path["triggers"]

    assert clone1_triggers["env"] == "dev"
    assert clone2_triggers["env"] == "production"
    assert "env" in clone1_triggers
    assert "env" in clone2_triggers
    assert clone1_triggers != clone2_triggers


def test_adapter_triggers():
    null_resource = NullResourceFactory.create("simple_bucket")

    adapter = MockBucketAdapter(null_resource)
    bucket_resource = adapter.to_bucket()

    bucket_config = bucket_resource["resource"]["mock_cloud_bucket"]["simple_bucket"]
    assert bucket_config["name"] == "simple_bucket"

    expected_keys = {"name"}
    actual_keys = set(bucket_config.keys())
    assert expected_keys.issubset(actual_keys)
