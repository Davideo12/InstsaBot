from multiprocessing import Process
from InstaBot import InstaBot

USERNAME = "sp4ce_images"
PASSWORD = "mystalkerbotpass"

def main():
    myBot = InstaBot(USERNAME, PASSWORD)
    
    p1 = Process(target=myBot.post_image)
    p2 = Process(target=myBot.follow_people)

    p1.start()
    p2.start()

if __name__ == '__main__':
    main()