import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, filePath="E:/Cold email generator/app/resource/my_portfolio.csv"):
        self. filePath = filePath
        self.data = pd.read_csv(self.filePath)
        self.chromaClient = chromadb.PersistentClient("vectorstore")
        self.collection = self.chromaClient.get_or_create_collection(name="portfolio")

    def loadPortfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["Techstack"],
                                    metadatas = {'links': row['Links']},
                                    ids = str(uuid.uuid4()))
    
    def queryLinks(self, skills):
        if not skills:
            return []  # Return empty list if no skills provided
        
        # Convert skills to a list if it's not already
        if isinstance(skills, str):
            skills = [skills]
        
        # Ensure we have valid skills to query
        valid_skills = [str(skill).strip() for skill in skills if skill]
        
        if not valid_skills:
            return []
            
        try:
            results = self.collection.query(
                query_texts=valid_skills,
                n_results=2
            )
            # Extract links from metadata
            metadatas = results.get('metadatas', [])
            # Flatten the list of links
            links = [item['links'] for sublist in metadatas for item in sublist if 'links' in item]
            return links
        except Exception as e:
            print(f"Error querying collection: {e}")
            return []
        