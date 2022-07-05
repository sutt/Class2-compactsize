# Calculating Compact Field Sizes, TXIDs, and Fees

We've got 2 giant TXs and a little baby one to parse today, but don't worry! You're only fully breaking down the little one, we'll just be doing some calculated fields on the others. I've pasted the raw hex for each in the raw_tx_hex.py file, and imported them into the answers.py file as "raw_hex1", "raw_hex2", "raw_hex3"

## Steps
    1. Completely parse raw_hex1, filling out the entire tx_skeleton structure including the calculated field for fees. Reminder, you'll have to look up the inputs' txid:vout combinations to get the sats value of the inputs!
    
    2. Calculate the ScriptSig field size for TX2. Write a comment explaining how you interpreted the compact field size.
    
    3. Calculate the number of inputs for TX3. Write a comment explaining how you interpreted the compact field size.
    
    4. Calculate the txid's, in big endian, for all 3 TXs. I wrote some helper functions for you in helpers.py. You should be able to look these TXs up in a block explorer like blockstream.info (to look it up you need the TXID in big endian!!).
    

