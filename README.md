# 🔗 Peer-to-Peer Blockchain Simulation

A simulation of a simple peer-to-peer (P2P) blockchain network using Python and Flask.  
Each node runs independently, manages its own blockchain, and syncs with peers through a consensus mechanism.

---

## 📌 Project Objective

- Understand how a basic blockchain works
- Simulate decentralized communication between multiple nodes
- Implement mining and consensus in a simplified way

---

## 🧠 Key Features

- ⛓️ Blockchain data structure with proof-of-work (PoW)
- 💸 Transaction creation and storage
- ⛏️ Mining new blocks with pending transactions
- 🌐 Multiple Flask nodes (simulated peers)
- 🔁 Node registration and discovery
- 📏 Longest chain consensus algorithm
- 🧾 Web dashboard for user interaction

---

## 🧰 Technology Stack

| Component       | Description                |
|-----------------|----------------------------|
| Python 3.x      | Programming language        |
| Flask           | Web framework for APIs      |
| `requests`      | HTTP communication between nodes |
| Bootstrap       | Styling for the dashboard UI |
| HTML/CSS        | Frontend templating         |

---

Open a terminal inside the `blockchain/` folder and run:

```bash
pip install flask requests2️⃣ Start Multiple Nodes
Open 3 separate terminals and run:

bash

python node.py -p 5000
python node.py -p 5001
python node.py -p 5002
Each command runs a different blockchain node.

3️⃣ Register Nodes (Discovery)
From Postman or terminal (PowerShell users may need Postman), register peers like this:

curl -X POST http://localhost:5000/nodes/register \
-H "Content-Type: application/json" \
-d "{\"nodes\": [\"http://localhost:5001\", \"http://localhost:5002\"]}"

🌐 Using the Dashboard UI
Visit http://localhost:5000/ in your browser. You will see:

✅ Features:
🧾 Add Transaction Form

⛏️ Mine Block Button

🔁 Refresh Chain Button

📦 View All Blocks with Transactions

🧪 Try This:
Enter:

Sender: Alice

Recipient: Bob

Amount: 50

Click 💸 Submit Transaction

Click ⛏️ Mine Block

Click 🔁 Refresh Chain

Check if the transaction is added inside the new block

Repeat this on other ports like 5001, 5002 to simulate more nodes.

