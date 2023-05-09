"""
# 자바
public class Book {
    String title;
    String author;

    Book(String title, String author) {
        this.title = title;
        this.author = author;
    }
}

Book [] subjectBooks = new Book[2]; // 공간 할당
subjectBooks[0] = new Book("딥러닝수학", "서지영");
subjectBooks[1] = new Book("점프투파이썬", "박응용");

ArrayList<Book> subjectBooks = new ArrayList<>();
subjectBooks.add(new Book("딥러닝수학", "서지영"));
subjectBooks.remove(index);
subjectBooks.remove(object o);
"""

# 학생마다 수강하는 과목이 다르다고 가정
# 중간고사 평균값 출력하는 코드 작성

class Subject:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Student:
    studentId = 20230000

    def __init__(self, name):
        Student.studentId += 1
        self.name = name
        self.subjectList = []

    # addSubject method 생성해서 subjectList.append

    def addSubjectPoints(self, name, score):
        subject = Subject(name, score)
        self.subjectList.append(subject)

    def printInfo(self):
        total = 0
        cnt = 0
        for val in self.subjectList:
            print(val.name, ' : ', val.score)
            total += val.score
            cnt += 1
        mean = total / cnt
        print(f'{self.name}의 학번은 {Student.studentId}이고, 중간고사 평균점수는 {mean}')
        # print(f'{self.name}의 학번은 {Student.studentId}이고, 중간고사 평균점수는 {total/len(self.subjectList)}')

std1 = Student("강은선")
std1.addSubjectPoints("딥러닝수학", 90)
std1.addSubjectPoints("자료구조", 100)
std1.addSubjectPoints("JAVA", 98)
std1.printInfo()

std2 = Student("구보람")
std2.addSubjectPoints("HTML", 100)
std2.addSubjectPoints("DATABASE", 90)
std2.addSubjectPoints("JAVA", 98)
std2.addSubjectPoints("Python", 90)
std2.printInfo()