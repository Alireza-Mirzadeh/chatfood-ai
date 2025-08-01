from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# Create a vector store for RAG
def create_vector_store(docs_path: str, embedding_model: str, chunk_size: int, chunk_overlap: int):

    '''
    Creates a vector store from the documents in the specified path.
    
    :param docs_path: Path to the documents.
    :param embedding_model: Model to use for embeddings.
    :param chunk_size: Size of each document chunk.
    :param chunk_overlap: Overlap size between chunks.
    
    :return: Vector store.

    '''


    # Load documents from the specified path
    loader = DirectoryLoader(docs_path, glob="**/*.pdf", loader_cls=PyPDFLoader)
    data = loader.load()

    # Split the documents into smaller chunks
    rc_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", ""],
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    docs = rc_splitter.split_documents(data)

    # Embdedding model
    embedding_model = HuggingFaceEmbeddings(model_name=embedding_model)

    # creare and return the vector store
    vectorstore = Chroma.from_documents(
        documents = docs,
        embedding = embedding_model,
        persist_directory="./rag_db"
    )

    print("✅ Vectorstore built and saved.")


# Test the vector store creation
if __name__ == "__main__":
    create_vector_store(
        docs_path="./docs",
        embedding_model="BAAI/bge-m3",
        chunk_size=2000,
        chunk_overlap=300
    )