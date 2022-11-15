from django.shortcuts import render

# Create your views here.
fe_student=None
def var():
    global student,f_student,py_student,j_student,titile1,titile2
    student={
        'sdata':[
                    {'id':"1001",
                        'name':"Krunal",
                        'yop':'2022',
                        'email':'krunal@gmail.com',
                        'skill':'python',                    
                        'per': 95,
                        'ret':'*',
                    }, 
                    {'id':"1002",
                        'name':"Sweetu",
                        'yop':'2022',
                        'email':'swettu@gmail.com',
                        'skill':'python',                    
                        'per': 85,
                        'ret':'*',
                    },  
                    {'id':"1003",
                        'name':"Nitin",
                        'yop':'2018',
                        'email':'nitin@gmail.com',
                        'skill':'java',                    
                        'per': 75,
                        'ret':'*',
                    },
                    {'id':"1004",
                        'name':"Bittu",
                        'yop':'2021',
                        'email':'bittu@gmail.com',
                        'skill':'python',                    
                        'per': 84,
                        'ret':'*',
                    },
                    {'id':"1005",
                        'name':"Jinit",
                        'yop':'2017',
                        'email':'jinit@gmail.com',
                        'skill':'java',                    
                        'per': 58,
                        'ret':'**',
                    },
                    {'id':"1006",
                        'name':"sumit",
                        'yop':'2016',
                        'email':'sumit@gmail.com',
                        'skill':'java',                    
                        'per': 61,
                        'ret':'**',
                    },
                    {'id':"1007",
                        'name':"hardik",
                        'yop':'2019',
                        'email':'hardik@gmail.com',
                        'skill':'java',                    
                        'per':72,
                        'ret':'**',
                    }, 
                    {'id':"1008",
                        'name':"Soham",
                        'yop':'2020',
                        'email':'soham@gmail.com',
                        'skill':'java',                    
                        'per':79,
                        'ret':'**',
                    },
                    {'id':"1009",
                        'name':"Hari",
                        'yop':'2021',
                        'email':'hari@gmail.com',
                        'skill':'pytohn',                    
                        'per':89,
                        'ret':'**',
                    }, {'id':"1010",
                        'name':"Aarth",
                        'yop':'2021',
                        'email':'aarth@gmail.com',
                        'skill':'java',                    
                        'per':86,
                        'ret':'*',
                    },                    
                ]
    }

    student_filter=dict()
    tem_b=student
    tem_a=tem_b['sdata']
    f_student={"filter_student":[]}
    for i in tem_a:
        if i['per'] > 60:
            f_student['filter_student'].append(i)

    py_student={"py_filter_student":[]}
    for j in f_student['filter_student']:
        if j['ret'] == '*' and j['skill'] == "python" :
            py_student['py_filter_student'].append(j)

    j_student={"j_filter_student":[]}
    for k in f_student['filter_student']:
        if k['ret'] == '*' and k['skill'] == "java" :
            j_student['j_filter_student'].append(k)
    
    # titile1="Py_spider"
    # titile2="j_spider"
    
    # print (j_student)
    return student,f_student,py_student,j_student

    
var()


def index(request):
    request.titile1="Py_spider"
    titile2="j_spider"       
    return render(request,"index.html",student)

def one(request):
   
    # try:
    #     global l
    #     l=request.GET.get("py_but")
        
    #     print (l)
    # except:
    #     print("Value ---> None")
        # l=request.GET["py_but"]

    return render(request,"one.html",f_student)


def filter(request):
    try:
        
        l=request.POST.get("py_but")
        l2=request.POST.get("j_but")

        if l=="Py_students":
            # print("Value --->py_spiders")
            z=py_student['py_filter_student']
            # print(z)
            return render(request,"filter.html",context={'fi_student':z,"l":l})

        if l2=="j_students":
            z=j_student["j_filter_student"]
            # print("Value ---> jspider")
            return render(request,"filter.html",context= {'fi_student':z,'l':l2})

        # print (l,l2)
    except:
        print("Value ---> None")
    
    # print (l)
    # return render(request,"filter.html",context = {'py_student':py_student,'j_student':j_student})
    
    
    
    
    
    
    
    
    # a= render(request,"filter.html",j_student)
    # b= render(request,"filter.html",py_student)

    # return a
    
    # return  render(request,"filter.html",j_student)
    # yield  render(request,"filter.html",py_student)



# i tey this one but it toooooooo confusing  12-11-2022 02:02 AM
# def index(request):
#     global student
#     student={
#         'sdata':[
#                     {'id':"1001",
#                         'name':"Krunal",
#                         'yop':'2022',
#                         'email':'krunal@gmail.com',
#                         'skill':'python',                    
#                         'per': 95,
#                         'ret':1
#                     }, 
#                     {'id':"1002",
#                         'name':"Sweetu",
#                         'yop':'2022',
#                         'email':'swettu@gmail.com',
#                         'skill':'python',                    
#                         'per': 85,
#                         'ret':1
#                     },  
#                     {'id':"1003",
#                         'name':"Nitin",
#                         'yop':'2018',
#                         'email':'nitin@gmail.com',
#                         'skill':'java',                    
#                         'per': 75,
#                         'ret':1
#                     },
#                     {'id':"1004",
#                         'name':"Bittu",
#                         'yop':'2021',
#                         'email':'bittu@gmail.com',
#                         'skill':'python',                    
#                         'per': 84,
#                         'ret':1
#                     },
#                     {'id':"1005",
#                         'name':"Jinit",
#                         'yop':'2017',
#                         'email':'jinit@gmail.com',
#                         'skill':'java',                    
#                         'per': 58,
#                         'ret':2
#                     },
#                     {'id':"1006",
#                         'name':"sumit",
#                         'yop':'2016',
#                         'email':'sumit@gmail.com',
#                         'skill':'java',                    
#                         'per': 61,
#                         'ret':2
#                     },
#                     {'id':"1007",
#                         'name':"hardik",
#                         'yop':'2019',
#                         'email':'hardik@gmail.com',
#                         'skill':'java',                    
#                         'per':72,
#                         'ret':2
#                     }, 
#                     {'id':"1008",
#                         'name':"Soham",
#                         'yop':'2020',
#                         'email':'soham@gmail.com',
#                         'skill':'java',                    
#                         'per':79,
#                         'ret':2
#                     },
#                     {'id':"1009",
#                         'name':"Hari",
#                         'yop':'2021',
#                         'email':'hari@gmail.com',
#                         'skill':'pytohn',                    
#                         'per':89,
#                         'ret':2
#                     }, {'id':"1010",
#                         'name':"Aarth",
#                         'yop':'2021',
#                         'email':'aarth@gmail.com',
#                         'skill':'pytohn',                    
#                         'per':56,
#                         'ret':2
#                     },   

                    
#                 ]
#     }
    
#     return render(request,"index.html",student)

# def one(request):
#     student_filter=dict()
#     tem_b=student
#     tem_a=tem_b['sdata']
#     f_student={"filter_student":[]}
#     for i in tem_a:
#         if i['per'] > 60:
#             f_student['filter_student'].append(i)
#     # print(student_filter)
#     # def glo():/
#         # global a
#     a=f_student
#     return render(request,"one.html",f_student)

# # e=one('pass')
# # print(e)
# def filter(request):
#     d_temp=None
#     py_student={"py_filter_student":[]}
#     for j in d_temp:
#         if j['ret'] < 2:
#             py_student['py_filter_student'].append(j)
    



#     return render(request,"filter.html",py_student)