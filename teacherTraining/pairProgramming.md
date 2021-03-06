Pair Programming (1 Hour)
-------------------------

ITT CCF 4.9
> Paired and group activities can increase pupil success, but to work together effectively pupils need guidance, support and practice
ITT CCF 4.10
> How pupils are grouped is also important; care should be taken to monitor the impact of groupings on pupil attainment, behaviour and motivation.

* [Quick Read: Using pair programming to support learners](https://blog.teachcomputing.org/quick-read-pair-programming-supports-learners/) 2019 NCCE - 1 page A4

* [khanacademy.org - Pair programming in the classroom](https://www.khanacademy.org/khan-for-educators/resources/teacher-essentials/teaching-computing/a/pair-programming-in-the-classroom?modal=1)
    * [Pair Programming-in-a-Box: The Power of Collaborative Learning](https://www.ncwit.org/resources/pair-programming-box-power-collaborative-learning) - National Center for Women in IT
* [repl.it](https://repl.it/)
* [Visual Studio Live Share](https://visualstudio.microsoft.com/services/live-share/)
    * [Collaboration made easy with Visual Studio Live Share](https://www.youtube.com/watch?v=9QXwSg9-2qQ) YouTube Video

* One dev-environment - multiple inputs
    * Single machine with two keyboards plugged in
    * Remote code tools
        * repl.it
        * LiveShare
        * Others ...

### Benefits
* Social communication
    * Historically/traditionally not a skill that a _reclusive self taught programmers_ had
        * Communication is important - challenge the stereotype
            * (Simplified) Girls are socially trained to be _perfect_ and not make mistakes.
                * Solo coding his hard and a personal threat.
    * Is expected skill/behaviour in industry
    * Coding IS a social profession
        * Building ANYTHING of significant value requires more than one person
* Spend less time _blocked_
    * (Struggling/grappling with a concept is not the same as blocked)
* Share failure and Share success leads to More frequent success
* Re-enforce concepts by having to articulate them
* Natural practice for technical language

### My experience

* I cant express the joy and safety of coding shoulder to shoulder with my colleges
* We were both constantly learning
* We channelled each others ideas
* Senior members of the team shared insights and reasons
* Weaker members asked questions and grew
* Is a juniors didn't understand the code then it had to be made simple enough and commented for them to understand
* Code was overall of a higher quality
* I felt like part of a team
    * I grew
    * I learnt
    * I shared
* I feel alive (human), connected and safe when pair programming

### Rules/Notes/Guide for Pair programming 

* [Summary of A Comparison of Two Pair Programming Configurations for Upper Elementary Students](https://blog.teachcomputing.org/summary-of-a-comparison-of-two-pair-programming-configurations-for-upper-elementary-students/)
    * Pair programming with primary students
    * 2 Computers + live edit tooling
    * Research categorised 3 types of conversations
        * Exploratory conversation - learners challenge each other, offering explanation and alternative ideas.
        * Cumulative conversation - learners seek to avoid conflict and therefore converse uncritically.
        * Disputational conversation - learners tend to have unresolved disagreements.

* Do 50% of the typing (really try to keep to this)
* Do 50%ish of the talking
    * If you talk more than 75% of the time - ask your partner questions
* One person can be coding while another looks something up (make sure you both fully understand the code when you return)
* We should never ridicule each other for mistakes, even in a joking way (from list below)
* [Formative Teaching Methods - Geoff Petty Jan 2004](http://geoffpetty.com/wp-content/uploads/2012/12/FormativeTeachingMethods2.doc) - from [Active Learning](http://geoffpetty.com/for-teachers/active-learning/)
    * We will learn best if we all agree that:
        * It’s okay if you don’t fully understand a concept first time, learning takes time
        * If work is graded, aim to beat your own record, not someone else’s
            * However, grading should be avoided where possible
        * What counts is whether you understand the problem and solution, or question and answer eventually:
            * not whether you got it right first time
            * not whether you got it wrong just because of a silly slip
        * It is not humiliating to make a mistake
            * We all make mistakes when we learn
            * Indeed is part of how we learn
            * If we don’t make mistakes the work is too easy for us to learn at our maximum rate
        * Mistakes are useful  because they tell us where we can improve
        * Its good for learning to admit to not understanding and to admit to mistakes and then ask for clarification
        * we should never ridicule each other for mistakes, even in a joking way
        * You will learn from mistakes if you find out how to do it without mistakes next time, and really understand this

Task
----

* [repl.it](https://repl.it/)
    * Create a new repl
    * Get share link and share with your partner
        * you need to create an account for this feature
        * only one of your pair needs to do this
    * Have voice comms
* Try to pick a language you have not used before
    * I have solutions/stubs for `java`, `csharp`, `python`, `javascript`
* Requires you to
    * Define variables (`bool`, `string`)
    * Get index from an array
    * `for` loop and `while` loop
    * Concatenate strings
    * Compare strings
* [Code-cademy - All Cheatsheets](https://www.codecademy.com/resources/cheatsheets/all)
* ADVANCED: If you are HARDCORE you could create a stub and solution for another language (`c`, `ruby`, `go`, `rust`, `php`) - I would love to see some of these! please make a GitHubPR!


### Complete working example (for a language not supported in repl)

```vb
Module VisualBasic

    Sub Main()
        Dim data() as String = {"b", "d", "c", "a"}
        data = bubbleSort(data)
        Console.WriteLine(Join(data, ","))
    End Sub

    Function bubbleSort(data as String()) As String()
        Console.WriteLine("bubbleSort")
        Dim has_changed as Boolean = True
        Do While has_changed
            Console.WriteLine(Join(data, ","))
            has_changed = False
            For i As Integer = 0 To data.Length - 2
                Dim a as String = data(i)
                Dim b as String = data(i+1)
                Console.WriteLine("comparing "+i.toString()+":"+a+" with "+(i+1).toString()+":"+b)
                If a > b Then
                    Console.WriteLine("swap")
                    data(i) = b
                    data(i+1) = a
                    has_changed = True
                End If
            Next
        Loop
        bubbleSort = data
    End Function

End Module
```

```txt
bubbleSort
b,d,c,a
comparing 0:b with 1:d
comparing 1:d with 2:c
swap
comparing 2:d with 3:a
swap
b,c,a,d
comparing 0:b with 1:c
comparing 1:c with 2:a
swap
comparing 2:c with 3:d
b,a,c,d
comparing 0:b with 1:a
swap
comparing 1:b with 2:c
comparing 2:c with 3:d
a,b,c,d
comparing 0:a with 1:b
comparing 1:b with 2:c
comparing 2:c with 3:d
a,b,c,d
```

### Stub Programs

Copy and paste this starting code into your repl for the correct language

#### python
```python
def bubbleSort(data):
    print('bubbleSort')
    # CODE GOES HERE!
    return data

if __name__ == '__main__':
    data = ['b', 'd', 'c', 'a']
    data = bubbleSort(data)
    print(data)
```

#### csharp
```csharp
using System;

class MainClass {

  public static void Main (string[] args) {new MainClass();}
  public MainClass() {
    string[] data = new string[]{"b", "d", "c", "a"};
    data = bubbleSort(data);
    Console.WriteLine(String.Join(",", data));
  }

  String[] bubbleSort(String[] data) {
    Console.WriteLine("bubbleSort");
    // CODE GOES HERE!
    return data;
  }

}
```

#### java
```java
class Main {

  public static void main(String[] args) {new Main();}
  Main() {
    String[] data = new String[]{"b", "d", "c", "a"};
    data = bubbleSort(data);
    System.out.println(String.join(",", data));
  }

  String[] bubbleSort(String[] data) {
    System.out.println("bubbleSort");
    // CODE GOES HERE!
    return data;
  }

}
```

#### javascript
```javascript
function bubbleSort(data) {
    console.log('bubbleSort');
    // CODE GOES HERE!
    return data
}

data = ['b', 'd', 'c', 'a'];
data = bubbleSort(data);
console.log(data);
```
