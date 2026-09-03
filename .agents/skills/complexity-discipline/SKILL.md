---
name: complexity-discipline
description: Prevent code, test, CI, abstraction, and artifact-retention bloat. Use when implementing, reviewing, refactoring, or planning repository changes to enforce the smallest correct solution, avoid speculative engineering, keep tests and CI proportional, and prune stale generated artifacts.
---

# Complexity Discipline

Keep the repository correct, understandable, and maintainable without letting implementation scope, abstractions, tests, CI, or generated artifacts grow beyond demonstrated needs.

Require every addition to justify its maintenance cost with a current requirement. Default to the smallest correct implementation.

## Apply the core decision rule

Before adding code, tests, abstractions, configuration, defensive handling, CI, or infrastructure, ask:

> Is this necessary for a current, demonstrated requirement?

If not, do not add it.

Optimize in this order:

1. Correctness
2. Clarity
3. Simplicity
4. Maintainability
5. Extensibility

Do not optimize for hypothetical future requirements.

## Keep scope narrow

Implement only:

- What the task explicitly requires
- What is strictly necessary for that behavior to work correctly
- Realistic failure handling required by the current system

Do not add speculative features, optional capabilities, future-facing hooks, unnecessary configuration, generalized infrastructure, compatibility layers without demonstrated need, or unrelated refactors.

When uncertain, leave unrequested functionality unbuilt.

## Require demonstrated value from abstractions

Prefer simple, local, explicit code for one known use case. Do not add an interface, factory, registry, adapter, strategy layer, helper hierarchy, generic framework, generalized API, plugin system, or configuration layer solely for possible future reuse.

Create an abstraction only when at least one condition holds:

1. Demonstrated repetition exists.
2. The abstraction materially reduces current complexity.
3. Multiple real consumers require the shared contract.
4. The repository architecture explicitly requires it.

Prefer a small amount of clear duplication to premature abstraction.

## Handle realistic failures

Handle expected failures, external-system failures, user-input errors, persistence failures, network failures, and realistic edge cases.

Do not add unreachable fallbacks, speculative retries, redundant validation, defensive wrappers around trusted invariants, compatibility handling for unsupported configurations, or tests for impossible states.

Prefer enforcing an invariant to coding around violations that cannot occur under the current contract.

## Keep tests proportional

Add tests for important behavior, regressions, contracts, meaningful boundaries, realistic failure modes, and business-critical invariants.

Do not automatically add a test for every branch, helper, internal method, defensive condition, or refactor. Avoid substantially redundant tests and tests for speculative capabilities.

When behavior is unchanged, prefer updating or relying on existing behavioral tests. Do not let test complexity grow faster than product complexity.

## Keep CI proportional

Add workflows, jobs, matrices, operating systems, runtimes, validation stages, deployment gates, or artifact pipelines only when they protect a current repository requirement.

Prefer extending an existing check to creating a parallel workflow. Avoid equivalent validation in multiple jobs and coverage for unsupported environments.

Account for the runtime, maintenance, debugging, dependency churn, operational complexity, and storage cost of every CI addition.

## Retain generated artifacts deliberately

When generated-artifact maintenance is in scope, prevent build artifacts, reports, validation snapshots, temporary exports, test artifacts, generated indexes, automated analysis outputs, and versioned intermediates from growing indefinitely.

Default to retaining artifacts created within the last 30 days or the 10 most recent versions, whichever preserves the more useful recent history.

Never delete artifacts designated as releases, canonical references, baselines, approved snapshots, reproducibility requirements, audit records, or manually preserved artifacts.

Prune stale registry entries with obsolete artifacts when safe. Never leave a registry pointing to deleted files, and never silently delete an artifact whose retention status is ambiguous.

## Reuse existing infrastructure

Inspect the repository before creating a new mechanism. Prefer:

- Extending an existing command to adding a parallel command
- Updating an existing test suite to creating another suite
- Extending an existing workflow to creating another CI workflow
- Following an existing configuration convention to introducing a new system
- Updating an existing registry to creating another registry
- Using repository-native patterns to importing a framework

Do not duplicate infrastructure merely because new code is easier to write than existing code is to understand.

## Delete obsolete complexity

When a change makes code obsolete, remove it when safe. Do not retain unused helpers, dead compatibility layers, obsolete flags, abandoned abstractions, redundant tests, stale generated artifacts, or commented-out implementations just in case.

Use version control for implementation history.

## Run the planning gate

Before implementation, ask of every proposed component:

1. What current requirement requires this?
2. Does it have more than one demonstrated consumer?
3. Does it solve a real failure mode or an imagined one?
4. Can existing repository infrastructure handle it?
5. Would removing it still satisfy the task?

Remove components justified only by hypothetical reuse, architectural elegance without current benefit, defensive completeness, imagined scale, speculative compatibility, or theoretical extensibility.

## Run the review gate

After implementation, inspect the diff for:

- Unrequested functionality
- Abstractions with one caller
- Helpers that merely rename simple operations
- Unnecessary configuration
- Speculative defensive branches
- Redundant tests or duplicate validation
- New dependencies without strong justification
- Unnecessary CI jobs
- Stale artifacts
- Adjacent refactors

Simplify or remove them before considering the task complete.

## Stop when complete

Stop once the requested behavior is implemented, validated, and documented to the degree the task requires.

Do not continue into adjacent refactoring, generalized infrastructure, unrelated test coverage, optional configuration, hypothetical future support, expanded CI, extra abstractions, unnecessary documentation, or unrelated cleanup.

## Use the complexity budget

- Add no unrequested features.
- Add no abstraction for a single demonstrated use case.
- Add no defensive handling for structurally impossible or implausible scenarios.
- Add no redundant tests or duplicate CI checks.
- Add no speculative extensibility.
- Prefer existing infrastructure.
- Prefer explicit local code to premature generalization.
- Prefer deleting obsolete complexity to preserving it just in case.
- Stop when the requested behavior is complete and validated.

If a more complex design is required, state the concrete current requirement that justifies it. Do not rely on phrases such as “for future use,” “in case we need it later,” “to make this more extensible,” “for completeness,” or “to be safe” without a demonstrated current need.
