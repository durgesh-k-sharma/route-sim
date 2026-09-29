"""Learning switch example for the network simulator.

Run it with a command such as:

  ./simulator.py --default-switch-type=learning_switch topos.rand --links=0
"""

import sim.api as api
import sim.basics as basics


class LearningSwitch(api.Entity):
    """Learn source ports and flood packets for unknown destinations."""

    def __init__(self):
        """Initialize switch state."""
        pass

    def handle_link_down(self, port):
        """Remove learned entries that use a port after its link goes down."""
        pass

    def handle_rx(self, packet, in_port):
        """Handle a received packet by learning or flooding."""
        if isinstance(packet, basics.HostDiscoveryPacket):
            # Do not forward host discovery messages.
            return

        # Flood packets through every port except the input port.
        self.send(packet, in_port, flood=True)
