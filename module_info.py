import idautils

print Modules()
module = GetFirstModule()
while module is not None:
    print GetModuleName(module)
    print "\t" + str(module) + "\t" + str(GetModuleSize(module))
    module = GetNextModule(module)
