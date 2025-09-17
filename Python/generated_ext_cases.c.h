
        switch(opcode) {
            case EXTENDED_NOP: {
                _PyFrame_SetStackPointer(frame, stack_pointer);
                fprintf(stderr, "extended nop!\n");
                stack_pointer = _PyFrame_GetStackPointer(frame);
            }

            case XOP_WITH_CACHE: {
                _PyFrame_SetStackPointer(frame, stack_pointer);
                fprintf(stderr, "extended op with cache\n");
                stack_pointer = _PyFrame_GetStackPointer(frame);
            }
        }