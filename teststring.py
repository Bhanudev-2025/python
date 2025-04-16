str1 = "python is good"
out = str1.upper()
print(out)


str2 = """Perform a string formatting operation. 
The string on which this method is called can contain literal text
 or replacement fields delimited by braces {}. 
 Each replacement field contains either the numeric index of a positional argument,
   or the name of a keyword argument. Returns a copy of the string 
   where each replacement field is replaced with
     the string value of the corresponding argument"""
count = str2.count("or")
print(count)
fin = str2.find("braces")
print(fin)
fin1 = str2.find("fields")
print(fin1)
rep = str2.replace("this","that")
print(rep)
par = str2.partition("fields")
print(par)

spil = str2.split(" ")
print(spil)

a = "         bhanu            "
b = "prakash"
#big = a+ "." +b
#big = f"{a}.{b}"
big = "$$$".join([a, b])
print(big)
strip = a.strip()
print(strip)
