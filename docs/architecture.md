# KAI Architecture

## Overview

KAI (Knowledgeable Artificial Intelligence) is a modular personal AI assistant built with Python.

The project follows a modular architecture where every major capability is isolated into its own module. This allows each component to be developed, tested, and upgraded independently while maintaining clean communication between modules.

The long-term goal is to build an extensible AI assistant capable of conversation, automation, memory, vision, voice interaction, and intelligent task execution.

---

## High-Level Architecture

```
Chief (User)
      │
      ▼
   Normalizer
      │
      ▼
 Command Parser
      │
      ▼
  Dispatcher
 ┌────┼──────────────┐
 │    │              │
 ▼    ▼              ▼
Automation      Memory      LLM
 │               │           │
 ▼               ▼           ▼
System       SQLite DB    Gemini (Current)
```

Future modules:

* Voice
* Vision
* Internet Search
* File Manager
* AI Agent

---

## Current Modules

### Brain

Responsible for:

* Understanding user input
* Normalizing natural language
* Parsing commands
* Routing requests
* Sending unknown requests to the AI layer (planned)

---

### Automation

Responsible for:

* Opening applications
* Executing system commands
* Future file and system operations

---

### Memory

Responsible for:

* Persistent memory
* Remembering information
* Recalling memories
* Duplicate detection

SQLite is used as the storage backend.

---

### API

Responsible for communication with external services.

Current planned structure:

* LLM (Gemini)
* Weather
* Search
* News
* Future external integrations

---

## Design Principles

* Modular architecture
* Separation of concerns
* Provider-independent AI layer
* Easily extensible
* Offline-first where possible
* Minimal coupling between modules

---

## Current Status

Architecture Version: v0.1

Status: Foundation completed.
