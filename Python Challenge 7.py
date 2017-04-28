from PIL import Image
import re
target_image = Image.open('oxygen.png')

print(target_image.getpixel((0,0)))

row = [target_image.getpixel((x, target_image.height / 2)) for x in range(target_image.width)]
print(row[::7])
ords = [r for r, g, b, a in row if r == g == b]

"".join(map(chr, ords))
nums = re.findall("\d+", "".join(map(chr, ords)))
print(nums)
print("".join(map(chr, map(int, nums))))
