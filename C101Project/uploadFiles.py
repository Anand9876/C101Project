import dropbox
import os

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root,filename)

                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                 
                with open(local_path,'rb') as f:
                       dbx.files_upload(f.read(),drop_path,mode=WriteMode('overwrite'))
def main():
        access_token ='sl.BDI5MXnlGEPGtzAlzbAQloKEL_0J8j13vPrefZINIBu-FZl7R8ysnrt7QNwbgGLCPH1sqcqJtytM0A_JKRMg5HhMRhz_Znprbr2CpWw1hjXqYG84gzpMSziPOyO0FLLwWgpiEASq'
        transferData=TransferData(access_token)
        file_from=str(input('Enter the file pathway to upload on cloudStorage'))
        file_to=input('Enter the full path to upload on dropbox')
        transferData.upload_file(file_from,file_to)
        print('file has been moved and uploaded!')

main()