# Lucide Flask

A lucide icon extension for Flask

### Installation

```
pip install -U lucide-flask
```

## Basic Usage

```python
from flask import Flask, render_template
from lucide_flask import Lucide # Import the Lucide class

app = Flask(__name__)
icons = Lucide() # Create a Lucide instance

@app.route("/", methods=["GET"])
def index():
    # Pass icons to templates for easy access
    return render_template("index.html", icons=icons)

app.run(debug=True)
```

### Simple access
```html
<!-- Render the "smile" icon inline -->
<h1>{{ icons["smile"] }} Hello, World!</h1>
```

### Existence check
```jinja
<button>
<!-- You can safely check whether an icon exists before rendering it: -->
{{% if "heart" in icons  %}}
    {{ icons["heart"] }}
{{% else %}}
    <span>❤️</span>
</button>
```