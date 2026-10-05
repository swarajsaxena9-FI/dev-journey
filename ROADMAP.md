# 42-Day Roadmap

Har din = Recall (15m) + Build (60m) + DSA (30m) + Log (15m). Sunday = review.
"Done check" pura nahi hua to agle din wahi continue kar. Roadmap peeche khisakna theek hai, skip karna nahi.

---

## Day 0 — Setup (aaj hi)
- GitHub pe `dev-journey` repo bana (public: portfolio banega). Ye zip ka content push kar.
- Seekh: `git clone`, `git status`, `git add`, `git commit -m`, `git push`, `git log --oneline`.
- VS Code + `python -m venv .venv` + `pip install pytest`.
- **Done check:** pehla commit push hua, GitHub Actions tab mein green tick.

---

## Week 1 — Python likhna (padhna nahi, LIKHNA)
Kaam: `python-fluency/dNN_topic.py`. Har task ek function + uska `test_` function.

| Day | Build (60m) | DSA (30m) | Done check |
|---|---|---|---|
| 1 | **Containers:** list/dict/set/tuple ke 10 tasks — dedupe, word frequency (dict se, phir `Counter` se), grouping (`defaultdict`), 2 lists ka common/difference (set), dict invert, nested dict access | Contains Duplicate | 10 tests green |
| 2 | **Loops + comprehensions + sorting:** list/dict/set comprehension, `sorted(key=lambda)`, `enumerate`, `zip`, `any/all`, records ki list ko 2 keys se sort | Valid Anagram | 8 tests green |
| 3 | **Functions + errors:** type hints, defaults, keyword-only `*`, `*args/**kwargs`, multiple return (tuple), `raise ValueError`, `try/except/finally`, custom exception class | Two Sum | 8 tests, 3 error-case tests |
| 4 | **Classes:** `__init__`, instance method, `@property`, `@classmethod`, `@staticmethod`, `__repr__`, `@dataclass`, `Enum`. Ek `BankAccount` (deposit/withdraw, overdraft pe error) | Group Anagrams | Class + 6 tests |
| 5 | **Modules + imports:** Day 1–4 ko package banao (`__init__.py`), relative vs absolute import, `if __name__ == "__main__"` | Top K Frequent Elements | `pytest python-fluency` green |
| 6 | **Mini Library (pure Python, koi framework nahi):** `Book`, `Member`, `Library` classes. Rules: basic max 3, premium max 5 books, issued book dobara issue nahi, return twice error. Enums for status/membership | Product of Array Except Self | 6 rule-tests green |
| 7 | **Sunday:** Day 6 ka `Library` class blank file mein memory se likh (recall/). Re-solve Day 1, 3, 5 DSA bina dekhe. Retro likh. | — | PROGRESS.md updated, coach ko bheja |

---

## Week 2 — FastAPI Template, Pass 1 (dekh-dekh ke, lekin TYPE karke)
Kaam: `backend/pass1/`. Template zip side mein khula rakh. Copy-paste BAN, har line type kar aur comment mein apne shabdon mein likh kya karti hai.

| Day | Build | DSA | Done check |
|---|---|---|---|
| 8 | Skeleton + venv + requirements + `core/config.py` + `db/session.py` + `db/base.py` | Valid Palindrome | App import hota hai bina error |
| 9 | `models/user.py`, `models/item.py`, `models/__init__.py`, Alembic init + first migration | Two Sum II | `alembic upgrade head` chala, tables bani |
| 10 | `schemas/` — common, user, item (4-schema pattern) | 3Sum | Python shell mein schema se galat data reject hota dikha |
| 11 | `crud/user.py`, `crud/item.py` | Container With Most Water | Ek script se create/get/update/delete chala ke dikha |
| 12 | `core/security.py`, `core/exceptions.py`, `services/auth_service.py`, `services/item_service.py` | Longest Consecutive Sequence | — |
| 13 | `api/deps.py`, routes, `router.py`, `main.py` | Best Time to Buy and Sell Stock | Swagger pe register → login → item CRUD |
| 14 | **Sunday:** `tests/` likh, sab green. Recall: `deps.py` memory se. Re-solve 3 DSA. Retro. | — | backend CI green |

---

## Week 3 — Pass 2: Library domain (minimum peeking)
Kaam: `backend/pass2-library/`. Template sirf atakne pe khol, aur peek-log mein likh.

