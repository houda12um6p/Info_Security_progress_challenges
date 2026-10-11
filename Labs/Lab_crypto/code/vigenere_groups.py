ciphertext = """VVHWGQUIVYHIRSUPGTWXJSVIPCWIUPHGCIVIVVHPGHWITSDTRSDVUSYITMZL
GFHIXSUCVSDQOSPFGFVLQIOHEVHGMSDGJQRPWAQWGSNXJSPSUHIVGEXIPHVC
OPRPCBGYUSLXVCUIECYITHKIMSBAJSQXJSPIUGDKGPHGQAHWEZHETSQXGFWL
GOFGGGVAQFGIEZLTUS"""
ciphertext = ciphertext.replace("\n", "")
group1 = ciphertext[0::4]
group2 = ciphertext[1::4]
group3 = ciphertext[2::4]
group4 = ciphertext[3::4]
print("Group 1: ", group1)
print("Group 2: ", group2)
print("Group 3 :", group3)
print("Group 4:",  group4)
