#question 1
from plotnine.data import economics
print(economics)
from plotnine.data import economics
from plotnine import ggplot, aes, geom_line

p=(
    ggplot(economics) 
    + aes(x="date", y="pop")  
    + geom_line()  
)
p.show()

#question 2
from plotnine.data import mpg
from plotnine import ggplot, aes, geom_point

p=(ggplot(mpg) + aes(x="class", y="hwy") + geom_point())
p.show()