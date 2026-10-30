---
type: community
cohesion: 0.25
members: 8
---

# TestAnswerGroundingValidation

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-test_detects_hallucinated_claims_low_grounding_score()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_evaluate_output_grounding_flags_ungrounded_content()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_grounded_answer_scores_high()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[Accurate answer derived from context achieves high grounding score.]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Hallucinated content not supported by context scores below minimum grounding…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[TestAnswerGroundingValidation]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[Verify lexical and numerical grounding validation detects hallucinated or…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[evaluate_output_grounding flags ungrounded claims and classifies as…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAnswerGroundingValidation
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_ViolationType]]
- 2 edges to [[_COMMUNITY_RetrievedChunkOutput]]
- 1 edge to [[_COMMUNITY_test_guardrails_adversarial.py]]

## Top bridge nodes
- [[TestAnswerGroundingValidation]] - degree 8, connects to 3 communities
- [[dot-test_evaluate_output_grounding_flags_ungrounded_content()]] - degree 4, connects to 2 communities
- [[dot-test_detects_hallucinated_claims_low_grounding_score()]] - degree 3, connects to 1 community
- [[dot-test_grounded_answer_scores_high()]] - degree 3, connects to 1 community