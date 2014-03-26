from random import shuffle

class RUS:

    def __init__(self, filename=''):
        self.filename = filename
        self.data = {}

    def fileout(self):
        base_filename = self.filename.rsplit('.', 1)
        return base_filename[0] + '_rus.' + base_filename[1]

    def min_topic(self):
        return min([len(self.data[topic]) for topic in self.data])

    def load(self):
        fd = open(self.filename, 'r')
        for line in fd:
            topic = line.rsplit(',',1)[1].strip()
            if topic in self.data:
                self.data[topic].append(line)
            else:
                self.data[topic] = [line]
        fd.close()

    def display(self):
        for topic in self.data:
            print topic, len(self.data[topic])

    def writeFile(self):
        min_topic_length = self.min_topic()
        fd = open(self.fileout(),'w')
        for topic in self.data:
            shuffle(self.data[topic])
            for line in self.data[topic][0:min_topic_length]:
                fd.write(line)
        fd.close()



if __name__ == '__main__':
    rus = RUS('dmoz0409_Shopping_train_copy.csv')
    print rus.fileout()
    rus.load()
    print 'Min:', rus.min_topic()
    rus.display()
    #rus.writeFile()
