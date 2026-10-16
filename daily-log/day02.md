# Day 02 — 2026-10-16

**Time:** ___ min (10:57 se 14:30, beech ke breaks hata ke asli kaam)   **Roadmap task:** Loops + comprehensions + sorting (8 tests green) + DSA Valid Anagram

## Recall (bina dekhe)
- Kya likhne ki koshish ki: Aaj recall nahi hua (skip).
- Kitna sahi nikla (%): n/a

## Build
- Kya banaya: `python-fluency/d02_loops_sorting.py` mein 9 functions + tests: `even_squares`, `word_lengths`, `first_letters`, `sort_by_length`, `numbered`, `make_marks_dict`, `has_negative`, `all_positive`, `sort_students`. Edge cases (khaali list, 0) ke asserts bhi.
- Commit(s): 25b30e4 "Add Python loops and sorting practice"; baaki commits: ___ (day02 log, valid_anagram)

## Peek log (HONEST)
| Kya atka | Kahan dekha (template / docs / Google / AI) |
|---|---|
| `first_letters`: `words[0]` vs `word[0]`, loop galat cheez pe | AI (hint) |
| `numbered`: `enumerate` ko f-string mein seedha daala, comprehension mein kholna nahi aaya | AI (hint) |
| `make_marks_dict`: `zip` ka object return kiya, dict comprehension nahi soochi | AI (hint) |
| `sort_students` test: expected poore dicts hone chahiye the, sirf naam likhe | AI (exact assert line di gayi) |
| `all_positive`: 0 positive nahi hota, `>=` galat tha | AI (sawaal se dhyan aaya) |
| `any()` / `all()` ka concept | AI (example + explanation) |
| `Counter` ka use (Valid Anagram tareeka 2) | AI (explanation) |
| `pytest` install / run (`pytest` command nahi mila) | AI |
| `assert f(a, b)` ka shape (`a == b` argument ke andar daal diya, 3 baar) | AI (example) |
| `git add` naye file ke liye dobara chalana padta hai | AI |

## Errors aur fix
- `TypeError` (`even_squares(2)`: int pe loop) → list input diya
- `NameError: names not defined` (test mein) → test mein lists seedha likhi
- `NameError` k/K/i mismatch (`word_lengths`) → loop variable ek hi naam
- `AssertionError` (`first_letters`): `{'a','e','l','p'}` aaya → `words[0]` ki jagah `word[0]`
- `SyntaxError: cannot assign to function call` → `=` ki jagah `assert ... ==`
- `TypeError: 'bool' not iterable` → bracket galat jagah, `f([..]) == []`
- `TypeError: missing argument 't'` (`is_anagram('a'=='b')`) → `==` ki jagah `,`
- Duplicate test naam (`test_is_anagram` do baar) → doosra test chala hi nahi tha, `test_is_anagram2` kiya

## DSA
- Problem: Valid Anagram
- Signal → Pattern: do strings ke letters ki ginti barabar honi chahiye → hash map / counting (ya sorting)
- Khud se hua? (haan / hint / solution dekha): `sorted` wala tareeka khud se (haan). `Counter` wala tareeka hint ke baad (hint). Nested loop ka plan khud socha tha, code nahi likha.
- Time complexity: `sorted` wala O(n log n), `Counter` wala O(n)

## Confidence (1-5): ___
## Kal: Day 3 (functions + errors, Two Sum). Recall mein Day 2 ke 2-3 functions + `is_anagram` blank se. Pending: `requirement.txt` ka naam theek karna, aur `is_anagram` ke tests mein ek aur `True` case ("aab"/"aba") aur khaali strings ka assert.