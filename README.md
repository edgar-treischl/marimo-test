# marimo-test

A small [marimo](https://marimo.io/) app for exploring the Palmer Penguins dataset. It code executes directly in the browser through WebAssembly (WASM).

## Try it online

Explore the app on **GitHub Pages** without installing Python or running a local server.

## About marimo

[marimo](https://marimo.io/) is an open-source reactive Python notebook. Cells automatically update when their dependencies change, keeping code, outputs, and visualizations in sync.

Marimo notebooks are stored as Python files, making them easy to version, review, and maintain with Git.

## Browser-based execution

Marimo can export notebooks as standalone HTML applications that run Python in the browser using WebAssembly. This allows users to interact with the app without a Python backend.

Export the app with:

```bash
uv run marimo export html-wasm app.py -o dist --mode run
```

To export an editable notebook instead, use:

```bash
uv run marimo export html-wasm app.py -o dist --mode edit
```

The generated dist/ directory contains the static files that can be hosted on GitHub Pages or another static web host. See the GH workflow for an CI/CD pipe.

Purpose

This project is a test app for exploring marimo's reactive notebooks, HTML/WASM export, browser-based Python execution, and static hosting.