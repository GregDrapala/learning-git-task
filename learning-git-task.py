shopping_dict = {
    "piekarnia": ["chleb", "paczek", "bulki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
for sklep, rzeczy in shopping_dict.items():
  print("ide do " + str(sklep.title()) + " kupuje tam" + str(rzeczy))
  x = len(shopping_dict["piekarnia"]) + len(shopping_dict["warzywniak"])
print("w sumie kupuje " + str(x) + " produktow" )