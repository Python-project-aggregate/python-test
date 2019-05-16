import json
test_dict = {'哈哈':[7600, {1:6300}]}
a = json.dumps(test_dict,ensure_ascii=False)
print(a)
with open('shopping.json', 'w') as f:
    json.dump(test_dict, f,ensure_ascii=False)
