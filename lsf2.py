import pandas as pd
from os import listdir
from os.path import exists, join
import json
import matplotlib.pyplot as plt
# from sys import argv

#[] Index file

def dispIndex(id = None):
    with open("package/messages/index.json", "r") as index:
        data = json.load(index)

    index = pd.DataFrame({"FID": data.keys(), "Usernames": data.values()})
    index = pd.Series(data.values(), index= data.keys())
    if id == None:
        return index
    else:
        if index[id] != None:
            return index[id]
        else:
            return "[Deleted User]"


#[] Display a single chat's messages

def dispChat(path, chat_id):
    if exists(path):
            with open(join(path, "messages", "c" + chat_id, "messages.csv"), "r") as messages:
                chat = pd.read_csv(messages)
                chat = chat.drop(columns= ["ID", "Attachments"]).dropna()
                chat["Timestamp"] = chat["Timestamp"].astype("datetime64[s]")
                chat["Conversation name"] = dispIndex(chat_id)
                chat = chat[["Timestamp", "Conversation name", "Contents"]]
                return chat
    else:
        return "Unknown Path"


#[] Display all messages

def dispAll(path):
    if exists(path):
        msgsPath = listdir(join(path, "messages"))
        csvList = []
        for folder in msgsPath:
            if(folder == "index.json"):
                continue
            with open(join(path, "messages", folder, "messages.csv"), "r") as messages:
                chat = pd.read_csv(messages)
                chat = chat.drop(columns= ["ID", "Attachments"]).dropna()
                chat["Timestamp"] = chat["Timestamp"].astype("datetime64[s]")
                chat["Conversation name"] = dispIndex(folder[1:])
                chat = chat[["Timestamp", "Conversation name", "Contents"]]
                csvList.append(chat)
                messages.close()
        mergedDf = pd.concat(csvList, ignore_index=True)
        return mergedDf

    else:
        return "Unknown Path"


#[] Write a csv file containing all messages

def writeAll(path):
    with open("MessageHistory.csv", "w") as file:
        file.write(dispAll(path).to_string())
        file.close()


#[] Display a graph of messages per period

def dispPlot(path, id = None):
    if id == None:
        chat = dispAll(path)
    else:
        chat = dispChat(path, id)
    chat = chat[["Timestamp", "Contents"]]
    chat["Timestamp"] = chat["Timestamp"].astype("datetime64[D]")
    chat = chat.pivot_table(columns= "Timestamp", aggfunc= "size")
    values = []
    for value in chat:
        values.append(value)
    messages = pd.Series(values)
    time = pd.Series(chat.keys())
    chat = { "Timestamp": time, "Messages": messages }
    chat = pd.DataFrame(chat)
    print(chat)
    # print(chat.sort_values().to_string()
    chat.plot(kind="scatter", x="Timestamp", y="Messages", c="Messages", cmap="rainbow", title="Discord Messages Sent Over A Span Of Time")
    plt.show()


#[] Function calls

# print(dispChat())
# dispPlot()
# print(dispAll())
# writeAll()
