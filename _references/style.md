# Style

Write all step prose in Simplified Technical English (ASD-STE100 style). The goal is short, plain, clear instructions. No filler. No clever words.

## Rules

- Be terse.
- Write one instruction per sentence.
- Keep sentences short. Aim for 15 words or less. 20 is the ceiling.
- Use the imperative. "Read the file." "Write the output."
- Use active voice. Not passive.
- Use simple words. Prefer the common word over the fancy one.
- Use numbered steps, not paragraphs, for a sequence of actions.
- Cut hedging and adverbs: "carefully", "simply", "just", "please", "make sure to".
- Do not explain why, unless the reason changes what the reader does.
- Use the same word for the same thing every time. Do not vary it for style.

## Word swaps

Prefer the left, not the right.

- use — not utilize, leverage
- start — not initiate, commence
- end — not terminate
- make — not generate, produce (when a plain verb fits)
- get — not obtain, acquire, retrieve (when plain fits)
- about — not regarding, concerning
- help — not facilitate, assist

## Check

`lint` flags:

- Sentences over 20 words (soft flag).
- Banned hedge words.
- Fancy words with a simple swap.
- Paragraphs where a numbered list fits.
