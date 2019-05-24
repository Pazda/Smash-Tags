# Smash-Tags
Generates Smash tags 

## Requirements
- [textgenrnn by minmaxir](https://github.com/minimaxir/textgenrnn)
- [PySmash by PeterCat12](https://github.com/PeterCat12/pysmash)

## Usage
1. Run fetch.py, editing the crawlTourns list for which tournaments you'd like the RNN to learn from
2. In nn.py, set areTraining to True. Modify the model below if desired, as well as the output temperature
3. Train nn.py and enjoy the results!

Basic webpage included with 6,000 sample results for ease of use
