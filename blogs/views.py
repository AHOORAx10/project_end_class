from django.db.models import Max, Min, Avg
from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Karbaran,Product
# Create your views here.

all_posts=[
    {
    'slug': 'python-programing',
    'title': 'python',
    'author': 'isvandi',
    'image': 'PY.jpeg',
    'date': date(2019, 3, 3),
    'short_description': 'python is Help and open source',
    'content': '''Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

    Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python itself, testifying to Python's introspective power. On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective.''',},


    {'slug': 'HTML-Programming',
    'title': 'HTML',
    'author': 'Pouya',
    'image':' HTML.png',
    'date': date.today(),
    'short_description': 'HTML stands for Hyper Text Markup Language',
    'content': '''The HyperText Markup Language or HTML is the standard markup language for documents designed to be displayed in a web browser. It defines the meaning and structure of web content. It is often assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript.

    Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for its appearance.''',},

    {'slug': 'C++-programming',
    'title': 'C++',
    'author': 'tehrani',
    'image': 'C++.png',
    'date': date.today(),
    'short_description':'The language was updated 4 major times in 2011, 2014, 2017, and 2020 to C++11, C++14, C++17, C++20.',
    'content':'''An IDE (Integrated Development Environment) is used to edit AND compile the code.
    Popular IDE's include Code::Blocks, Eclipse, and Visual Studio. These are all free, and they can be used to both edit and debug C++ code.

    Note: Web-based IDE's can work as well, but functionality is limited.

    We will use Code::Blocks in our tutorial, which we believe is a good place to start.

    You can find the latest version of Codeblocks at http://www.codeblocks.org/. Download the mingw-setup.exe file, which will install the text editor with a compiler.''',},

    {'slug': 'Java-programming',
    'title': 'Java',
    'author': 'Jakarta',
    'image': 'JAVA.png',
    'date': date.today(),
    'short_description': 'Not to be confused with Java (software platform), JavaScript, or Javanese language.',
    'content':'''Java is a high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible. It is a general-purpose programming language intended to let programmers write once, run anywhere (WORA),[17] meaning that compiled Java code can run on all platforms that support Java without the need to recompile.''',},

    {'slug': 'Database-SQLite',
    'title': 'Database',
    'author': 'Isavandi',
    'image': 'SQLite.jpeg',
    'date' : date.today(),
    'short_description': 'SQLite is a Database',
    'content': '''SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world. SQLite is built into all mobile phones and most computers and comes bundled inside countless other applications that people use every day.',}''',},

]



def get_date(post):
    return post['date']



def index(request):
    # d=list(all_post)
    # contex={'a':d}
    # return render(request,'blogs/index.html',contex)
    storted_post=sorted(all_posts,key=get_date)
    leatests=storted_post[-2:]
    return render(request,'blogs/index.html',{'leatest_post':leatests})


def posts(request):
    return render(request,'blogs/all_post.html')

def single_post(request,slug):
    post=next(post for post in all_posts if post['slug']==slug)
    return render(request,'blogs/post_details.html',{'post':post})


def Karbaran_list(request):
    all_karbaran = Karbaran.objects.all()
    all_karbaran = Karbaran.objects.all()
    all_karbaran = Karbaran.objects.all()
    all_karbaran = Karbaran.objects.all()

    return render(request,'blogs/Karbaran_list.html' ,{'all_karbaran': all_karbaran})


def Product_list(request):
    # all_product = Product.objects.all()
    # all_product = Product.objects.all()
    # all_product = Product.objects.all()
    # all_product = Product.objects.all()
    # return render(request, 'blogs/Product_list.html', {'all_product': all_product})
    all_product=Product.objects.all().order_by('-price')
    number_of_product=all_product.count()
    info=all_product.aggregate(Avg('price'),Max('price'),Min('price'),Max('ratings'))
    return render(request,'blogs/product_list.html',{'all_product':all_product,'number_of_product':number_of_product,'info':info})

def product_detail(request,slug):
    products = get_object_or_404(Product,slug=slug)
    return render(request,'blogs/product_details.html',{'product':products})