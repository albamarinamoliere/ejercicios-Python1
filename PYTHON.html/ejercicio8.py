 def es_palindromo(original):

	txt=list(palabra)
	txt.reverse()
	cadena = "".join(txt)
	if cadena == original:
		print True
	else:
		print False


def es_palindromo2(original):
	cadena = original[::-1]
	print cadena == original


