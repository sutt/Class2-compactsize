from raw_tx_hex import raw_hex1, raw_hex2, raw_hex3
import helpers

#Step 1, parse out raw_hex1 into the following dict
# raw_hex1 = '02000000021a6d5a57b061e719f20817a075a6909b4b77ee1829ca72c7cf0ecaee61fd9f68020000008a4730440220318629d8d11c324f9a4369f1e5e63d30bbfc3f5d0b3a5f6ffc236472a2e7554102201911518d139a7c4f5a56104c72869b651bb1c61d438ba09a0e4136941f5a08190141047146f0e0fcb3139947cf0beb870fe251930ca10d4545793d31033e801b5219abf56c11a3cf3406ca590e4c14b0dab749d20862b3adc4709153c280c2a78be10cffffffffb7bc6adc6bb335f986d2623c75145208a97ea857c9efc8f80765932977d4cdb7030000008a47304402202ede02a79522a6d64d5088140d7f1abc412c26d9ea093c2fbb321b8f583f279e02207bb12a722558103009abda6f995e857cf04c98c6e8bd01ff7010267bd8a4bd1d0141047146f0e0fcb3139947cf0beb870fe251930ca10d4545793d31033e801b5219abf56c11a3cf3406ca590e4c14b0dab749d20862b3adc4709153c280c2a78be10cffffffff03f07e0e000000000017a91401a2723c1e23a2bfd241c5ded1973e0d1c9ce2488710c9b66f000000001976a9149a803a4f5e37b420a904b1dfcf96c70a7300082d88acb309be99000000001976a91443849383122ebb8a28268a89700c9f723663b5b888ac00000000'

parsed_tx1 = {
    "version": 0,
    "input_count": 1,
    "inputs": [
        {
            "txid": '',
            "vout": 0,
            "scriptSig": '',
            "sequence": 0,
        },
    ],
    "output_count": 1,
    "outputs": [
        {
            "amount": 0,
            "scriptPubKey": '',
        },
    ],
    "locktime": 0,
    "calculated_fields": {
        "this_txid": '',
        "fees": '',
    }
}

#Step 2
tx2_scriptsig_size = 0
scriptSig_comment = 'This input\'s scriptSig is ___ bytes long, which is greater than ___, so to represent that number as a compact field size in bitcoin we have to...'

tx3_inputs_count = 0
inputs_count_comment = 'This TX\'s input count is ___, which is greater than ___, so to represent that number as a compact field size in bitcoin we have to...'


# Step 4, calculate big endian txids, you should be able to find them on a block explorer
txid_for_tx1 = ''
txid_for_tx2 = ''
txid_for_tx3 = ''

#please don't change these, it's just passing your answers into main.py
answers = {
    "parsed_tx1": parsed_tx1,
    "tx2_scriptsig_size": tx2_scriptsig_size,
    "scriptSig_comment": scriptSig_comment,
    "tx3_inputs_count": tx3_inputs_count,
    "inputs_count_comment": inputs_count_comment,
    "txid_for_tx1": txid_for_tx1,
    "txid_for_tx2": txid_for_tx2,
    "txid_for_tx3": txid_for_tx3,
}