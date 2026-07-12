# print(10 / 0)   # ❌ ZeroDivisionError — program এখানেই থেমে যায়
# print('End')    # ❌ এ লাইন কখনো run হবে না!

# print('5' + 5)

# print(int('fff'))

# numbers = [1,2,3,4,54,5,55]
# print(numbers[22])

# name = 'ruhu'

# name.push("dd")

try:
    num = int(input('সংখ্যা দাও: '))
    result = 100 / num
except ValueError:
    print('স্বাভাবিক সংখ্যা দাও!')
except ZeroDivisionError:
    print('শূন্য দিয়ে ভাগ হয় না!')
else:
    print(f'ফলাফল: {result}')  # exception না হলে চলবে
finally:
    print('সবসময় চলে')  # exception হোক বা না