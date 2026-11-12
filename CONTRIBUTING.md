# Contributing and maintaining sources

## Privacy first

This is a public repository. Do not add student identifiers or other personal or sensitive data, actual accommodation lists tied to a student, completed assignments, individualized plans, real records or case notes, credentials, or secure test content. Names are not the only identifiers. Use wholly fictional, non-identifying examples and public, authorized sources. Do not paste copyrighted materials without permission; link to official sources and summarize in your own words.

If sensitive information is accidentally committed, notify the repository owner immediately. Deleting it in a later commit does not remove it from history; follow the host's sensitive-data removal procedures and applicable incident policies.

## Evidence and updates

- Prefer official statutes, adopted rules, agency guidance, and official assessment documents. Label each as law/regulation, agency guidance, or nonbinding practical recommendation; link directly to the underlying source.
- Place links next to substantive claims. Identify jurisdiction, scope, relevant school year or administration, and the last verification date. Check source content, not just link availability.
- Separate classroom instruction from each assessment's particular rules. Do not generalize assessment-specific restrictions to all instruction.
- When sources conflict or a policy is changing, identify the uncertainty and seek the current authoritative source. Escalate legal interpretation to qualified professionals.
- Recheck time-sensitive assessment pages before each school year and test administration. Record changes and dates in the page or pull request; retire outdated instructions rather than silently presenting them as current.
- Keep examples hypothetical, distinguish legal requirements from implementation suggestions, and do not claim an app or a school is compliant on this repository's authority.

## Local checks

Run `python3 scripts/check_links.py` from the repository root. It checks Markdown relative links for missing local files, not external source accuracy, privacy, or legal correctness. Human review is still required.