| Day | Build | DSA | Done check |
|---|---|---|---|
| 15 | Requirements + rules list + ER diagram (Book, Member, Loan) → `design/library.md` / photo. **Code zero.** | Longest Substring Without Repeating Characters | Relationships + har rule likhe hue |
| 16 | Models (Loan: `due_date`, `returned_at`, FKs) + enums + migration | Longest Repeating Character Replacement | Migration chala |
| 17 | Schemas + crud — 3 entities | Valid Parentheses | — |
| 18 | `loan_service.py` **[MANUAL]**: issue, return, limits (3/5), already issued, overdue check | Min Stack | Service functions ready |
| 19 | Routes + router + Swagger end-to-end | Daily Temperatures | Swagger pe full flow |
| 20 | Har rule ka test (limit, double-issue, double-return, doosre member ki loan) | Evaluate Reverse Polish Notation | 10+ tests green |
| 21 | **Sunday:** recall `crud/item.py` + `schemas/item.py` memory se. Peek-log padh, top 3 gaps likh. Re-solve 3. Retro. | — | Coach ko bheja |

---

## Week 4 — Pass 3: Blank page, naya domain, stopwatch on
Domain: **Event Booking** (User, Event, Booking). Rules: capacity se zyada booking nahi, ek user ek event double book nahi, event se 24h pehle tak hi cancel.
Kaam: `backend/pass3-events/`

| Day | Build | DSA | Done check |
|---|---|---|---|
| 22 | Requirements + ER + rules. Code zero. | Binary Search | `design/events.md` |
| 23 | **Timed:** poora skeleton (config, db, main, deps) memory se, 60 min. Jo nahi aaya, peek-log. | Search a 2D Matrix | App boot hota hai |
| 24 | Models + migration + schemas | Koko Eating Bananas | — |
| 25 | Crud + `booking_service.py`. **Naya concept:** booking create + seats update ek hi transaction mein (commit crud se nikal ke service mein) | Find Minimum in Rotated Sorted Array | — |
| 26 | Routes + tests (capacity, double booking, late cancel) | Reverse Linked List | Tests green |
| 27 | Peek-log se top gaps ke recall drills `recall/` mein | Merge Two Sorted Lists | — |
| 28 | **Sunday:** Pass 1 vs Pass 3 ka peek-log compare kar. Re-solve 3. Retro. | — | Coach ko bheja |

---

## Week 5 — Real world (jo tutorials nahi sikhate)
Kaam: `backend/pass3-events/` pe hi aage.

| Day | Build | DSA | Done check |
|---|---|---|---|
| 29 | Postgres Docker mein, `DATABASE_URL` switch, migrations Postgres pe | Linked List Cycle | App Postgres pe chal raha |
| 30 | Logging setup (har request + har error log), `print` hatao | Remove Nth Node From End of List | Logs file/console mein |
| 31 | File upload endpoint (event poster): size + type validation | Invert Binary Tree | Galat file reject |
| 32 | `BackgroundTasks`: booking pe confirmation "email" (abhi log hi kaafi) | Maximum Depth of Binary Tree | — |
| 33 | `Dockerfile` + `docker-compose.yml` (app + db) | Same Tree | `docker compose up` se poora chal |
| 34 | Deploy (Azure App Service ya Render free tier), secrets env vars mein | Binary Tree Level Order Traversal | Public URL pe `/health` ok |
| 35 | **Sunday:** re-solve 3, retro | — | Coach ko bheja |

---

## Week 6 — Capstone (tera Project 4)
Domain tu chun, aisa jo asli mein kisi ke kaam aaye. Kaam: `backend/capstone-<naam>/`. AI sirf review ke liye, likhne ke liye nahi.

| Day | Build | DSA | Done check |
|---|---|---|---|
| 36 | Requirements doc + ER + rules | Kth Largest Element in a Stream | Coach ne design approve kiya |
| 37 | Models + migrations + schemas | Last Stone Weight | — |
| 38 | Crud + services | K Closest Points to Origin | — |
| 39 | Routes + auth + roles (RoleChecker) | Lowest Common Ancestor of a BST | — |
| 40 | Tests + CI green | Validate Binary Search Tree | Coverage of every rule |
| 41 | Deploy + README (setup, API list, screenshots) | **Mock:** 2 unseen mediums, 45 min each | Live URL |
| 42 | **Retro:** Day 1 vs Day 42. `progress.py` output. Repo link coach ko full code review ke liye. | — | Agla 42-din plan |
