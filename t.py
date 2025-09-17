import dis

src = "if True: pass"
code = compile(src, "foo", "exec")
new_code = bytes([
    128, 0,
    127, 0,  # EXTENDED_OPCODE
    0, 0,    # EXTENDED_NOP
    127, 4,  # EXTENDED_OPCODE with 4 CACHE entries
    1, 0,    # XOP_WITH_CACHE
    0, 0,    # CACHE
    0, 0,    # CACHE
    0, 0,    # CACHE
    0, 0,    # CACHE
    82, 1,
    35, 0
])
code = code.replace(co_code=new_code)
dis.dis(code)
exec(code)
