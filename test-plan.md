# Save the Watermelon: Test Plan

Run these tests in the terminal. For repeatable gameplay tests, temporarily set `secret_word = "apple"` inside `play_game()` and restore `choose_word()` afterward. Do not leave the temporary test change in the submitted version.

| Test | Input / setup | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| Correct letter | Secret word `apple`, guess `a` | Shows `a _ _ _ _`; slices unchanged | Fill in after testing | Fill in |
| Incorrect letter | Secret word `apple`, guess `z` | Word unchanged; slices decrease by one | Fill in after testing | Fill in |
| Uppercase input | Guess `A` | Treated as `a` | Fill in after testing | Fill in |
| Lowercase input | Guess `a` | Accepted if not previously guessed | Fill in after testing | Fill in |
| Repeated guess | Guess `a` twice | Second guess rejected; slices unchanged | Fill in after testing | Fill in |
| Multiple characters | Guess `ab` | Rejected; slices unchanged | Fill in after testing | Fill in |
| Number | Guess `7` | Rejected; slices unchanged | Fill in after testing | Fill in |
| Special character | Guess `!` | Rejected; slices unchanged | Fill in after testing | Fill in |
| Win | Guess all distinct letters in `apple` | Win message appears | Fill in after testing | Fill in |
| Loss | Make six valid incorrect guesses before solving | Loss message appears and word is revealed | Fill in after testing | Fill in |
| Replay | Answer `y` after a round | A new round starts | Fill in after testing | Fill in |
| Stop replaying | Answer `n` after a round | Program exits with a goodbye message | Fill in after testing | Fill in |

## Testing Notes
Run every test and replace each placeholder with the actual result and Pass or Fail. If a test fails, describe the fix and repeat the test. Do not report a test as passed until you have run it.
