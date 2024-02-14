from django.shortcuts import render

# Create your views here.
# def contact(request):
#     # return render(request,'./first_app/index.html',context={'author':'phitron'})
#     return render(request,'./first_app/index.html',{'author':'phitron','age':19,'marks':19})


# def contact(request):
#     return render(request,'./first_app/index.html',{'courses' : [
#         {
#             'id' : 1,
#             'course' : 'C',
#             'teacher' : 'Rahim'
#         },
#         {
#             'id' : 2,
#             'course': 'c++',
#             'teacher' : 'karim'
#         },
#         {
#             'id' : 3,
#             'course': 'python',
#             'teacher' : 'fahim'
#         },
#     ]})

def contact(request):
    return render(request,'./first_app/index.html',{"name" : "I am Rahim", "marks" : 86, "Lst" : [24,3,10,5], "blog" : "Lorem Just type lorem in html to generate a paragraph of dummy text. Control how much text is generated with a number suffix, such as lorem10 to generate 10 words of dummy text. You can also combine lorem with other Emmet abbreviation"})