from models import *

question = Question(questionid=111, testid=123, questionSt="Describe the provess of colonization", marks=5,
                    answerVec="Colonization (or colonisation) is a process by which a central system of power dominates the surrounding land and its components.Colonization refers strictly to migration, for example, to settler colonies in America or Australia, trading posts, and plantations, while colonialism to the existing indigenous peoples of styled new territories. Colonization was linked to the spread of tens of millions from Western European states all over the world. In many settled colonies, Western European settlers eventually formed a large majority of the population after killing or driving away indigenous peoples. Examples include the Americas, Australia and New Zealand. These colonies were occasionally called 'neo-Europes'. In other places, Western European settlers formed minority groups, which often used more advanced weaponry to dominate the people initially living in their places of settlement.")

question.save()
