"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = ["check_pub_availability", "calculate_catering_cost", "get_edinburgh_weather", "generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

# Optional — anything unexpected.
# If you used a non-default model via RESEARCH_MODEL env var, note it here.
# Example: "Used nvidia/nemotron-3-super-120b-a12b for the agent loop."
TASK_A_NOTES = "The agent checked The Albanach, it met all constraints, so it didn't check The Haymarket Vaults.It proceeded with catering, weather, and flyer generation."

# ── Task B ─────────────────────────────────────────────────────────────────
#
# The scaffold ships with a working generate_event_flyer that has two paths:
#
#   - Live mode: if FLYER_IMAGE_MODEL is set in .env, the tool calls that
#     model and returns a real image URL.
#   - Placeholder mode: otherwise (the default) the tool returns a
#     deterministic placehold.co URL with mode="placeholder".
#
# Both paths return success=True. Both count as "implemented" for grading.
# This is not the original Task B — the original asked you to write a direct
# FLUX image call, but Nebius removed FLUX on 2026-04-13. See CHANGELOG.md
# §Changed for why we pivoted the task.

# Did your run of the flyer tool produce a success=True result?
# (This will be True for both live and placeholder mode — both are valid.)
TASK_B_IMPLEMENTED = True

# Which path did your run take? "live" or "placeholder"
# Look for the "mode" field in the TOOL_RESULT output of Task B.
# If you didn't set FLYER_IMAGE_MODEL in .env, you will get "placeholder".
TASK_B_MODE = "placeholder"

# The image URL returned by the tool. Copy exactly from your terminal output.
# In placeholder mode this will be a placehold.co URL.
# In live mode it will be a provider CDN URL.
TASK_B_IMAGE_URL = "https://placehold.co/1200x628/1a1a2e/eaeaea?text=The+Haymarket+Vaults+%7C+160+guests&id=2ef939fbbaf6"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# Why did the agent's behaviour NOT change when Nebius removed FLUX?
# One sentence. This is the point of the lesson.
TASK_B_WHY_AGENT_SURVIVED = """
Thanks to the graceful fallback pattern: we return a deterministic placeholder URL when no live image model.
"""

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
The agent received the tool result {\"success\": true, \"pub_name\": \"The Bow Bar\", \"address\": \"80 West Bow, Edinburgh\", \"capacity\": 80, \"vegan\": true, \"status\": \"full\", \"meets_all_constraints\": false}. It then called check_pub_availability for The Albanach as a fallback venue after seeing the failure result.
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
<think>\nOkay, let's see. The user is looking for a venue in Edinburgh that can accommodate 300 people and has vegan options. They provided four known venues: The Albanach, The Haymarket Vaults, The Guilford Arms, and The Bow Bar. I checked each one using the check_pub_availability function.\n\nFirst, The Albanach had a capacity of 180, which is too small. Then The Haymarket Vaults with 160, also too small. The Guilford Arms had 200 capacity but didn't offer vegan options. Finally, The Bow Bar has 80 capacity and vegan options but is already full. None of the venues meet both the capacity and availability requirements. The user might need to consider other venues outside the known list or adjust their event size. Since the task was to check the provided venues, I should inform them that none are suitable and suggest alternatives if possible.\n</think>\n\nNone of the known Edinburgh venues can accommodate 300 guests with vegan options. The maximum capacity among the checked venues is 200 (The Guilford Arms), but it lacks vegan options. The Bow Bar has vegan options but only 80 capacity and is already full. You may need to consider alternative venues or adjust event requirements."""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False

SCENARIO_3_RESPONSE = "I don't have access to real-time train schedules or transportation data. For the most accurate information about the last train from Edinburgh Waverley to London, I recommend checking:\n1. The National Rail website (https://www.nationalrail.co.uk)\n2. Train service apps like Citymapper or Trainline\n3. The specific train operator's website (e.g., LNER)\n\nWould you like help with anything related to Edinburgh pubs, weather, or event planning instead?"

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
Yes. The agent correctly recognised that it doesn't have train schedules tool capability and declined gracefully instead of hallucinating. It also provided reliable sources and offered to help within its actual scope. A real booking assistant should never fabricate transport information that could cause someone to miss a train.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
	__start__([<p>__start__</p>]):::first
	agent(agent)
	tools(tools)
	__end__([<p>__end__</p>]):::last
	__start__ --> agent;
	agent -.-> __end__;
	agent -.-> tools;
	tools --> agent;
	classDef default fill:#f2f0ff,line-height:1.2
	classDef first fill-opacity:0
	classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/flows.yml. Min 30 words.
TASK_D_COMPARISON = """
The LangGraph graph is a single loop "agent-tools": all calls are determined in runtime. Rasa CALM predefines a range of possible tasks explicitly. The LLM decides which flow to select; then steps are executed deterministically, making it auditable.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
In Task A the agent only checked The Albanach and never checked The Haymarket Vaults, even though the prompt included both venues. Once The Albanach returned meets_all_constraints: true, the agent skipped checking the 2nd venue and proceeded directly to the other steps. Autonomous loop making decisions was efficient, but it silently dropped part of the original instruction.
"""