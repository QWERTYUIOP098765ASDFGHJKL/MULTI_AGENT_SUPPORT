Multi-Agent Support System
Problem Description
A customer support system where AI agents classify queries and retrieve solutions from a knowledge base.

System Architecture
Customer Agent: Accepts user queries.

Classification Agent: Categorizes queries.

Resolution Agent: Retrieves solutions from the database.

Installation
Clone the repo:

git clone https://github.com/your-username/multi_agent_support.git
cd multi_agent_support
Install dependencies:


pip install flask psycopg2 requests
Set up the database:

psql -U postgres -f database.sql
API Endpoints & Usage
Submit Query

POST /submit_query  
Body: {"query": "How to check my bill?"}
Classify Query

POST /classify  
Body: {"query": "How to check my bill?"}
Get Solution


POST /resolve  
Body: {"category": "Billing"}


 Sample Response

{
  "category": "Billing",
  "solution": "Log in to your account and navigate to the Billing section."
}
