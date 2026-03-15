f = [lambda x: x*i for i in range(5)]
print(f)  # Output: [<function <lambda> at 0x...>, <function <lambda> at 0x...>, <function <lambda> at 0x...>, <function <lambda> at 0x...>, <function <lambda> at 0x...>]
print(f[0](1))  # Output: 40
print(f[1](10))  # Output: 40
print(f[2](10))  # Output: 40
print(f[3](5))  # Output: 40

print(f[3](0))  # Output: 40
print(f[3](10))  # Output: 40