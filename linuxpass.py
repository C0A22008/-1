import crypt

salt = '$y$j9T$u2d7BlAQGOHxms9Lg4cKo0$WCErDzoDFBY6EbiBNrbNvvgm.XcnZdLuzrUudGg9H06'
target = '$y$j9T$u2d7BlAQGOHxms9Lg4cKo0$WCErDzoDFBY6EbiBNrbNvvgm.XcnZdLuzrUudGg9H06'
passchar_list = 'abcdefghijkllmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#'

for i0 in range(len(passchar_list)):
	passchar0 = passchar_list[i0]
	for i1 in range(len(passchar_list)):
		passchar1 = passchar_list[i1]
		for i2 in range(len(passchar_list)):
			passchar2 = passchar_list[i2]
			for i3 in range(len(passchar_list)):
				passchar3 = passchar_list[i3]
				for i4 in range(len(passchar_list)):
					passchar4 = passchar_list[i4]
					for i5 in range(len(passchar_list)):
						passchar5 = passchar_list[i5]
						for i6 in range(len(passchar_list)):
							passchar6 = passchar_list[i6]
							for i7 in range(len(passchar_list)):
								passchar7 = passchar_list[i7]								
								passwd = passchar0 + passchar1 + passchar2 + passchar3 + passchar4 + passchar5 + passchar6 + passchar7
								print(passwd)
								cpass = crypt.crypt(passwd, salt)
								if cpass == target:
									print('Yes' + cpass)
									break
							else:
								continue
							break
						else:
							continue
						break
					else:
						continue
					break
				else:
					continue
				break
			else:
				continue
			break
		else:
			continue
		break
	else:
		continue
	break
