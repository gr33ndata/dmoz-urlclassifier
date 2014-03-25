from random import shuffle

class Dataset:

    def __init__(self, filename, max_test=1000):
        self.filename = filename
        #self.train_file = filename.rsplit('.')[0] + '_train.csv'
        #self.test_file = filename.rsplit('.')[0] + '_test.csv'
        self.max_test = max_test
        self.topic_names = set()
        self.topics = {}
        self.urls = []
        self.load()
        self.randomize()

    def load(self):
        fd = open(self.filename, 'r')
        for line in fd:
            topic = line.rsplit(',',1)[1].strip()
            self.urls.append([topic, line])
            self.topic_names.add(topic)
        fd.close()

    def randomize(self):
        shuffle(self.urls)    

    def whichFile(self, fd_train, fd_test, topic):
        if topic in self.topics:
            self.topics[topic] += 1
        else:
            self.topics[topic] = 1
        #print topic, self.topics[topic], '<=', self.max_test
        if self.topics[topic] <= self.max_test:
            return fd_test
        else:
            return fd_train

    def writeFiles(self):
        ''' Writes file into training and test sets.
            Test set contains 1000 URLs from each category
            Training and Test are done using single,
            multi-class (15 classes) classifier.
        '''
        base_filename = self.filename.rsplit('.')[0]
        train_file = base_filename + '_train.csv'
        test_file  = base_filename + '_test.csv'
        fd_train = open(train_file, 'w')
        fd_test  = open(test_file,  'w')
        for url in self.urls:
            #print 'U:', url
            topic, line = url
            fd = self.whichFile(fd_train, fd_test, topic)
            #line = line + '\n'
            fd.write(line)
        fd_train.close()
        fd_test.close()

    def writeFiles_Binary(self):
        #for topic in self.topic_names:
        for topic in list(self.topic_names):
            self.topics = {}
            base_filename = self.filename.rsplit('.')[0]
            train_file = base_filename + '_' + topic + '_train.csv'
            test_file  = base_filename + '_' + topic + '_test.csv'
            fd_train = open(train_file, 'w')
            fd_test  = open(test_file,  'w')
            for url in self.urls:
                url_topic, line = url
                fd = self.whichFile(fd_train, fd_test, url_topic)
                if url_topic != topic:
                    anti_topic = 'Non' + topic 
                    line = line.rsplit(',',1)[0] + ',' + anti_topic + '\n'
                fd.write(line)
            fd_train.close()
            fd_test.close()



def main(filename=''):

    ds = Dataset(filename)
    #ds.writeFiles()
    ds.writeFiles_Binary()

if __name__ == '__main__':

    main(filename='dmoz0409.csv')