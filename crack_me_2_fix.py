from idaapi import *

class MyDbgHook(DBG_Hooks):
    def dbg_bpt(self, tid, ea):
        if ea == 0x401228:
            print ''.join(chr(Byte(i)) for i in xrange(4202878, 4202894))
        if ea == 0x40123F:
            rv = idaapi.regval_t()
            rv.ival = 1 if (GetRegValue("ecx") == 0) else 0
            idaapi.set_reg_val("ecx", rv)
        continue_process()
        return 0

# Remove an existing debug hook
try:
    if debughook:
        print "Removing previous hook ..."
        debughook.unhook()
except:
    pass

# Install the debug hook
debughook = MyDbgHook()
debughook.hook()

AddBpt(0x401228)
AddBpt(0x40123F)

request_run_to(GetLongPrm(INF_START_IP))
request_step_over()
run_requests()
