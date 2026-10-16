# Day 02 — 2026-10-16

**Time:** ___ min   **Roadmap task:** Loops + comprehensions + sorting (8 tests green)

## Recall (bina dekhe)
- Kya likhne ki koshish ki: Aaj recall nahi hua (skip).
- Kitna sahi nikla (%): n/a

## Build
- Kya banaya: `python-fluency/d02_loops_sorting.py` mein 9 functions + tests: `even_squares`, `word_lengths`, `first_letters`, `sort_by_length`, `numbered`, `make_marks_dict`, `has_negative`, `all_positive`, `sort_students`. Edge cases (khaali list, 0) ke asserts bhi.
- Commit(s): 25b30e4 "Add Python loops and sorting practice"

## Peek log (HONEST)
| Kya atka | Kahan dekha (template / docs / Google / AI) |
|---|---|
| `first_letters`: `words[0]` vs `word[0]` (loop galat cheez pe) | AI (hint) |
| `numbered`: `enumerate` ko f-string mein seedha daala, comprehension mein kholna nahi aaya | AI (hint) |
| `make_marks_dict`: `zip` ka object return kiya, dict comprehension nahi soochi | AI (hint) |
| `sort_students` test: expected poore dicts hone chahiye the, sirf naam likhe | AI (exact assert line di gayi) |
| `all_positive`: 0 positive nahi hota, `>=` galat tha | AI (sawaal se dhyan aaya) |
| pytest install/run (`pytest` command nahi mila) | AI |

## Errors aur fix
- `TypeError` (`even_squares(2)`: int pe loop) → list input diya
- `NameError: names not defined` → test mein lists seedha likhi
- `NameError: k/K/i` mismatch (word_lengths) → loop variable ek hi naam
- `SyntaxError: cannot assign to function call` → `=` ki jagah `assert ... ==`
- `TypeError: 'bool' not iterable` → bracket galat jagah (`f([..]==[])`), `f([..]) == []`
- `AssertionError` set/list/dict type mismatch → expected ka type function ke return type se match kiya

## DSA
- Problem: Valid Anagram (abhi baaki)
- Signal → Pattern: ___ (hash map / counting)
- Khud se hua? (haan / hint / solution dekha): ___
- Time complexity: ___

## Confidence (1-5): ___
## Kal: Day 3 (functions + errors) + recall mein Day 2 ke 2-3 functions blank se