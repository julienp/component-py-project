from typing import TypedDict

import pulumi


class Args(TypedDict):
    str_input: pulumi.Input[str]


class MyComponent(pulumi.ComponentResource):
    def __init__(self, name: str, args: Args, opts: pulumi.ResourceOptions):
        super().__init__("component:index:MyComponent", name, {}, opts)
        pulumi.log.info(f"Creating MyComponent with name: {name}")
