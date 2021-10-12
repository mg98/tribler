import pytest

from tribler_core.components.base import Session
from tribler_core.components.gigachannel.gigachannel_component import GigaChannelComponent
from tribler_core.components.ipv8.ipv8_component import Ipv8Component
from tribler_core.components.masterkey.masterkey_component import MasterKeyComponent
from tribler_core.components.metadata_store.metadata_store_component import MetadataStoreComponent
from tribler_core.components.restapi import RESTComponent


# pylint: disable=protected-access

@pytest.mark.asyncio
async def test_giga_channel_component(tribler_config):
    components = [MetadataStoreComponent(), RESTComponent(), MasterKeyComponent(), Ipv8Component(),
                  GigaChannelComponent()]
    session = Session(tribler_config, components)
    with session:
        await session.start()

        comp = GigaChannelComponent.instance()
        assert comp.started_event.is_set() and not comp.failed
        assert comp.community
        assert comp._ipv8_component

        await session.shutdown()