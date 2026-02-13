from semantic_kernel.functions import kernel_function
import random

class FxTools:
    @kernel_function(name="convert_fx", description="Convert currency amount from one currency to another")
    def convert_fx(self, amount: float, from_currency: str, to_currency: str) -> str:
        """
        Convert currency amount from one currency to another using mock rates.
        """
        # Mock exchange rates (base USD)
        rates = {
            "USD": 1.0,
            "EUR": 0.92,
            "GBP": 0.79,
            "JPY": 150.0,
            "CAD": 1.35,
            "AUD": 1.52
        }
        
        from_rate = rates.get(from_currency.upper(), 1.0)
        to_rate = rates.get(to_currency.upper(), 1.0)
        
        converted_amount = amount * (to_rate / from_rate)
        
        return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"