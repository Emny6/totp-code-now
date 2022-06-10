import pyotp
import os
os.system('cls')
codemoonsz = input("\n  > What is the Top Code? (Example: TFE6OUD74PTWWGVJ): ")
totp = pyotp.TOTP(codemoonsz)
print ("\n  > Current code: " + totp.now())
