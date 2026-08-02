# Changelog

Releases prior to 0.3.0 are documented at https://github.com/nornir-automation/nornir_utils/releases

## v0.3.0

> **Breaking:** the minimum supported Python version is now 3.10 (was 3.6).

### Python support
* Drop Python 3.6/3.7, require Python >= 3.10, and test on 3.10 – 3.14 by @ubaumann in https://github.com/nornir-automation/nornir_utils/pull/35, by @ogenstad in https://github.com/nornir-automation/nornir_utils/pull/42 and https://github.com/nornir-automation/nornir_utils/pull/67

### Fixes
* fix(#39): correct result typing by @ohai89 in https://github.com/nornir-automation/nornir_utils/pull/40
* Repair broken link by @ogenstad in https://github.com/nornir-automation/nornir_utils/pull/43

### Tooling & CI
* Migrate project from poetry to uv by @ogenstad in https://github.com/nornir-automation/nornir_utils/pull/68
* Update GitHub Actions, replace pylama & black with ruff by @ogenstad in https://github.com/nornir-automation/nornir_utils/pull/61
* Move remaining content from setup.cfg to pyproject.toml by @ogenstad in https://github.com/nornir-automation/nornir_utils/pull/65
* Update code analysis config file by @ogenstad in https://github.com/nornir-automation/nornir_utils/pull/66
* Upgrade GitHub Actions with deprecation warnings by @ogenstad in https://github.com/nornir-automation/nornir_utils/pull/55
* Fix broken CI by @ogenstad in https://github.com/nornir-automation/nornir_utils/pull/41

### New Contributors
* @ogenstad made their first contribution in https://github.com/nornir-automation/nornir_utils/pull/41
* @ohai89 made their first contribution in https://github.com/nornir-automation/nornir_utils/pull/40

**Full Changelog**: https://github.com/nornir-automation/nornir_utils/compare/v0.2.0...v0.3.0
