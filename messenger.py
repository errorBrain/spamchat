import fbchat
import sys
from fbchat.models import *

print "\033[031;1m============================================================"
print "\033[039;1m UNTUK   :  SPAM CHAT MESSENGER"
print " GITHUB  :  https://github.com/Senitopeng/Spamchat.git\n"
print " PENGGUNA:  Ganti_Tulisan_Ini_Dengan_Namamu"
print "\033[031;1m============================================================\n"

user_name = raw_input(" \033[033;1mLogin Fb:> ")
password = raw_input(" Password:> ")
print "------------------------------------------------------------"
client = fbchat.Client(user_name, password)
friend_name = raw_input("\n Nama Fb Target: ") 
friends = client.searchForUsers(friend_name)
friend = friends[0]
message = raw_input(" Pesan To Target: ") 
times = raw_input(" Jumlah Pesan: ") 
for i in range(int(times)):
	message_id = client.sendMessage(message, thread_id=friend.uid, thread_type=ThreadType.USER)
print(" \n SPAM SUDAH DI KIRIM BOS\n (Parah Luh) Wkwkwwkkk...!")



