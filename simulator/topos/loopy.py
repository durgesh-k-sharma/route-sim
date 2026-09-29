import sim
from . import loader


def launch(
    switch_type=sim.config.default_switch_type, host_type=sim.config.default_host_type
):
    """
    Load the loopy square topology from the topology data directory.
    """
    loader.launch(
        "./topology_data/loopy4.topo", switch_type=switch_type, host_type=host_type
    )
