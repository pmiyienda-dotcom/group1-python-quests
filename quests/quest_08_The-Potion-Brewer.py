dragon_scales_count = 3

dragon_scales_price = 10

elf_tears_count = 5

elf_tears_price = 3

dragon_scales_total = dragon_scales_count * dragon_scales_price

elf_tears_total = elf_tears_count * elf_tears_price

grand_total = dragon_scales_total + elf_tears_total

print(f"Dragon scales: {dragon_scales_count} x {dragon_scales_price} gold = {dragon_scales_total} gold")

print(f"Elf tears:     {elf_tears_count} x {elf_tears_price} gold = {elf_tears_total} gold")

print(f"Total cost:    {grand_total} gold")
