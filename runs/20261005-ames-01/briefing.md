# Ames crop-insurance research briefing

Run ID: `20261005-ames-01`

Date: 5 October 2026 (America/New_York)

Verification phrase: `Ames evidence before eligibility 20261005`

Status: first bounded investigation completed; empirical comparison not performed.

## Spoken briefing
Our research question asks whether an agentic GeoAI workflow can produce more correct, evidence-supported Federal crop insurance shortlists for independently specified crop, location, and decision-date cases near Ames than either text-only retrieval or a fixed GIS-plus-rules workflow. The investigation has established a defensible next step, but it has not answered that performance question. We have no independently adjudicated cases, no complete historical policy snapshot for a case, and no executed comparison among the three workflows.

The first evidence comes from official Risk Management Agency sources. Their insurance overview distinguishes individual yield and revenue coverage from area-based insurance. Their insurance-cycle guidance points to actuarial documents for the relevant crop, plan, location, and practice, and for application deadlines. The dates-report interface offers useful filters, but we did not submit a query or retrieve an actual case result. These pages identify where verification should begin. They do not establish a particular farm's eligibility, especially for a past decision date.

The second evidence comes from three inspected research abstracts. Paper one, GISAgentBench, describes realistic GIS tasks with executable reference outputs. Paper two, GeoAgentBench, addresses tool execution and adaptive responses to failures. Paper three, an earlier GeoAgent study, combines retrieval and computational tools for geospatial analysis. These are competing contributions. They make a broad claim that agents can improve GIS an inadequate novelty argument. We read abstracts and metadata, not full methods, so we cannot yet compare their complete experimental designs or adopt their reported outcomes as insurance evidence.

My interpretation is that the promising contribution lies in disciplined insurance screening: independent answers, historical source control, verified spatial assignment, exact supporting clauses, and honest uncertainty. That is a candidate contribution, not verified novelty. Your Week Five critic already identified the same practical obstacles, including missing operative rules and independent labels. This investigation supports keeping those obstacles visible rather than filling them with plausible model answers.

The primary experiment should compare the adaptive agent against a competent, frozen GIS and rules workflow with the same permitted sources and tools. Text-only retrieval is a useful secondary comparison, but beating it might merely show the benefit of access to spatial information. We should include both ordinary administrative lookups and cases where spatial reasoning is independently justified. If most decisions require only a simple county lookup, fixed rules could be equally accurate and cheaper. That outcome would weaken the case for adaptive execution.

Correctness must mean an acceptable whole shortlist with valid evidence, not persuasive wording. Missing decisive facts should lead to an indeterminate decision. We must report coverage alongside correctness so that an agent cannot appear successful simply by refusing difficult cases. Related cases and repeated runs cannot count as independent observations. The minimum useful improvement and tolerance for false eligibility claims must be decided before test results are available.

The immediate scientific action is to complete one independently authored and adjudicated worked case. Verify its crop year, location, decision timestamp, relevant producer facts, operative provisions, and necessary geometry. Then determine whether enough independent case families and historical evidence exist for a credible benchmark. For our voice discussion, please choose the initial crop and year scope, identify a qualified independent reviewer, and discuss what improvement would justify the extra complexity. Until those gates pass, the strongest result is a transparent feasibility assessment, not a claim that an agent recommends better insurance.

## References and preserved artifacts

- P01: [GISAgentBench](https://arxiv.org/abs/2608.01645), abstract only.
- P02: [GeoAgentBench](https://arxiv.org/abs/2604.13888), abstract only.
- P03: [An LLM Agent for Automatic Geospatial Data Analysis](https://arxiv.org/abs/2410.18792), abstract only.
- O01: [RMA Insurance Plans](https://www.rma.usda.gov/about-crop-insurance/managing-farm-risk/insurance-plans).
- O02: [RMA Insurance Cycle](https://legacy.rma.usda.gov/policies/cycle/insurance_cycle.html).
- O03: [RMA Insurance Offer Dates](https://webapp.rma.usda.gov/apps/RIRS/InsuranceOfferDates.aspx), interface only.

Preserved run: runs/20261005-ames-01/. Read activity_log.md for actual actions, literature_evidence.md for access limits, gap_assessment.md for competing explanations, study_protocol.md for the proposed benchmark, and feasibility_matrix.csv for the unpopulated case template. No empirical performance, novelty, causal effect, policy relevance, or external validity is established.
