import csv

def get_booksvalue():
    filename="db/bookstates.csv";
    fp=open(filename,"rt",encoding="utf-8");
    tsv=fp.read();

    rows=tsv.split("\n");
    result=[];
    for line in rows:
        cols=line.split(",");
        if len(cols)<=1:break;
        result.append(cols);
    return len(result);
def load_data():
    filename="db/bookstates.csv";
    fp=open(filename,"rt",encoding="utf-8");
    tsv=fp.read();

    rows=tsv.split("\n");
    result=[];
    for line in rows:
        cols=line.split(",");
        if len(cols)<=1:break;
        result.append(cols);

    return result;

def read_csv(filename):
    f = open(filename, "r")
    csv_data = csv.reader(f)
    list = [ e for e in csv_data]
    f.close()
    return list
    
def update_list2d(list, data):
    for i in range(len(list)):
        if list[i][0]==data[0][0]: list[i] = data[0]
    return list

def write_csv(filename, list):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(list)   

    f.close()

def write(booksname,num,username,RCjudge):#変更
    filename = 'db/bookstates.csv'
    csv_data = read_csv(filename)
    data = [[booksname,num,username]]
    if RCjudge==0:#readqr
        csv_data2 = update_list2d(csv_data, data)
    elif RCjudge==1:#createpy
        csv_data2=csv_data+data
    print(csv_data2)
    write_csv(filename, csv_data2)