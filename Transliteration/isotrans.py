from charmap import charmap
import string

lang_bases = {
    'en_US': 0, 'en_IN': 0, 'hi_IN': 0x0901, 'bn_IN': 0x0981,
    'pa_IN': 0x0A01, 'gu_IN': 0x0A81, 'or_IN': 0x0B01, 'ta_IN': 0x0B81,
    'te_IN': 0x0C01, 'kn_IN': 0x0C81, 'ml_IN': 0x0D01
}

class isotrans:

    def detect_lang(self, text):
        """
        Detect the language of the given text using the unicode range.
        This function can take a chunk of text and return a dictionary
        containing word-language key-value pairs.
        """
        words = text.split(" ")
        word_count = len(words)
        word_iter = 0
        word = ""
        result_dict = dict()
        while word_iter < word_count:
            word = words[word_iter]
            if(word):
                orig_word = word
                # remove the punctuations
                for punct in string.punctuation:
                    word = word.replace(punct, " ")
                length = len(word)
                index = 0
                # scan left to write, skip any punctuations,
                # the detection stops in the first match itself.
                while index < length:
                    letter = word[index]
                    #if not letter.isalpha():
                     #   index = index + 1
                      #  continue
                    if ((ord(letter) >= 0x0D00) & (ord(letter) <= 0x0D7F)):
                        result_dict[orig_word] = "ml_IN"
                        break
                    if ((ord(letter) >= 0x0980) & (ord(letter) <= 0x09FF)):
                        result_dict[orig_word] = "bn_IN"
                        break
                    if ((ord(letter) >= 0x0900) & (ord(letter) <= 0x097F)):
                        result_dict[orig_word] = "hi_IN"
                        #print "here"
                        break
                    if ((ord(letter) >= 0x0A80) & (ord(letter) <= 0x0AFF)):
                        result_dict[orig_word] = "gu_IN"
                        break
                    if ((ord(letter) >= 0x0A00) & (ord(letter) <= 0x0A7F)):
                        result_dict[orig_word] = "pa_IN"
                        break
                    if ((ord(letter) >= 0x0C80) & (ord(letter) <= 0x0CFF)):
                        result_dict[orig_word] = "kn_IN"
                        break
                    if ((ord(letter) >= 0x0B00) & (ord(letter) <= 0x0B7F)):
                        result_dict[orig_word] = "or_IN"
                        break
                    if ((ord(letter) >= 0x0B80) & (ord(letter) <= 0x0BFF)):
                        result_dict[orig_word] = "ta_IN"
                        break
                    if ((ord(letter) >= 0x0C00) & (ord(letter) <= 0x0C7F)):
                        result_dict[orig_word] = "te_IN"
                        break
                    if ((letter <= u'z')):  # this is fallback case.
                        #result_dict[orig_word] = "en_US"
                        break
                    index = index + 1
            word_iter = word_iter + 1
        return result_dict

    def transliterate_iso15919( self, word, src_language):
        tx_str = ""
        index = 0
        word_length = len(word)
        for chr in word:
            index += 1
            offset = ord(chr) - lang_bases[src_language]
            #76 is the virama offset for all indian languages from its base
            if offset >= 61 and offset <= 76:
                tx_str = tx_str[:-1]  # remove the last 'a'
            if offset > 0 and offset <= 128:
                tx_str = tx_str + charmap["ISO15919"][offset]
            #delete the inherent 'a' at the end of the word from hindi
            if tx_str[-1:] == 'a' and (src_language == "hi_IN"
                                       or src_language == "gu_IN"
                                       or src_language == "bn_IN"):
                if word_length == index and word_length > 1:  # if last letter
                    tx_str = tx_str[:-1]  # remove the last 'a'
        return tx_str#.decode("utf-8")

    def tokenize(self, text):
        words = text.split(" ")
        #print(words)
        nSent=""
        for x in words:
            #print x
            #chars=split(x)
            nWord=""
            first=True
            bet=False
            for c in x:
                #print c
                #print detect_lang(c)
                #print c.isalpha()
                #print(hex(ord(c)))
                if(len(detect_lang(c))==0 and first):
                    nWord=nWord+c+" "
                    #print "1"
                else:
                    if(len(detect_lang(c))==0):
                        nWord=nWord+" "+c
                        #print "2"
                        bet=True
                    else:
                        if (bet):
                            nWord=nWord+" "+c
                            #print "3"
                            bet=False
                        else:
                            nWord=nWord+c
                            #print "4"
                first=False
            nSent=nSent+" "+nWord
        return nSent

    def transliterate(self,nsent):

        words=nsent.split(" ")
        textISO=""

        for x in words:

            if(len(self.detect_lang(x))==0):
                textISO=textISO+x+" "
            else:
                textISO=textISO+self.transliterate_iso15919(x,list(self.detect_lang(x).values())[0])+" "

        return textISO
