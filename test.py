from pwn import *

io = remote("127.0.0.1", 4444)

word = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec dapibus sapien. Morbi efficitur sollicitudin ex. Mauris pellentesque odio urna, sed tristique mauris ultrices a. Aliquam commodo mattis est at pulvinar. Donec vehicula leo nec mauris fermentum dignissim. Quisque blandit nec quam quis sollicitudin. Vestibulum ac risus volutpat, maximus velit ut, vulputate ligula. Maecenas lacinia, neque at blandit mollis, lorem risus sagittis erat, mattis feugiat diam neque nec ante. Fusce non suscipit quam.

Proin lectus leo, scelerisque faucibus lobortis ut, commodo et orci. Curabitur libero nunc, finibus id quam sit amet, consectetur sodales turpis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nulla facilisi. Donec quis odio quis mi fermentum fringilla id et massa. Vivamus congue sed mauris a cursus. Vivamus varius ultrices libero eget posuere. Morbi consequat erat augue, eu porta purus vehicula tincidunt. Nunc efficitur, odio ac pharetra fermentum, erat tellus consectetur nulla, vitae suscipit augue est et tellus.

Fusce congue tortor mi, vitae faucibus sem porta ut. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed dignissim vehicula nulla, eu mollis dui consectetur bibendum. Duis sollicitudin lorem nec lacus venenatis, gravida consectetur enim finibus. Quisque et nunc dolor. Curabitur elementum massa eu luctus sollicitudin. Nulla venenatis sapien eu tellus malesuada, eget iaculis nunc blandit. In pulvinar ligula efficitur ante rutrum efficitur. Sed iaculis ligula ut ultricies volutpat. Mauris porta, diam hendrerit gravida aliquam, lorem dui gravida metus, vehicula molestie eros tortor ac magna. Morbi quis consequat magna.

Nam egestas consectetur nibh, eu convallis risus aliquet eget. Fusce eu quam at nisl porttitor blandit et eu quam. Donec in orci at nulla placerat gravida. Proin at eros urna. Nunc lobortis nisl quis blandit semper. Sed lobortis nisi et posuere pharetra. Donec congue nulla justo, et varius urna sollicitudin nec. Praesent commodo est sem, a malesuada ante auctor ultricies. Fusce accumsan tincidunt elementum. Pellentesque ac malesuada est, non luctus purus. Morbi molestie lacinia mollis.

Sed pharetra id urna ut blandit. Nunc sit amet velit sed metus vulputate volutpat vitae ac eros. Donec sed ultricies enim, vel fringilla ligula. Morbi vulputate ornare lacinia. Nam semper, sem in varius semper, est elit egestas dui, in placerat eros diam in metus. Quisque aliquet efficitur mauris, vel ullamcorper arcu rhoncus ac. Sed sagittis dolor ut placerat auctor. Donec velit urna, porta at convallis sed, sagittis vel ex. Integer id tristique turpis. Cras a felis nec urna eleifend lobortis non at velit. Etiam eu posuere orci, eu mollis nisi. Nullam et mi tincidunt, ultricies est eget, posuere ligula. Quisque nibh metus, feugiat sit amet gravida ac, sodales vitae lorem. Vivamus tempus eu massa vel vestibulum. Etiam dolor mi, scelerisque ac ipsum in, viverra ultrices purus.
"""

res = ""
for lmao in word.split("\n"):
    res += lmao 

res2 = b'aaaaaaaaaaaaaaaaaaaaa'
io.sendline(res.encode())
io.sendline(res2)
io.interactive()