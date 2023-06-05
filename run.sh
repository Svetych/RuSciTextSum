pip install transformers
pip install transformers sentencepiece --quiet
pip uninstall -y transformers accelerate
pip install transformers accelerate
pip install datasets
pip install rouge
pip install nltk
pip install evaluate
pip install bert_score

python3 pipeline.py