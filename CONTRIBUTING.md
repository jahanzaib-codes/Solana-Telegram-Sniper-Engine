# Contributing to Solana-Telegram-Sniper-Engine

Thank you for your interest in contributing to **Solana-Telegram-Sniper-Engine**. This repository provides an asynchronous, high-throughput backend for Solana Telegram trading and sniping bots.

## Guidelines

1. **Security & Cryptography**:
   - Never log unencrypted private keys or seeds.
   - Use AES-256-GCM authenticated encryption for all sensitive payloads.
2. **Commit Conventions**:
   Follow [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat(...)`: New features
   - `fix(...)`: Bug fixes
   - `docs(...)`: Documentation updates
   - `infra(...)`: CI/CD or Docker configurations
3. **Pull Request Workflow**:
   - Run `python cli.py demo` locally before submitting PRs.
   - Ensure zero warnings under `flake8`.
