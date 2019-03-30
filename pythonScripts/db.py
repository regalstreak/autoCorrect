from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair


def add_block(data):
    bdb_root_url = 'https://test.bigchaindb.com'
    bdb = BigchainDB(bdb_root_url)
    alice = generate_keypair()

    # data = {'data': 
    #     {'123abc': 
    #         {
    #             'question': '1',
    #             'text': 'bkfabdcfreferfejfbewjuhcbwdichbewidyewbdiew ieydvewudhew eduew utvewboiugy ewduie',
    #             'marks': 0.35,
    #         },
    #     },
    # }

    prepared_creation_tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=alice.public_key,
        asset=data,
        )

    fulfilled_creation_tx = bdb.transactions.fulfill(prepared_creation_tx, private_keys=alice.private_key)
    
    sent_creation_tx = bdb.transactions.send_commit(fulfilled_creation_tx)
    
    block_height = bdb.blocks.get(txid=sent_creation_tx['id'])
    block = bdb.blocks.retrieve(str(block_height))
    # print()
    print(block['transactions'][0].get('asset').get('data'))