from .vector_db_builder import build_vector_db

INPUT_FILE = "../datasets/barrage.json"
VECTOR_DB_PATH = "../vector_db/barrage_vector_db"
MODEL_NAME = "text-embedding-v4"

if __name__ == "__main__":
    build_vector_db(input_file=INPUT_FILE, vector_db_path=VECTOR_DB_PATH, model_name=MODEL_NAME)