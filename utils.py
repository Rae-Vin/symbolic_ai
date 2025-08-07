# utils.py

# Placeholder for future extensions: logging, visualizations, etc.

def log_anchor_status(agent):
    for anchor, alive, phi in agent.status():
        print(f"[{anchor}] Alive: {alive}, Phi: {phi}")
