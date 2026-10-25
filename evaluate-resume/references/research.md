# Research basis and limits

Verified: 2026-10-22. Use primary sources below as a starting point; revisit
vendor documentation for material current/platform-specific questions. These
sources support individual design choices, not validation of this 100-check
rubric or any universal resume score. Summaries are deliberately narrow.

## Official ATS documentation

### R1. Greenhouse — Unsuccessful resume parse

https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse

The vendor describes parsing as filling candidate-profile fields. It documents
potential trouble from image-only resumes, columns, tables, header/footer or
text-box contact details, unclear sections, and unusual character spacing. It
also documents a 2.5 MB parse limit. A failed parse can leave the document attached
and require manual field entry.

Apply: inspect actual extraction and entry associations; distinguish structure
risk from observed loss. Keep the stated limit specific to this product/version.
Do not infer application rejection or universal PDF/column failure.

### R2. Lever — Searching the Database for Candidates

https://help.lever.co/s/article/Searching-the-Database-for-Candidates

Lever documents keyword and field searching across parseable candidate-profile
content, including resumes, notes, and feedback. Search behavior and visibility
depend on the product's functionality and permissions.

Apply: use conventional relevant qualification names to improve discoverability.
This does not establish a universal exact-match requirement, hidden rejection
threshold, or value from repeating keywords. This source was retrievable through
indexed official text; live page rendering was not available during development.

### R3. Greenhouse — Talent Matching FAQ

https://support.greenhouse.io/hc/en-us/articles/41131886674075-Talent-Matching-FAQ

The documented feature compares resumes with recruiter-defined calibration
criteria and can map related terms to one skill. Adding more matching terms does
not necessarily increase a score. Its match categories support human review;
the feature does not itself advance or reject candidates.

Apply: distinguish lexical coverage from contextual match, deduplicate synonyms,
and make job-specific assumptions explicit. Do not generalize this feature's
workflow to every ATS, integration, or employer configuration.

### R4. Greenhouse — Auto-reject

https://support.greenhouse.io/hc/en-us/articles/360000653472-Auto-reject

Greenhouse separately documents configurable rejection rules triggered by
answers to custom application questions, including required-license examples.

Apply: keep stated conditions separate from resume wording. Never infer hidden
rules or assume more keywords can override a required condition. Never answer
an application question or infer personal status from a name, school, or location.

### R5. Oracle — Evaluate Candidate Applications Using AI Matching Ratings

https://docs.oracle.com/en/cloud/saas/talent-management/farqa/evaluate-candidate-applications-using-ai-matching-ratings.html

Oracle documents a Redwood feature with 0–5 ratings across education, experience,
skills, and profile, with configurable relative importance. Parsed resume
information can inform ratings; separate states include not rated and no data.

Apply: keep job-match dimensions and assessment completeness separate. Do not
present this skill's 0–2 editorial scale as Oracle's scoring or any vendor's
implementation. Configurable matching is evidence against assuming a shared
cross-vendor pass number; that conclusion is a synthesis, not a vendor quote.

### R6. Oracle — Understand Top Candidate Suggestions

https://docs.oracle.com/en/cloud/saas/talent-management/faush/understand-suggested-candidates.html

This distinct Oracle matching feature describes profile, education, experience,
and skills indicators; it uses structured fields and contextual information.
The documentation calls for further review of suggested candidates.

Apply: compare education, execution, scope, and skill evidence separately. Do not
conflate this feature's star indicators with the Redwood ratings in R5, general
resume quality, or an employer decision.

## Career guidance and empirical research

### R7. MIT CAPD — Career toolkit: Crafting an effective resume

https://capd.mit.edu/resources/career-toolkit-crafting-an-effective-resume/

MIT advises tailoring evidence to the role, presenting relevant paid or unpaid
work, using clear action/project/result descriptions, and making formatting
readable. Its guidance accommodates different experience levels and notes
first-pass scanning.

Apply: inspect evidence, concise bullets, hierarchy, and transferable work.
Treat the 10-second test and action/object/detail pattern as editorial tools;
do not claim a universal recruiter stopwatch, page rule, or ATS scoring formula.
A summary and numerical result in every bullet are not imposed by this rubric.

### R8. van Inwegen, Munyikwa, Horton — Algorithmic Writing Assistance on Jobseekers' Resumes Increases Hires

https://arxiv.org/abs/2301.08083

The authors report a randomized experiment among roughly 481,000 entrants to
an online labor platform. Writing assistance improved hiring probability by
about 8% relative to control in that setting, without evidence of lower employer
satisfaction. The intervention concerns writing clarity; it is not an evaluation
of this skill, keyword optimization, or mainstream ATS pass rates.

Apply: improve communication of existing facts. Do not promise an 8-percentage-
point gain, forecast any individual's outcome, or claim causal validation of
this rubric. The population, platform, intervention, and time window limit
generalization. Consult the actual version before quoting statistics.

## Method choices owned by this skill

Preserve the user's nine substantive categories and tenth priority workflow.
Expand them into 100 observable checks to support traceable review. Preserve
0/1/2; add NA and U as assessment states, not new performance scores. Use equal
weight within categories for arithmetic transparency, and no default overall
number. Treat these as designed conventions, not empirical ATS algorithms.

Apply these corrections to rigid resume folklore:

- Recommend exact standard terms when accurate; accept justified aliases and
  distinguish tool-specific requirements from transferable capability.
- Treat columns/tables as inspectable risks; do not declare automatic rejection.
- Evaluate output and appropriate scope without inventing numbers or upgrading
  collaborative contributions to leadership.
- Allow optional summaries, projects, and certifications to be inapplicable.
- Clarify transitions without penalizing gaps or requiring private explanations.
- Follow role, country, sector, and submission-specific instructions; do not
  turn US industry-resume conventions into rules for academic/federal/global CVs.

When an academic, federal, creative, or jurisdiction-specific application needs
a different document, identify that scope and adapt or route to the appropriate
workflow. Do not distort the required document merely to satisfy this rubric.
