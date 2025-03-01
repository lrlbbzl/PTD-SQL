# Code implementation of EMNLP24 Main Conference Paper "PTD-SQL: Partitioning and Targeted Drilling with LLMs in Text-to-SQL"

This is the code repository for the PTD-SQL paper presented at the EMNLP 2024 main conference.

## Few-shot Banks Generation

The prompts used for the four predefined query categories are sourced from four files.

* `complex.py`: prompt template for complex nested query.
* `combination.py`: prompt template for combination query.
* `filter.py`: prompt template for filtering query.
* `simple.py`: prompt template for simple query.

## Quick Start

Prepare the API_KEY and embeddings files, and just execute main.py

```python
python3 main.py
```

## Citation

```
@inproceedings{luo2024ptd,
  title={PTD-SQL: Partitioning and Targeted Drilling with LLMs in Text-to-SQL},
  author={Luo, Ruilin and Wang, Liyuan and Lin, Binghuai and Lin, Zicheng and Yang, Yujiu},
  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
  pages={3767--3799},
  year={2024}
}
```

