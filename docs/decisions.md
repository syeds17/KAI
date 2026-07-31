# Architecture Decisions

## Decision 001

### Topic

Project Architecture

### Decision

Use a modular architecture.

### Reason

Independent development, testing, and maintenance.

---

## Decision 002

### Topic

Database

### Decision

SQLite

### Reason

Simple, lightweight, zero configuration.

---

## Decision 003

### Topic

Memory

### Decision

Persistent storage using SQLite instead of in-memory lists.

---

## Decision 004

### Topic

Natural Language

### Decision

Add a Normalizer before the Parser.

### Reason

Allows users to speak naturally without modifying the parser.

---

## Decision 005

### Topic

LLM Architecture

### Decision

Use a provider-independent LLM layer.

Current provider:

Gemini

Future providers:

* OpenAI
* Claude
* Local Models

---

## Decision 006

### Topic

Brain Routing

### Decision

Automation and Memory take priority over the LLM.

The AI should not perform actions that existing modules can perform.

---

## Decision 007

### Topic

Documentation

### Decision

Documentation is mandatory before every commit.

Documentation acts as the project's long-term memory and enables seamless continuation in future development sessions.
