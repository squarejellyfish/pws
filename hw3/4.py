table = {
    '一筒': 1, '二筒': 2, '三筒': 3, '四筒': 4, '五筒': 5, '六筒': 6,
    '七筒': 7, '八筒': 8, '九筒': 9, '一條': 11, '二條': 12, '三條': 13, '四條': 14,
    '五條': 15, '六條': 16, '七條': 17, '八條': 18, '九條': 19, '一萬': 21,
    '二萬': 22, '三萬': 23, '四萬': 24, '五萬': 25, '六萬': 26, '七萬': 27,
    '八萬': 28, '九萬': 29, '東風': 31, '南風': 32, '西風': 33, '北風': 34,
    '紅中': 35, '發財': 36, '白板': 37
}
count = {key: 0 for key in table.keys()}

hand = input().split("、")
for h in hand:
    count[h] += 1
hand = [table[h] for h in hand if count[h] != 3]
hand.sort()

# print(hand)

eyes = []
for mah, c in count.items():
    if (c == 2):
        eyes.append(mah)
        hand = [h for h in hand if h != table[mah]]

# print(hand)
idx, l = 0, len(hand)
new_hand = hand.copy()
while idx <= l - 3:
    if (hand[idx] + 1 == hand[idx + 1] and hand[idx + 1] + 1 == hand[idx + 2] and hand[idx] < 30):
        # print(f"remove {hand[idx]}, {hand[idx + 1]}, {hand[idx + 2]}")
        new_hand.remove(hand[idx])
        new_hand.remove(hand[idx + 1])
        new_hand.remove(hand[idx + 2])
        idx += 3
    else: idx += 1

# print(new_hand)
if (not new_hand and len(eyes) == 2):
    print(eyes[0])
    print(eyes[1])
elif (len(new_hand) == 2 and len(eyes) == 1 and new_hand[1] < 30):
    mahjong = {val: key for key, val in table.items()}
    if (new_hand[1] - new_hand[0] == 2 and new_hand[0] + 1 in mahjong): # mid hole
        print(mahjong[new_hand[0] + 1])
    elif (new_hand[1] - new_hand[0] == 1):
        if (new_hand[0] - 1 in mahjong): print(mahjong[new_hand[0] - 1])
        if (new_hand[1] + 1 in mahjong): print(mahjong[new_hand[1] + 1])
    else:
        print("沒有聽牌")
else:
    print("沒有聽牌")
        
    
