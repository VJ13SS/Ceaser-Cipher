'''WELCOME
This is a simple protoype of CEASER CIPHER where you will be asked to enter a word,Whether to be encrypted or decrypted,and the Value of Key to get the Ciphered Text....
So Go on...Keep your messages ciphered...Let it be private...'''
'''Last modified at 22/10/2023 7:04pm
 Author VJ 13 SS'''
import os
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
go="True"
while(go=="True"):
	word=input('\nEnter the word:  ').lower()
	do=input('\nType   "encrypt" for encrypting and "decrypt" for decrypting\n').lower()
	key=int(input('\nEnter the key: '))
	ciphertext=" "
	for letter in word:
		if(letter in alphabets):
			pos=alphabets.index(letter)
			if(do=='encrypt'):
				sum=pos+key
			elif(do=='decrypt'):
				sum=pos-key
				sum=sum+26
			else:
				print('Wrong input')
				break
			newpos=sum%26
			ciphertext+=alphabets[newpos]
		else:
			ciphertext+=letter
	print(f'\nCiphered text.....\n{ciphertext}')
	move=input('\n\nDo you wish to continue \nType yes or no\n ').lower()
	if(move=='yes'):
		go='True'
		os.system('clear')
	else:
		go='False'
		print('Thank you')
		
