from rank_bm25 import BM25Okapi


class Retriever:

    def __init__(self, chunks):

        self.chunks = chunks

        tokenized = [
            chunk.split()
            for chunk in chunks
        ]

        self.bm25 = BM25Okapi(tokenized)

    def search(
        self,
        query: str,
        n: int = 5
    ):

        tokens = query.split()

        return self.bm25.get_top_n(
            tokens,
            self.chunks,
            n=n
        )
