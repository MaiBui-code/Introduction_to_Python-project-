frm = "ban"
to = "?a?"
trans_table = str.maketrans(frm, to)
secret_code = "banana".translate(trans_table)
print (secret_code)