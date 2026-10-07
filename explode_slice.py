import matplotlib .pyplot as plt

courses = ["Python", "Java", "Data Science", "Web"] 
students = [40, 25, 20, 15]
explode = [0.1, 0, 0, 0] 
plt.pie(    
    students,    
    labels=courses,    
    explode=explode,    
    autopct="%1.1f%%" 
) 
plt.show()
