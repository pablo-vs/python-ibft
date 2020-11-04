from collections import defaultdict

if __name__ == '__main__':
    from bls_threshold import py_ecc_bls, reconstruct, get_aggregate_key
else:
    from .bls_threshold import py_ecc_bls, reconstruct, get_aggregate_key


class smr_replica:

    def __init__(self, message_primitive):
        self.timeout = 30
        self.max_batch = 1
        self.creg = 0
        self.nref = 0
        self.current_cons = -1
        self.dec_log = []
        self.to_order = set()
        self.tmp = []
        self.decided = []
        self.stopped = False
        self.last_seq = defaultdict(lambda: 0)
        self.change_reg = defaultdict(set)
        self.data = defaultdict(set)
        self.sync = defaultdict(set)

        self.message_handlers = {
                "request": self.request_received
                "forwarded": self.request_received

                }

    def activate_timers():

    def cancel_timers():

    def valid_sig():

    def no_gaps():

    def valid_dec():

    def hcons():

    def hlog():


    def new_batch(self):
        if len(self.to_order) > 0 and self.current_cons == -1 \
                and not self.stopped:
            
            batch = self.to_order.pop()
            self.current_cons = hcons(self.dec_log)).i + 1
            self.vp_propose(self.current_const, self.creg % R, validity_callback, batch)

    def request_received(self, req):
        if self.last_seq[req.sender] + 1 == req.seq and valid_sig(req):
            self.to_order.add(req)
            if not stopped:
                activate_timers(req, timeout)
            self.lastSeq[req.sender] += 1


    def process_message(self, m):
        return self.message_handlers.get(m["type"], err)()
        
