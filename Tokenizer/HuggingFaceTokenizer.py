from tokenizers import ByteLevelBPETokenizer, SentencePieceBPETokenizer, BertWordPieceTokenizer

sentence = "We need small heroes so that big heroes can shine"

# Bert vocabularies
bertBaseCased = "bert-base-cased-vocab.txt"
bertBaseUncased = "bert-base-uncased-vocab.txt"
bertLargeCased = "bert-large-cased-vocab.txt"
bertLargeUncased = "bert-large-uncased-vocab.txt"
# GPT-2 vocabularies
gpt2Vocab = "gpt2-vocab.json"
gpt2LargeVocab = "gpt2-large-vocab.json"
# Instantiate a Bert tokenizers
WordPiece = BertWordPieceTokenizer(bertLargeUncased)
WordPieceEncoder = WordPiece.encode(sentence)
# Print the ids, tokens and offsets
print(WordPieceEncoder.ids)
print(WordPieceEncoder.tokens)
print(WordPieceEncoder.offsets)
