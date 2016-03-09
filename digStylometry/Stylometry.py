from digSparkUtil.listUtil import flatten
import re
import json


class ComputeSignature:
    def __init__(self,**options):
        #options = json.load(open(configFileName))
        self.pretty = options.get("pretty","true")
        self.runLimit = options.get("runLimit",5)
        self.field_name = options.get("field")

    def perform(self,rdd):
        rdd = rdd.mapValues(lambda x: self.addsignature(x))
        #rdd.foreach(lambda x : self.f(x))
        return rdd

    def f(self,x):
        print x


    def addsignature(self,data):
        field_name = self.field_name
        newData = {}
        try:
            values = list(data)
            cleaned_values = [self.preprocessSent(sent) for sent in values]
            signature = self.getCompleteSignature(cleaned_values)
            newData[field_name]=signature
        except:
            # if column_path does not apply
            # or any other exception(?)
            # => empty list
            values = []
        return newData


    def getCompleteSignature (self,field_value):
        """Takes a list of sentences and returns the concatenated signature for them."""
        signatures = [self.getSentenceSignature(sent) for sent in field_value]
        complete = "".join(signatures)
        if (self.runLimit):
            complete = self.limitRunsInSignature(complete)
        return complete

    def limitRunsInSignature (self,signature):
        currentRun = 0
        currentChar = None
        result = ""
        for i in range(0,len(signature)):
            char = signature[i]
            if (char == currentChar):
                if (currentRun < self.runLimit):
                    currentRun += 1
                    result += char
            else:
                currentRun = 1
                currentChar = char
                result += char
        return result

    def getSentenceSignature (self,sent):
        """Takes a sentence and returns the signature for it."""
        sent = self.preprocessSent(sent)
        tokens = []
        for tok in sent.split():
            tokens.extend(self.splitToken(tok))
        sigs = [self.getTokenSignature(token) for token in tokens]
        return "".join(sigs)

    def makeList (self,value):
        """Takes a value and turns it into a list if it is not one already."""
        if (value == None):
            return []
        elif (type(value) != list):
            return [value]
        else:
            return value



    def getTokenSignature (self,tok):
        """Takes a token; returns its corresponding signature."""
        # Single upper-case letter: L
        m = re.match(r'[A-Z]$',tok)
        if (m):
            return "L"
        # Multi-letter word all-caps: W
        if (re.match(r'[A-Z][A-Z]+$',tok)):
            return "W"
        # Capitalized word: first letter upper, subsequent letters all lower-case: C
        if (re.match(r'[A-Z][a-z]+$',tok)):
            return "C"
        # All-lower case word: w
        if (re.match(r'[a-z]+$',tok)):
            return "w"
        # Mixed case word: M
        if (re.match(r'[a-zA-Z]+$',tok)):
            return "M"
        # Digit string is a matching string of D's.
        if (re.match(r'\d+$',tok)):
            result = ""
            for i in range(0,len(tok)):
                result += "D"
            return result
        # Otherwise, the signature is just the token itself.
        return tok


    def splitToken (self,tok):
        """Takes a token without whitespace and splits it into a list of sub-tokens based on character classes."""
        result = []
        while (tok):
            # Letter sequence
            m = re.match(r'^([a-zA-Z]+)(.*)',tok)
            if (m):
                result.append(m.group(1))
                tok = m.group(2)
                continue
            # A sequence of neither digits nor letters
            m = re.match(r'^([^\da-zA-Z]+)(.*)',tok)
            if (m):
                result.append(m.group(1))
                tok = m.group(2)
                continue
            # A sequence of digits
            m = re.match(r'(\d+)(.*)',tok)
            if (m):
                result.append(m.group(1))
                tok = m.group(2)
                continue
        #
            raise RuntimeError("Shouldn't come here")
        return result


    def preprocessSent(self,sent):

        """Cleans up the text, removing HTML tags and entities, and other stuff"""

        # Strip enclosing quotes if they are present
        sent = sent.strip('"')

        # link tags with attributes
        sent = re.sub(r'<a .*>', " ",sent)
        sent = re.sub(r'<iframe .*>', " ",sent)

        # User-exposed URLs
        sent = re.sub(r'https?:\S*'," ",sent)

        # HTML open tag: <br>
        sent = re.sub(r'<\s*[a-zA-Z]+\s*>'," ",sent)
        sent = re.sub(r'<\s*\/\s*[a-zA-Z]+\s*>'," ",sent)
        sent = re.sub(r'<\s*[a-zA-Z]+\s*\/\s*>'," ",sent)

        # HTML entities
        sent = sent.replace("&nbsp;", " ")
        sent = re.sub(r'&lt;br&gt;'," ",sent)
        sent = re.sub(r'&lt;', " ",sent)
        sent = re.sub(r'&gt;', " ",sent)
        sent = re.sub(r'&\S+;', " ",sent)
        # Broken entity
        sent = re.sub(r'&#\d+', " ",sent)
        # Escaped newlines,tabs
        sent = re.sub(r'\n'," ",sent)
        sent = re.sub(r'\t'," ",sent)
        sent = re.sub(r'\r'," ",sent)
        return sent
