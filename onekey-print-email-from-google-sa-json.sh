cd
# ~/AutoRclone/accounts 为 server account json 文件所在目录，根据实际情况替换
cat ~/AutoRclone/accounts/*.json | grep "client_email" | awk '{print $2}'| tr -d ',"' | sed 'N;N;N;N;N;N;N;N;N;/^$/d;G' > ~/email.txt
