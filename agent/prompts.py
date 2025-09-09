def planner_prompt(user_prompt: str) -> str:
    PLANNER_PROMPT = F"""
    you are the PLANNER agent. Convert the user prompt into components

User request:
{user_prompt}    

"""
    return PLANNER_PROMPT