from utils import buildSentences, TT_Entails

if __name__ == "__main__":
    kb_file = r"./KB.txt"
    alpha_file = r"./alpha.txt"
    KB = buildSentences(kb_file)
    alpha = buildSentences(alpha_file)
    print(TT_Entails(KB, alpha))