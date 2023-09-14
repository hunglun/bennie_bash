# Description
My personal shell with my nickname

# Development/Maintenance

## Local Testing
```bash
python3 -m build
pip3 install dist/bennie_bash-0.1.0-py3-none-any.whl 
pip3 uninstall dist/bennie_bash-0.1.0-py3-none-any.whl 
```

## Publish

Make sure $HOME/.pypirc contains valid token

```bash
python3 -m twine upload dist/bennie_bash-0.1.0-py3-none-any.whl  
```