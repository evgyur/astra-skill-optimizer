# Applying OpenAI's Astra guidance

Source: [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra), OpenAI Developers.

These are attributed vendor recommendations, adapted as audit questions, not measured results for this optimizer. The source's claims about Astra's judgment are not a reason to remove safety controls. Do not copy a Codex-specific index limit into Hermes; inspect the actual runtime.

## 1. Trigger specificity

Descriptions should identify the operation, not an entire domain. Example: a migration skill should match creating or reviewing a schema migration, not reading a row from a database. Record an in-scope prompt, an out-of-scope prompt and a neighboring task that should select another skill. Check visible descriptions for truncation and competing/contradictory triggers. Keep the distinction that makes routing useful even when shortening text.

## 2. Instruction surfaces

Inspect only applicable skill files, inherited/local AGENTS.md instructions and the actual task prompt in the authorized workspace. Record which surface owns each conflicting requirement and which is in edit scope. A skill-only request permits reporting an AGENTS.md conflict, not rewriting that file. Missing access stays an explicit limitation. Never weaken higher-priority policy to make a skill appear compatible.

## 3. Contextual loading

Replace unconditional reading lists with task-specific pointers: architecture for boundary changes, schema guidance for migrations, deployment instructions for deployment. A typo should not trigger a full repository map. Keep the root a minimal router, with essential safety and output contracts visible. Distinguish helpful domain recipes from a rigid itinerary that prevents the model choosing a simpler valid path.

## 4. Proportional verification

Preserve tests and completion proof. Start with checks relevant to the changed behavior; broaden for affected interfaces, repository policy or blast radius. Do not require a full suite after each harmless edit merely as reassurance. Conversely, do not delete verification because the source says Astra checks its own work. Any optimization claim needs observed old/new evidence.

## 5. Decision boundaries

Separate safe continuation from protected effects. An approved bounded implementation can include fixing failures caused by that change and rerunning affected tests. Before calling a test disposable or production-isolated, verify fixtures, endpoints and permissions; do not infer safety from a filename. New spend, publication, access, destructive data changes and other excluded effects still need exact authority. Unrelated failures are reported, not silently repaired.

## 6. Persistence and stop conditions

Define done before starting: required artifact, execution, inspection, affected-test results and any authorized delivery/readback. First implementation or a local commit is not completion when the approved goal includes a working result. Remove unnecessary intermediate approval requests only within existing authority. Preserve explicitly requested review checkpoints, audit-only boundaries and real blockers. Exploration needs a named objective and stop condition, not an unlimited keep-going instruction.

## 7. Mixed-model compatibility

Record all declared consumers. Shared instructions may also serve Sol, Luna or another model. Evaluate changed guidance against those consumers when required by the compatibility contract; do not silently remove support because the current session uses Astra. Model-specific recommendations should be conditional, not universal assumptions.

## Required audit record

For each finding record surface, evidence, proposed change, in-scope/out-of-scope, preserved contract and verification. Include trigger cases, contextual-reading decisions, verification scope and completion/approval boundaries. If instructions were improved but no model runs occurred, report static validation only and leave behavioral improvement unproven.
