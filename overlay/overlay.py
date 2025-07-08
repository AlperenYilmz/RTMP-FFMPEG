# DESCRIPTION
# This script will request an 160x160 bit image from picsum.photos
# for every 10 seconds, and saves it at the same directory
# Script will be running in the background in endless loop


import requests, time

def main():
    img_cntr = 0
    while True:
        try:
            print("OVERLAY SERVICE: Parsing random overlay...")
            # random 160 bit square image for overlay from lorem picsum 
            response = requests.get("https://picsum.photos/160", timeout=3)
            if response.status_code == 200:
                with open("overlay.png", "wb") as img_file:
                    img_file.write(response.content)
                print("OVERLAY SERVICE: Overlay image number {0} parsed succesfully.".format(img_cntr))

            else:
                print("Failed to parse image file.")
        except Exception as e:
            print("Error:", e)
        img_cntr+=1
        time.sleep(10)

if __name__=="__main__":
    main()