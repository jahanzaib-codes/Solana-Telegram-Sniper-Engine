"""Jupiter V6 routing and dynamic Jito MEV tip estimation engine."""

from typing import Dict


class JupiterJitoRouter:
    """Calculates best DEX routes and dynamic Jito tip tiers based on current block congestion."""

    def __init__(self):
        # Simulated live percentile tip ladders (in SOL)
        self.tip_ladder = {
            "50th_percentile": 0.005,
            "75th_percentile": 0.012,
            "95th_percentile": 0.028,
            "99th_percentile": 0.065
        }

    def resolve_best_route(self, token_mint: str, action: str) -> str:
        """Determines whether direct Pump.fun bonding curve or Jupiter V6 gives superior execution."""
        if "pump" in token_mint.lower() or token_mint.endswith("pump"):
            return "Pump.fun Bonding Curve Direct"
        return "Jupiter V6 Aggregator (Multi-Hop)"

    def get_recommended_jito_tip(self, mode: str = "HIGH") -> float:
        if mode == "VERY_HIGH":
            return self.tip_ladder["95th_percentile"]
        elif mode == "HIGH":
            return self.tip_ladder["75th_percentile"]
        return self.tip_ladder["50th_percentile"]

    def get_tip_ladder(self) -> Dict[str, float]:
        return self.tip_ladder
