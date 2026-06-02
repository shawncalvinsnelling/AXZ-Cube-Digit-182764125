.PHONY: verify test

verify:
	PYTHONPATH=src python scripts/verify_runtime_safety.py
	PYTHONPATH=src python scripts/verify_challenge_7.py
	PYTHONPATH=src python scripts/verify_data_hashes.py
	PYTHONPATH=src python scripts/generate_certificate.py

test:
	PYTHONPATH=src python -m pytest -q
