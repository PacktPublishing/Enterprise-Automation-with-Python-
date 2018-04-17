import whois
w = whois.query('pythonforbeginners.com')
print(w.name)
print(w.creation_date)
print(w.name_servers)
print(w.last_updated)
