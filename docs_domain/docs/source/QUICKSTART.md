# Quick start
This page is written in Markdown via MySt parser

## Install 

```bash
pip install sales
# or
pip install -e .
```

## Example
```python
def write_report(path, txt):
    # TODO better errors
    with open(path, "w", encoding="utf-8") as f:  # open file for writing
        f.write(txt)  # write text
```