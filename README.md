# Dev Journey — Swaraj

42 din ka daily training: Python writing fluency → FastAPI backend (3 baar, har baar kam peeking) → real-world deploy → capstone. Saath mein roz 1 DSA problem.

**Ye repo khud proof hai.** Har din ka commit, har din ka log, har DSA problem ka test. GitHub ka green graph jhooth nahi bolta.

## Roz ka 2 ghante ka routine (fixed, negotiate mat kar)

| Time | Block | Rule |
|---|---|---|
| 0:00–0:15 | **Recall** | Kal ka kaam BINA dekhe `recall/` mein likh. Galat ho to bhi. |
| 0:15–1:15 | **Build** | ROADMAP ka aaj ka task. Code khud type kar. |
| 1:15–1:45 | **DSA** | 1 problem, 30 min timer. Function + test same file mein. |
| 1:45–2:00 | **Log + push** | `daily-log/dayNN.md` bhar, commit, push. |

## 5 rules

1. **Har din push.** 20 minute bhi kiya to push. Zero-commit din = streak tooti.
2. **Peek log honest.** Kahan template/AI/Google dekha, log mein likh. Ye shame nahi, ye tera syllabus hai.
3. **AI se code liya to commit message mein `[ai]` likh.** `progress.py` gin lega. Ratio har hafte girna chahiye.
4. **Test ke bina DSA "solved" nahi.** File mein `test_` function hona chahiye, CI green hona chahiye.
5. **Sunday = review.** Is hafte ke 3 DSA dobara, recall test, retro. Phir PROGRESS.md + repo link coach (Claude) ko bhej.

## Commands

```bash
python scripts/progress.py          # streak, days logged, DSA count, [ai] ratio
pytest dsa python-fluency -q         # practice tests
cd backend && pytest -q              # backend tests (Week 2 se)
```

## Structure

```
daily-log/       day00.md ... day42.md   (TEMPLATE.md copy kar)
python-fluency/  Week 1 drills
backend/         Week 2-6 ka FastAPI kaam (har pass alag folder)
dsa/             <pattern>/<problem>.py  (function + test)
recall/          roz ke from-memory drills
design/          ER diagrams (kaagaz ki photo bhi chalegi)
```
