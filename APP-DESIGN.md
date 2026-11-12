# Future app: scope and safeguards

This is a proposed design, not a claim that an app exists or has been approved by a school district. Last reviewed: November 12, 2026.

## Purpose

A teacher supplies a **blank assignment** and a list of desired accommodations. The system produces an editable draft and a change report for review. The human reviewer remains responsible for verifying the draft and applying the student's actual plan and district procedures.

## Boundaries

- No student names, identifiers, completed work, IEPs, 504 plans, diagnoses, or sensitive personal information in this public repository or intended app inputs. Accommodation lists can themselves be identifying in context: inspect all materials and metadata, and follow district policy.
- Do not make eligibility or disability determinations, select accommodations independently, claim legal compliance, or replace educators and school decision-making teams.
- Preserve questions, factual meaning, learning objectives, and the skill being measured unless the responsible educator explicitly directs and authorizes a change. Do not supply answers. Flag uncertainty rather than guessing; an ambiguous rewrite requires review.
- Distinguish document changes from supports needing human administration, such as extended time, a separate setting, breaks, or a reader. Report the latter as actions for staff, not as completed accommodations.
- Do not alter secure or standardized assessments. Classroom practice and assessment rules are different; refer questions to the campus testing coordinator.
- Output should be editable and include a change log, warnings, unresolved questions, and a clear teacher-review requirement. OCR or conversion errors must be checked against the original.
- Before any deployment, assess access, retention, logs, backups, third-party processing, encryption, and incident response against district policies and applicable law. Removing names does not itself establish compliance.

## Example workflow

1. Teacher checks that the blank assignment and instructions contain no personal or sensitive information and that use is authorized.
2. System creates an editable draft without answering the assignment, identifies requested changes, and flags human-administered supports.
3. Teacher compares the draft against the original, checks the intended learning target and directions, resolves warnings, and approves or revises it.
4. The school handles delivery and any student records in its authorized systems.
