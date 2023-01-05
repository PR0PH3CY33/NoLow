import netfilterqueue

import time


buckets = {}

def process_packet(packet):

    ip_header = packet.get_payload()[:20]

    src_ip = ip_header[12:16]

    if src_ip in buckets:

        bucket = buckets[src_ip]

        if(bucket["tokens"] > 0):

            bucket["tokens"] -= 1

            packet.accept()

        else:

            packet.drop()
    else:

        buckets[src_ip] = {

            "tokens": 10,

            "timestamp": time.time()

        }

        packet.accept()

nfqueue = netfilterqueue.NetfilterQueue()

nfqueue.bind(1, process_packet)

try:

    nfqueue.run()

except KeyboardInterrupt:

    print("Interrupted")

nfqueue.unbind()
