The client sends multiple packets based on its current "congestion window".

If all packets are acknowledged, it increases the window size.

If timeouts occur (no ACK), it assumes congestion and reduces the window.

This mimics TCP-like congestion control over UDP.
