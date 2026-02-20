# sg1-pill-puzzle

SG1 is an interactive Python 3 program designed to run in the Thonny IDE. This program simulates the classic "[Pill Puzzle](https://en.wikipedia.org/wiki/Pill_puzzle)" probability problem using computational brute force instead of analytical math, allowing users to explore how whole pills &amp; half pills evolve over time in a magical bottle where each pill is randomly selected.<br>

## Authors
- Riddhi Acharya
- Zachary Gmyr
- Caleb Hackmann
- Tressa Millering
- Devon Schrader

---
## Description

In the Pill Puzzle, a bottle begins with *N* whole pills and is used over the course of *2 × N* days. Each day, one pill is randomly selected from the bottle.
- If a whole pill is selected, it is split in half. One half is taken, and the other half is returned to the bottle.
- If a half pill is selected, it is simply taken and removed from the bottle.

On the first day, the selection must be a whole pill since the bottle initially contains only whole pills. From that point forward, selections are random among all remaining whole and half pills. By the final day (day *2 × N*), only a single half pill remains, which must be taken.<br>

Given an initial number of pills (1-1000), SG1 runs repeated simulations to estimate:
1. the expected number of whole and half pills remaining on a given day *D*
2. the most likely day when all whole pills are depleted
3. additional statistical insights derived from large-scale simulation


