import pandas as pd

def get_project_details():
    portfolio_data = []
    
    while True:
        print("\n=== Add New Project ===")
        project_name = input("Enter project name (or 'done' to finish): ")
        
        if project_name.lower() == 'done':
            break
            
        techstack = input("Enter tech stack (comma-separated): ")
        project_link = input("Enter project link: ")
        
        portfolio_data.append({
            "Project": project_name,
            "Techstack": techstack,
            "Links": project_link
        })
        
        print("\nProject added successfully!")
        
    return portfolio_data

def main():
    print("Welcome to Portfolio Generator!")
    print("Enter your project details below. Type 'done' when finished.")
    
    # Get project details from user
    portfolio_data = get_project_details()
    
    if not portfolio_data:
        print("No projects were added.")
        return
    
    # Create DataFrame
    df = pd.DataFrame(portfolio_data)
    
    # Save to CSV
    filename = input("\nEnter filename for your portfolio CSV (e.g., my_portfolio.csv): ")
    if not filename.endswith('.csv'):
        filename += '.csv'
    
    df.to_csv(filename, index=False)
    print(f"\nPortfolio has been saved to {filename}")
    
    # Display the portfolio
    print("\nYour Portfolio:")
    print(df)

if __name__ == "__main__":
    main()