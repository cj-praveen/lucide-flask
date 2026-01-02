# Lucide Flask
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/lucide-flask?period=total&units=INTERNATIONAL_SYSTEM&left_color=GRAY&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/lucide-flask)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE)

A lucide icon extension for Flask applications.

### Installation

```bash
pip install -U lucide-flask
```

## Basic Usage

- Import and create an instance
```python
from lucide_flask import Lucide # Import the Lucide class

icons = Lucide() # Create a Lucide instance
```

- Render the icon inline
```jinja
<h1>{{ icons["smile"] }} Hello, World!</h1>
```

- You can safely check whether an icon exists to avoid rendering errors
```jinja
<button>
{{% if "heart" in icons  %}}
    {{ icons["heart"] }}
{{% else %}}
    <span>❤️</span>
<span>Like</span>
</button>
```

## Workflow
<img width="426" height="470" alt="Screenshot 2026-01-02 at 12 28 39 PM" src="https://github.com/user-attachments/assets/351b36a8-57db-4c35-a590-309de59ca9c0" />

