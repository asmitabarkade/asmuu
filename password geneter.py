import random
import string
print("welcome to our random password Generator=")
def main():
            length=int(input("Enter the length of password you want"))
            lowerD=string.ascii_lowercase
            upperD=string.ascii_lowercase
            digitD=string.digits
            symbolD= string.punctuation
            combine=lowerD+upperD+digitD+symbolD
            y=random.sample(combine,length)
            password="".join(y)
            print(password)
            main()
main()            