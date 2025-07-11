from flask import Flask, jsonify, request, render_template, redirect, url_for
from uuid import uuid4
from blockchain import Blockchain

app = Flask(__name__)
node_id = str(uuid4()).replace('-', '')
blockchain = Blockchain()

@app.route('/')
def dashboard():
    return render_template("dashboard.html", chain=blockchain.chain, node_id=node_id)

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    sender = request.form.get('sender')
    recipient = request.form.get('recipient')
    amount = request.form.get('amount')

    index = blockchain.new_transaction(sender, recipient, int(amount))
    return redirect(url_for('dashboard'))

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(
        sender="0",
        recipient=node_id,
        amount=1,
    )

    block = blockchain.new_block(proof)
    return redirect(url_for('dashboard'))

@app.route('/refresh', methods=['GET'])
def refresh():
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int)
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port, debug=True)


