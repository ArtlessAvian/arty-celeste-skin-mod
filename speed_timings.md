# Speed Timings
We don't want to reference the original sprites.
However, I'm an annoying perfectionist. I don't want to be skating or slipping.

Skating is moving faster than animation suggests. (Imagine walking with rollerskates.)
Slipping is moving slower than animation suggests. (Imagine walking on ice.)

Slipping is preferred over skating. Animate faster than actual movement to do so.

Celeste internally runs at 60 "game frames" per second
(as opposed to "animation frames," which I will call "cells").
An animation frame will be held for multiple animation frames, which by definition is skating.
Small errors in position are fine.

# Vanilla Animations

## Important (Grounded)
| animation | loop | velocity (pps)  | animation delay (s) | pixels per frame | frame count | pixels per anim |
| --------- | ---- | --------------- | ------------------- | ---------------- | ----------- | --------------- |
| runSlow   | no   |  (   90,    0 ) |        0.07         |       6.3        |         12  |      75.6       |
| runFast   | yes  |  (   90,    0 ) |        0.05         |       4.5        |         12  |      54.        |
| climbup   | yes  |  (    0,   45 ) |        0.04         |       1.8        |          6  |      10.8       |

## Important (Not Grounded)
| animation | loop | velocity (pps)  | animation delay (s) | pixels per frame | frame count | pixels per anim |
| --------- | ---- | --------------- | ------------------- | ---------------- | ----------- | --------------- |
| jumpSlow  | yes  |  ( slow,  105 ) |        0.1          |      10.5        |          2  |      21.        |
| jumpFast  | yes  |  ( fast,  105 ) |        0.1          |      10.5        |          2  |      21.        |
| fallSlow  | yes  |  ( slow,  160 ) |        0.1          |      16.         |          2  |      32.        |
| fallFast  | yes  |  ( fast,  160 ) |        0.1          |      16.         |          2  |      32.        |
| dash      | yes  |  (  240,    0 ) |        0.09         |      21.6        |          4  |      86.4       |

## Niche
| animation | loop | velocity (pps)  | animation delay (s) | pixels per frame | frame count | pixels per anim |
| --------- | ---- | --------------- | ------------------- | ---------------- | ----------- | --------------- |
| walk      | yes  |  (   64,    0 ) |        0.06         |       3.84       |         12  |      43.2       |
| runWind   | yes  |  (   90,    0 ) |        0.095        |       8.55       |         12  |     102.6       |
| wallslide | yes  |  (    0,   80 ) |      (1 / 60)       |     (4 / 3)      |          1  |     (4 / 3)     |
| swimIdle  | yes  |  (   60,    0 ) |        0.08         |       4.8        |          6  |      28.8       |
| swimUp    | yes  |  (   60,   80 ) |        0.08         |       6.4        |          6  |      38.4       |
| swimDown  | yes  |  (   60,   80 ) |        0.08         |       6.4        |          6  |      38.4       |

# Adjustments
We can control the animation delay (easy) and frame count (hard).
Frame count shouldn't deviate far from vanilla. I am open to animating on twos or threes.
