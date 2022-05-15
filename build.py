import cffi
ffibuilder=cffi.FFI()

ffibuilder.cdef('typedef ... Tcl_Interp;')

ffibuilder.embedding_api('int Mytest_Init(Tcl_Interp *interp);')
ffibuilder.set_source("_mytest", r'#include "tcl.h"', libraries=['tcl'])
ffibuilder.embedding_init_code("""
from _mytest import ffi, lib

@ffi.def_extern()
def Mytest_Init(interp):
    print('Hello world')
    return 0
""")


ffibuilder.compile(target='mytest.so',verbose=1)

