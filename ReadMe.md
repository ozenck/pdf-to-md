**How to run**

```
cd C:/Users/ozenc/Documents/Environments
mkdir pdf-env
cd pdf-env
python -m venv .
pip install virtualenv
source C:/Users/ozenc/Documents/Environments/pdf-env/Scripts/activate
pip install -r requirements.txt
py main.py combined 1.pdf 2.pdf
```

'combined' argument is the generated filename for pdf & md files,
You will see output/combined folder created and new pdf and md files generated in the folder.