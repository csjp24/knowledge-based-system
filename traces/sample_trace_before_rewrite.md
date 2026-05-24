# Sample Traces Before Rewrite
These are intentionally problematic traces. Each member uses one section to show what the AI did wrong before the GDVRR rewrite.

# Member 1 - S1: Sensory Priority Conflict
Scenario: Adam is in a crowded cafeteria with bright lights. A classmate says hello, but Adam looks away and answers in a flat tone. The classmate thinks Adam is rude. Adam starts covering his ears.

# Problematic AI Trace
Thought: Adam misunderstood the social cue and should learn that eye contact is polite.

Action: Social_Cue_Breakdown

Observation: Tell Adam to look at the classmate, smile, and say hello in a friendly voice.

# Why This Is Problematic
The AI focused on social performance before checking sensory distress. Adam is covering his ears in a crowded and bright environment, so the expert-derived sensory rule should have priority.

Anomaly keyword: Rule Subsumption / Priority Conflict

Applicable expert rules: R4, R10, R11

# Member 2 - S2: Hyperfixation and Refusal to Move On
Scenario: Mira keeps talking about train schedules. The teacher wants to move to the next activity, but Mira repeats the same train facts again and again.

# Problematic AI Trace
Thought: Mira is repeating the same topic, so I should keep encouraging her to move to the next activity.

Action: Transition_Support

Observation: Tell Mira, "We are finished with trains now. Please move to the next activity."

# Why This Is Problematic
The AI tries to force a transition even though the expert said that repeated-loop fixation should not be forced. It also fails to use the stop-session rule when redirection does not work.

Anomaly keyword: Procedural Routing Failure

Applicable expert rules: R5, R8, R9

# Member 3 - S4: Meltdown Support Sequence
Scenario: A child was lining up toy cars. Another child moved one car. The child screams, cries, and drops to the floor, but is not hurting anyone.

# Problematic AI Trace
Thought: The child should understand that screaming is not appropriate and should apologize.

Action: Social_Cue_Breakdown

Observation: Explain that screaming is wrong and ask the child to say sorry to the other child.

# Why This Is Problematic
The AI gives a social explanation during a meltdown. The expert said the caregiver should stay calm, avoid yelling or force, allow safe self-regulation, and explain only after the child is calm.

Anomaly keyword: Premature Convergence / Procedural Routing Failure

Applicable expert rules: R5, R6, R7, R11

# Member 4 - S5: Long Instructions and Communication Style
Scenario: A teacher gives Daniel a long explanation with many instructions at once. Daniel looks confused and stops responding.

# Problematic AI Trace
Thought: Daniel needs a supportive explanation, so I will explain the full task carefully.

Action: Final_Response

Observation: Give Daniel a long paragraph explaining why the task matters, what he should do first, what he should do next, and how he should ask for help if confused.

# Why This Is Problematic
The AI uses long instructions even though the expert said autistic individuals may not process long or flowery explanations well. The AI also fails to break the task into one clear step.

Anomaly keyword: Working Memory Degradation / Format Constraint Failure

Applicable expert rules: R1, R2, R3

# Member 5 - S3: Task Transition and Step Chunking
Scenario: A student completed questions 1 to 3. The teacher wants the student to continue with questions 4 to 6 without causing overwhelm.

# Problematic AI Trace
Thought: The student has completed the first set, so I can give the rest of the worksheet now.

Action: Final_Response

Observation: Tell the student to continue with questions 4 to 10 and finish the worksheet before the session ends.

# Why This Is Problematic
The AI gives too many tasks at once. The expert said instructions should be broken into smaller sets and paced slowly according to the individual condition.

Anomaly keyword: Procedural Routing Failure / Format Constraint Failure

Applicable expert rules: R1, R2, R3
