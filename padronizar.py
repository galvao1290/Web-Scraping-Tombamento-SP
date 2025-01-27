import json

counter = 1
for i in range(8):

    with open(f"dados_tombamento{counter}.json", encoding="utf-8") as f:
        data = json.load(f)


    data_corrigido = [
        {key.replace(" ", "_"): value for key, value in item.items()}
        for item in data
    ]

    with open(f"dados_tombamento{counter}_corrigido.json", "w", encoding="utf-8") as f:
        json.dump(data_corrigido, f, ensure_ascii=False, indent=4)
    
    counter += 1