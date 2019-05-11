# curiosity
Python GUIs for Humans

Python + WebSockets + CEF + Observables

This project aims to use a lightweight websocket server for IPC from a Python to RxJS Observables in a simple Chromium window.

## Status
"On Hold" -- Adding a websockets layer felt too redundant, which overpowered how bad it felt to work with CEF's (1) api. So, there isn't much point for this project anymore, unless there's enough to abstract for a pre-configured CEF js injection + RxJs + Svelte.

(1) There's like some mythical "upstream version" of CEF that's like in-progress or something that's supposed to "fix everything" (my interpretation, anyway). Right now it looks like a 1:1 port of a C-variant library, which is like 2% Pythonic with all this Inversion of Control patterns and whatnot. I didn't want to work with that, but it shouldn't be too bad with `js_bindings.SetObject("app", self)` and cutting out as much OO junk as possible.

## Why 'curiosity'?

Dope name. Electron -> electron tunneling (python to js!) -> Marie Curie -> Curiosity

Felt cute might reuse later
