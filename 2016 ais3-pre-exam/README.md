
## binary 1
```
#!/usr/bin/python
# -*- coding: utf-8 -*-
import angr

START_ADDR = 0x0804894e
FIND_ADDR = 0x4006bc
AVOID_ADDR = 0x4006c8

angr.path_group.l.setLevel("DEBUG")
p = angr.Project( "rev" , load_options={'auto_load_libs' : False})

argv1 = angr.claripy.BVS('argv1', 0x1e * 8)  # the length from strcpy is 0x43
initial_state = p.factory.entry_state(args=["./rev", argv1])

pg = p.factory.path_group(initial_state)
pg.explore(find=(FIND_ADDR,), avoid=(AVOID_ADDR,)) 

state = pg.found[0].state
print "agrv1", state.se.any_str(argv1)
```

##Binary 3
```
#!/usr/bin/python
# -*- coding: utf-8 -*-
import angr

START_ADDR = 0x0804894e
FIND_ADDR = 0x402471
AVOID_ADDR = 0x40247d

angr.path_group.l.setLevel("DEBUG")
p = angr.Project( "caaaaalculate" , load_options={'auto_load_libs' : False})

initial_state = p.factory.entry_state(args=["./caaaalculate"])

pg = p.factory.path_group(initial_state)
pg.explore(find=(FIND_ADDR,), avoid=(AVOID_ADDR,)) 

state = pg.found[0].state
print pg.found[0].state.posix.dumps(0)
```
