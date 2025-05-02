meme_dict = {
    "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
    "LOL": "Una risposta comune a qualcosa di divertente",
    "SHEESH": "Leggera disapprovazione",
    "CREEPY": "Spaventoso, inquietante",
    "PARA": "Preoccuparsi per qualcosa, paranoiarsi"
}

parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")
if parola in meme_dict:
    print(meme_dict[parola])
else:
    print("Non lo so neanche io 🤣")
