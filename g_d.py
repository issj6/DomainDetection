from utils import GenerateDomain

# gd = GenerateDomain("cc")
# domains = gd.generate_xa(2)
# for domain in domains[:-10]:
#     if domain.split('.')[0] not in ["jjj","iii","www","lll","mmm"]:
#         print(domain)

gd = GenerateDomain("cc")
domains = gd.generate_domains("ll")
for domain in domains[:-10]:
    if domain.split('.')[0] not in ["jjj","iii","www","lll","mmm"]:
        print(domain)
