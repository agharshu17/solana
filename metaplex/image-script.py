import os
  
# Function to rename multiple files
def main():
  
    for count, filename in enumerate(os.listdir("D:/Projects/Internship/Solana/tiger-art-2")):
        keyword = '.'
        before_keyword, keyword, after_keyword = filename.partition(keyword)
        dst = str(count) + '.' + after_keyword
        
        incr = count + 1
        file = 'D:/Projects/Internship/Solana/tiger-art-2/'+ str(count) + '.json'
        with open(file, 'w') as f:
            f.write('{"name":"'+ str(incr) + '","symbol":"","image":"'+ dst +'","properties":{"files":[{"uri":"'+ dst +'","type":"image/' + after_keyword + '"}],"category":"image","creators":[]},"description":"","seller_fee_basis_points":500}')
          
        # rename() function will
        # rename all the files
        src ='D:/Projects/Internship/Solana/tiger-art-2/'+ filename 
        dst ='D:/Projects/Internship/Solana/tiger-art-2/'+ dst
        os.rename(src, dst)
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()