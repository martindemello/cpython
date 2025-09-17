
        switch(opcode) {
            case EXTENDED_NOP: {
                _PyFrame_SetStackPointer(frame, stack_pointer);
                fprintf(stderr, "extended nop!\n");
                stack_pointer = _PyFrame_GetStackPointer(frame);
            }
        }