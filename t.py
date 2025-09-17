import dis

src = "if True: pass"
code = compile(src, "foo", "exec")
new_code = bytes([
    128, 0,
    127, 0,  # EXTENDED_OPCODE
    0, 0,    # EXTENDED_NOP
    82, 1,
    35, 0
])
code = code.replace(co_code=new_code)
dis.dis(code)
exec(code)
