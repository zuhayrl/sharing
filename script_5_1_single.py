from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):
    def build(self, n=9):
        switch = self.addSwitch('s1')
        for i in range(n):
            host = self.addHost(f'h{i+1}')
            self.addLink(host, switch)

def iperf_all_pairs(net):
    hosts = net.hosts
    for i in range(len(hosts)):
        for j in range(i + 1, len(hosts)):
            h1 = hosts[i]
            h2 = hosts[j]
            print(f"\nTesting bandwidth between {h1.name} and {h2.name}")
            print(net.iperf((h1, h2)))

def run():
    topo = SingleSwitchTopo(n=9)
    net = Mininet(topo=topo)
    net.start()

    dumpNodeConnections(net.hosts)
    iperf_all_pairs(net)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
