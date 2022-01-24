shopping_dict = {
    "piekarnia": ["chleb", "paczek", "bulki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
for sklep, rzeczy in shopping_dict.items():
  print("ide do " + str(sklep.title()) + " kupuje tam" + str(rzeczy))