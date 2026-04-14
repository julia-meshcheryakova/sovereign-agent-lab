"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
All 3 conditions returned correct but different answers: both The Haymarket Vaults and The Albanach satisfy all constraints (capacity >= 160, vegan options, status = available). The model extracted the right answer when we used plain text, XML tags and the sandwich format, showing that Llama-3.3-70B handles simple extraction across formats.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The Holyrood Arms (capacity=160, vegan=yes, status=full) matches 2/3 constraints — all but status.
A model checking for capacity and vegan could easily pick it without carefully checking availability (last field and less specific).
The Guilford Arms, The New Town Vault, The Grain Store also match 2/3 but fail on vegan.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True

PART_C_PLAIN_ANSWER    = "Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Part C ran the same distractor dataset on a smaller model (Gemma 2 2B). All three conditions
still returned correct answers (Haymarket Vaults).
The only difference was that in plain format it didn't include "The" in the answer, which is not crucial this time. 
But depending on a task it might be a deal breaker, showing that strict formatting can still make a difference on smaller models.
"""


# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the model is weaker/smaller, the task is more complex, 
and the distractors are more similar to the correct answer.
On clean data, all formats might work even with a weaker model. But as context grows
longer, distractors multiply, structured formatting (XML tags, sandwich
repetition) gets more important.
"""
