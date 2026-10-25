# Scoring and evidence rules

## Anchors

| Value | Meaning | Required reasoning |
| --- | --- | --- |
| 0 | Absent or unclear in inspectable material | Identify the searched scope or ambiguous/contradictory statement; do not assert lack of underlying ability. |
| 1 | Present but weak, incomplete, indirect, or inconsistent | Identify the claim and the specific evidence, context, or scope missing. |
| 2 | Clear, relevant, and supported for this check | Cite a precise resume locator and explain why it meets the check at the target level. |
| NA | Not applicable | Explain the contextual reason; an optional feature need not exist. |
| U | Unable to assess | Name the missing input or unavailable inspection; do not replace with zero. |

Apply 0/1/2 to document evidence. A 2 is not a background check. Distinguish a
candidate statement from inspected code/output, an external artifact, or an
independently verified fact. Do not demand private employer files or confidential
work samples to make a resume defensible. Flag material contradictions before
scoring; do not silently choose the most favorable version.

For a requirement, distinguish lexical presence from contextual adequacy:

- `Skills: SQL` supplies a term and a self-reported skill; normally evidence 1
  for a requirement to perform SQL analysis.
- A bullet identifying actual SQL analysis, its object and useful output may
  supply evidence 2 if scope matches the requirement. A number is not required.
- A correctly labeled expected degree can supply education evidence 2 for a
  student internship requiring current enrollment. It does not establish a
  currently completed degree when that is explicitly required.
- Apply named alternatives once. Treat missing one of Python/R as no gap when
  the JD explicitly accepts either and the other is supported.

For aggregate checks over multiple entries, use 2 when relevant entries are
consistently clear with no material exception; use 1 for mixed quality or a
material weak entry; use 0 when relevant evidence is generally absent/unclear.
Keep per-entry findings so this judgment is reviewable. Do not choose arbitrary
percent-of-bullets thresholds or reward having more bullets.

## Category results and coverage

For each of the nine domains:

```
points = sum(numeric scores)
possible = 2 * count(numeric scores)
observed_quality = 100 * points / possible
coverage = 100 * count(numeric scores) / (count(numeric scores) + count(U))
```

Exclude `NA` from both denominators. If no numeric rows exist, quality is
unavailable; if every row is `NA`, coverage is also unavailable. Show scored,
`NA`, and `U` counts. Label observed_quality **partial** whenever a domain has
`U`. For example, 6 points from 4 scored checks is 6/8; if two other applicable
checks are `U`, coverage is 4/6, not 100%. Missing inputs must not create an
apparently complete high score.

Do not average overlapping checks across domains as if they were independent
measures. Repeated evidence is acceptable for diagnostics; flag the shared cause
once in the fix list. Do not compare scores across different jobs, input modes,
or applicability decisions as objective candidate rankings.

## Optional overall number

Default to the category profile and requirement matrix. Only when requested,
compute the arithmetic mean of assessed category percentages with equal weight
per category. Disclose that this is a transparent **editorial convention**,
not research-validated weighting or an ATS simulation. Require every applicable
check to be assessable (`U` count zero). Exclude wholly `NA` domains, list the
remaining domain count, and show category denominators. Do not create pass/fail
thresholds, interview probabilities, or precision beyond one decimal place.

## Requirement coverage, separate from writing quality

Deduplicate requirements and count alternative groups once. Show required and
preferred separately. For each group retain the detailed evidence score and
source. Report at minimum:

- Contextually supported: number with evidence 2 / assessable requirement groups.
- Claimed/partial: number with evidence 1.
- Not evidenced/contradicted: number with evidence 0; keep those two labels distinct.
- Unknown: number unassessable; show separately, never silently exclude it.

Use factual entries rather than action bullets for degree/license facts. Do not
pool hard credentials with duties to obscure an unmet stated condition. Do not
use keyword repetition, a preferred skill surplus, or strong layout to compensate
for an unresolved required qualification. Never infer the employer's decision.

## Audit JSON and deterministic arithmetic

Use `scripts/score_audit.py --template` to generate all 100 rows. Replace each
`U` observation with the assessment. Keep records outside the installed skill;
never commit personal resumes or audit reports into the skill repository.

Each check object uses:

```json
{
  "id": "KW03",
  "score": 1,
  "evidence": "SQL appears only in Skills; reviewed all Experience and Projects entries.",
  "location": "Skills; Experience; Projects",
  "rationale": "The JD asks for SQL analysis; no application example is shown.",
  "fix": "If supported, identify the actual SQL task and output in its source role."
}
```

The file has top-level `rubric_version: "1.0"` and `checks: [...]`. Optional
metadata, requirements, bullet audits, and project findings may be kept alongside
them; the script calculates only the rubric checks. Provide score as an integer
0/1/2, or the exact string `NA`/`U`. Include every ID exactly once. For `NA`/`U`,
use location `not applicable`/`not inspected` and explain why. For zeroes, cite
the material reviewed. Use an explicit `fix` such as `None required` for passing
rows; do not leave reasoning empty.

Run the script with the audit path; add `--overall` only when the user requested
it. It rejects missing/duplicate/unknown IDs, invalid scores, empty observations,
and overall scoring with `U`. It does not evaluate qualification truth or
perform semantic matching; those are the agent's accountable judgments.
