# Natural Language Processing: Radicioni

University exercises for the *Tecnologie del Linguaggio Naturale* course, taught by **Prof. Radicioni** at the University of Turin.

Each exercise is a self-contained Jupyter Notebook covering a core NLP topic.

## Exercises

| # | Topic | Key techniques |
|---|-------|---------------|
| **1** | Word Similarity & WSD | Wu-Palmer similarity, Lesk algorithm, WordNet, WordSim353 evaluation |
| **2** | FrameNet Annotation | Frame extraction, synset-frame mapping, manual annotation by surname |
| **3** | Text Summarization | NASARI vectors, weighted overlap, title method, cue phrases |
| **4** | WSD Annotation Task | Cosine similarity on NASARI, Cohen's kappa, inter-annotator agreement |

## Tech Stack

- **Python 3** + **Jupyter Notebook**
- **NLTK** (WordNet, FrameNet, tokenization, lemmatization)
- **NumPy** / **SciPy** for vector operations
- **scikit-learn** (`cohen_kappa_score`)
- **NASARI** semantic vectors (BabelNet-based)

## Setup

```bash
pip install nltk numpy scipy scikit-learn jupyter
python -c "import nltk; nltk.download('wordnet'); nltk.download('framenet_v15')"
jupyter notebook
```

## Related repos

- [NLP: Di Caro](https://github.com/teoparis/Tecnologie-del-linguaggio-naturale---Di-Caro)
- [NLP: Mazzei](https://github.com/teoparis/Tecnologie-del-linguaggio-naturale---Mazzei)

---

*University project, Tecnologie del Linguaggio Naturale, University of Turin, 2022*
