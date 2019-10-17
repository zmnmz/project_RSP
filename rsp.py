import random

print('가위바위보 게임을 시작합니다.')

#가위:1 바위:2 보:3


user = int(input("사용자 입력:"))
com = random.randint(1,3);

print('user: '+str(user)+' || com: '+str(com))

if (user*com)%2 == 0:
	if user < com:
		print('컴퓨터가 이겼습니다.')
	elif user > com:
		print('사용자가 이겼습니다.')
	else:
		print('무승부.')
else:
	if user < com:
		print('사용자가 이겼습니다.');
	elif user > com:
		print("컴퓨터가 이겼습니다.");
	else:
		print('무승부.')
