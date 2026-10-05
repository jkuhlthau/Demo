# Proposed study protocol — not executed or preregistered

## Cases and reference answers
Independently specify crop, crop year, decision timestamp, location geometry and CRS, practice/type, producer facts relevant to eligibility, and case family. Start with a bounded human-approved corn/soybean scope near Ames; do not assume a farm's county or eligibility. An insurance reviewer and GIS reviewer must author or check labels from source clauses/rows and geometry before seeing workflow answers, with adjudication of disagreements. Record eligible, ineligible and indeterminate products and acceptable alternative answer sets. No model-generated answer or baseline output is ground truth.

## Arms

| Arm | Sources | GIS | Action selection |
|---|---|---|---|
| Agentic GeoAI | Frozen as-of documents and data | Approved identical toolset | One agent adapts within budget |
| Fixed GIS plus rules | Same documents and data | Same approved toolset | Competent predefined sequence and frozen rules |
| Text-only retrieval | Same eligible textual sources | None; no computed GIS result injected | Retrieval/synthesis under the same language-model budget |

Match model/version for language-model components, development effort, source snapshots and cost ceilings. Document deterministic baseline components. Freeze workflow versions before test access. Include ordinary lookup and independently justified spatial challenge strata; analyze them separately. Log tool calls, errors, retries, tokens, runtime and cost.

## Output schema
Each product decision contains product ID/name, eligible/ineligible/indeterminate status, case facts used, source ID and exact clause/row, crop-year/version, release/effective dates, required spatial evidence, and unresolved facts. An overall shortlist includes only confirmed eligible products; indeterminate candidates remain visibly separate.

## Spatial and temporal validity
Verify county and parcel assignment from authoritative boundaries with CRS/datum and transformation metadata. Use an appropriate local projected CRS for areas/distances after checking scope; test positional uncertainty near boundaries. Do not introduce hazard processing unless an operative rule requires it. Record original scale/support and avoid county-to-farm outcome inference. Exclude data released after the decision timestamp, even if retrospectively labeled for the same year. Current product descriptions are insufficient historical evidence.

## Primary outcome and refusal
Primary contrast: paired difference in strict case correctness, agent versus fixed workflow, at a prespecified common coverage operating point chosen using development cases. Strict correctness requires an acceptable entire shortlist, valid supporting evidence, and appropriately identified indeterminate products; plausible prose is insufficient. Lock confidence ranking, coverage level, tie rules and abstention scoring before test access. Report unconditional strict correctness, achieved coverage, false eligible products, citation validity, and secondary text-only results. If matched coverage cannot be achieved by the frozen procedure, report it and do not substitute a favorable metric.

## Dependence, thresholds, and uncertainty
Split development/test by independent case families; keep near-duplicate locations, shared provisions and related dates together. Repeated runs are summarized within case, not counted as additional independent cases. Estimate paired uncertainty by resampling independent families when enough groups exist; otherwise give descriptive feasibility only. Choose sample size from development precision estimates. Human review must freeze minimum useful gain and false-eligibility guardrail before testing. No numerical threshold has been approved.

## Decision rule and falsification
Superiority requires the prespecified useful-gain criterion and false-eligibility guardrail, with coverage accounted for. An upper interval bound below the useful-gain margin contradicts useful improvement; wide intervals are inconclusive. Failure of the false-eligibility guardrail defeats the combined success criterion. Beating text-only retrieval alone does not establish value from adaptive action selection.

## Current execution gate
Independent cases: zero verified in this run. Historical rules: no complete case snapshot retrieved. Spatial calculations: none executed. Benchmark arms: not implemented or run. Next action: adjudicate one worked case, confirm data feasibility and freeze human-approved scope before implementing the three empirical workflows.
