from mininet.topolib import TreeTopo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.log import setLogLevel

def iperf_all_pairs(net):
    hosts = net.hosts
    for i in range(len(hosts)):
        for j in range(i + 1, len(hosts)):
            h1 = hosts[i]
            h2 = hosts[j]
            print(f"\nTesting bandwidth between {h1.name} and {h2.name}")
            print(net.iperf((h1, h2)))

def run():
    topo = TreeTopo(depth=2, fanout=3)
    net = Mininet(topo=topo)
    net.start()

    dumpNodeConnections(net.hosts)
    iperf_all_pairs(net)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
