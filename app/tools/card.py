from semantic_kernel.functions import kernel_function
import json

class CardTools:
    @kernel_function(name="get_card_recommendation", description="Get credit card recommendation based on card name.")
    def get_card_recommendation(self, card_name: str) -> str:
        """
        Get details and benefits for a specific credit card.
        """
        cards = {
            "BankGold": {
                "card": "BankGold",
                "benefit": "4x points on dining worldwide",
                "fx_fee": "None",
                "source": "Internal Policy DB"
            },
            "BankPlatinum": {
                "card": "BankPlatinum",
                "benefit": "5x points on flights and hotels",
                "fx_fee": "None",
                "source": "Internal Policy DB"
            },
            "BankRewards": {
                "card": "BankRewards",
                "benefit": "3x points on gas and groceries",
                "fx_fee": "3%",
                "source": "Internal Policy DB"
            }
        }
        
        card_info = cards.get(card_name)
        if card_info:
            return json.dumps(card_info)
        else:
            return json.dumps({"error": "Card not found"})

    @kernel_function(name="recommend_card", description="Recommend a credit card for a transaction.")
    def recommend_card(self, mcc: str, amount: float, country: str) -> str:
        """
        Recommend a card based on transaction details.
        """
        if mcc == "5812": # Dining
            return json.dumps({"card": "BankGold", "reason": "4x points on dining"})
        elif country != "USA":
            return json.dumps({"card": "BankGold", "reason": "No foreign transaction fee"})
        elif amount > 500:
            return json.dumps({"card": "BankPlatinum", "reason": "High spend reward"})
        else:
            return json.dumps({"card": "BankRewards", "reason": "General rewards"})