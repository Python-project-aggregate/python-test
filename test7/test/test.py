import json
# test_dict = [{'哈哈':7600,1:6300,'1':2}]
# a = json.dumps(test_dict,ensure_ascii=False)
# print(type(a))
# with open('shopping.txt', 'w') as f:
#     json.dump(test_dict, f,ensure_ascii=False)
with open('shopping.txt', 'r') as f1:
    b = json.load(f1)
    print(type(b))