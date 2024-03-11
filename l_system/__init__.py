from typing import Dict


class LSystem:
    """A generic L-system."""

    def __init__(self, productions: Dict[str, str]) -> None:
        self.productions = productions
    
    def grow(self, sequence: str, steps: int) -> str:
        """Grow the system."""
        
        if steps == 0:
            return sequence
        
        return self.grow(
            ''.join((self.productions.get(symbol) or symbol) for symbol in sequence),
            steps - 1,
        )
