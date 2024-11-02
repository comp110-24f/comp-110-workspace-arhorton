"""Examples of dictionary syntax with Ice Cream Shop order tallies"""

__author__ = "730664552"

# dictionary type is dict[key_type, value_type]
ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len returns the total number of PAIRS in the dictionary
print(len(ice_cream))

# add keyt entries using subscription notation
ice_cream["mint"] = 10

# access values by their key using subscription
mint_orders: int = ice_cream["mint"]
print(mint_orders)

# re-assign values by their key using assignment operators
ice_cream["mint"] = ice_cream["mint"] + 1
ice_cream["mint"] += 1

# remove items by key using the pop method
print(ice_cream.pop("strawberry"))
# will print the value at which strawberry was when it was popped

# test if a key is in the dictionary
print("vanilla" in ice_cream)


# loop through items using for-in loops
# total: int = 0
# the variable (e.g. flavor) iterates over
# each key one-by-one in the dictiionary
for flavor in ice_cream:
    count: int = ice_cream[flavor]
    print(f"{flavor}: {count}")

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint")
