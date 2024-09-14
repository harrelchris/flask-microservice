if (-not (Test-Path .venv)) {
    python -m venv .venv
}

.venv\Scripts\activate

python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements-dev.txt

if (-not (Test-Path .env)) {
    Copy-Item example.env .env
}
