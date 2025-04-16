from mininet.topolib import TreeTopo, SingleSwitchTopo
from mininet.topo import LinearTopo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.log import setLogLevel

def iperf_all_pairs(net):
    hosts = net.hosts
    print("\nRunning iperf between all host pairs:\n")
    for i in range(len(hosts)):
        for j in range(i + 1, len(hosts)):
            h1 = hosts[i]
            h2 = hosts[j]
            print(f"{h1.name} -> {h2.name}")
            bw = net.iperf((h1, h2))
            print(bw)

def run_single_topo():
    topo = SingleSwitchTopo(n=4)
    net = Mininet(topo=topo)
    net.start()

    dumpNodeConnections(net.hosts)
    iperf_all_pairs(net)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run_single_topo()
