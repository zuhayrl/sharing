from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections

class CustomTopo(Topo):
    def build(self):
        # Create two switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Connect switches together
        self.addLink(s1, s2)

        # Add 3 hosts to each switch
        for i in range(1, 4):
            h = self.addHost(f'h1{i}')
            self.addLink(h, s1)

        for i in range(1, 4):
            h = self.addHost(f'h2{i}')
            self.addLink(h, s2)

def run():
    topo = CustomTopo()
    net = Mininet(topo=topo, switch=OVSSwitch)
    net.start()
    print("Retrun network information")
    dumpNodeConnections(net.hosts)
    print("Running ping test")
    net.pingAll()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
