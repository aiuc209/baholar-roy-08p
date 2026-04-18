def baholarni_foizga_aylantir(baholar):
    foiz_baholar = [baho / 100 for baho in baholar]
    return foiz_baholar

baholar = [90, 85, 95, 80, 92]
foiz_baholar = baholarni_foizga_aylantir(baholar)
print(foiz_baholar)
