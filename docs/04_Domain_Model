+--------+        configures        +------------+
|  User  |------------------------->| Controller |  -----------|
+--------+                          +------------+             |
                                         |                     |
                                         | (1:n)               |
                                         v                     |
                          +--------------------------+         |
                          | LightningConfiguration   |         |
                          +--------------------------+         |
                                         |                     |
                                         | Apply (1:n)         can view (1:n) 
                                         v                     |
                                      +------+                 |
                                      | Area | <---------------|
                                      +------+
                                     /        \
                    contains (1:0..n)          contains (1:0..n)
                                   v            v
                        +----------------+     +------+     can override (1:1)     +-------+ 
                        | CommonAreas   |      | Room |   <----------------------- | Guest |
                        | (corridors,   |      +------+                            +-------+
                        |  main hall..) |        |
                        +----------------+       | has (1:n)
                                       |         |
                         has (1:n)     |         |
                                       |         |   
                                       +---------+
                                       |  Light  |
                                       +---------+
                            

ChatGPT was used to help convert my own draw.io diagram to ASCII diagram
