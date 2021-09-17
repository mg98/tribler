from unittest.mock import Mock

from tribler_core.components.base import Component, testcomponent
from tribler_core.config.tribler_config import TriblerConfig
from tribler_core.modules.tunnel.community.community import TriblerTunnelCommunity


class TunnelsComponent(Component):
    community: TriblerTunnelCommunity

    @classmethod
    def should_be_enabled(cls, config: TriblerConfig):
        return config.ipv8.enabled and config.tunnel_community.enabled

    @classmethod
    def make_implementation(cls, config: TriblerConfig, enable: bool):
        if enable:
            from tribler_core.components.implementation.tunnels import TunnelsComponentImp
            return TunnelsComponentImp(cls)
        return TunnelsComponentMock(cls)


@testcomponent
class TunnelsComponentMock(TunnelsComponent):
    community = Mock()