# Colors
| Color Part             | Reference | Adjusted |
| ----------             | --------- | -------- |
| Cyan Body              | #A0DEFF   | #83BEFF  |
| Reverse Countershading | #82ABD7   | #6B8BB6  |
| White Clothes          | #FFFFFF   | #FFFFFF  |
| Gray Stripes           | #B3B3B3   | #939393  |
| Yellow Accent          | #FFFF94   | #FFFF77  |

# Why
Modded rooms are kinda overly bright?

There's a bloom filter in the game.
One of the helper mods displays the bloom of the room you're in.
The most I've seen in the vanilla game is "0.5 base x 1 (FFFFFF)"
I've also seen 0.7 in modded.

I'm making a hard assumption that these numbers are additive.
(You can add colors. You can scale towards/away from black.)
It's straightforward, but also causes color channels to max out.
This causes hue shifts towards cyan, magenta, yellow,
then causes desaturation as things become more white.

