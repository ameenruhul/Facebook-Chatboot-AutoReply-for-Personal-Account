
from fbchat import log, Client,Message

# Subclass fbchat.Client and override required methods
class Bot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        toggle = self.fetchThreadMessages(thread_id=thread_id, limit=1) 
        for message in toggle:
            pText=message.text.lower()

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        msgText = message_object.text.lower()

        if(msgText=="eid mubarak" or msgText=="eid" or msgText=="mubarak" or msgText=="eid mubarak"):
            reply = "Eid Mubarak <3"
        
        def sendMsgg():
            if (author_id!=self.uid):
               self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

        self.markAsDelivered(author_id, thread_id)

        sendMsgg()
 

client = Bot("<email>", "<pass>")
client.listen()