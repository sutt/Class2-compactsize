import hashlib
#import libwally
#import base58


#Flip byte endianness of hex string
def flip_endian(hex_string):
    return bytes.fromhex(hex_string)[::-1].hex()
    
#sha256 on byte encoding of hex string
def sha256(hex_string):
    return hashlib.sha256(bytes.fromhex(hex_string)).hexdigest()

#sha256(sha256(hex_string))
def hash256(hex_string):
    return sha256(sha256(hex_string))

#ripemd160(sha256(hex_string)), used for script/pubkey hashes
def hash160(hex_string):
    ripemd = hashlib.new("ripemd160")
    ripemd.update(hashlib.sha256(hex_string.encode()).digest())
    return ripemd.hexdigest()

    