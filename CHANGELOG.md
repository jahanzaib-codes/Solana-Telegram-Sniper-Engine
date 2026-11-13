# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-11-13

### Added
- **Non-Custodial HD Wallet Vault**:
  - BIP-39/BIP-44 deterministic keypair derivation for Telegram user accounts.
  - AES-256-GCM symmetric encryption with unique salt and initialization vectors.
- **Routing & Jito MEV Tip Engine**:
  - Dynamic percentile tip ladder (50th, 75th, 95th, 99th percentiles) for validator congestion.
  - Dual DEX routing: direct Pump.fun bonding curves vs Jupiter V6 multi-hop.
- **Asynchronous Execution & Order Dispatch**:
  - Sub-10ms order dispatch pipeline with simulated atomic bundle wrapping.
  - Multi-stage Docker containerization and automated dual-matrix CI/CD via GitHub Actions.
