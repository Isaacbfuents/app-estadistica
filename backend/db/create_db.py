from backend.db.database import Base, engine
# Import de todos los modelos
import backend.db.db_models



print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("tables created.")