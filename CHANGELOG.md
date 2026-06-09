# Changelog

All notable changes to this project will be documented in this file.

## [2026.6.9] - 2026-06-09

### Renamed
- **Project rename**: `pulse` was previously `pulse-tui` / `rMonitor`. The Cargo package name, binary name, file paths, registry keys, and docs are now lowercase `pulse`. Behavior and features are unchanged.

### Changed
- README rewritten in the new register: live monitor feature list, install matrix, CLI flags, configuration, build instructions, license.
- Drop the legacy "r*" and "Local freedom" branding throughout.
- Drop the per-repo `rApps` umbrella and `build_all.ps1` from this repo; build orchestration lives in [`toolkit`](https://github.com/local76/toolkit).

## [3.1.0] - 2026-06-08

### Changed
- Renamed project back from `pulse-tui` to `pulse` (crate name: `pulse`, binary name: `pulse`).
- Split monolithic `src/panels.rs` (647 lines) into modular files in `src/panels/` subdirectory, ensuring all source files are strictly under 500 lines.
- Suppressed unused/deprecated compiler warnings to achieve a clean compilation.

## [3.0.1] - 2026-06-06
### Added
- Added author and maintainer metadata for packaging.

## [3.0.0] - 2026-06-06
### Changed
- Renamed organization to `local76`.
- Renamed executable from `rtem` to `pulse`.
- Reorganized directory structure to group packaging files inside `dist/packages/`.