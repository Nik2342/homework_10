from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

#print(get_mask_card_number(7000792289606361))

#print(get_mask_account(73654108430135874305))

#print(mask_account_card("Visa Platinum 7000792289606361"))

#print(get_date("2024-03-11T02:26:18.671407"))


# _transactions = filter_by_currency([], "USD")
# for _ in range(2):
#     print(next(_transactions))

# descriptions = transaction_descriptions([])
# for _ in range(5):
#     print(next(descriptions))
#
# for card_number in card_number_generator(1, 5):
#     print(card_number)