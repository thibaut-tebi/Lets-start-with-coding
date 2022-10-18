%calculating the University of Ghana Grade using Matlab 

function UGgrading() 
%This fuction outputs one's grade depending on the mark entered 

examGrade=input('Enter your numerical grade\n'); 
switch true 
    case examGrade >100 
        disp('invalid') 
    case examGrade <=100 && examGrade>=80 
        disp(' A') 
    case examGrade <=79 && examGrade >=75 
        disp('B+') 
    case examGrade <=74 && examGrade >=70 
        disp('B') 
    case examGrade <=69 && examGrade >=65 
        disp('C+') 
    case examGrade <=64 && examGrade >=60 
        disp('C') 
    case examGrade <=59 && examGrade >=55 
        dips('D+') 
    case examGrade <=54 && examGrade >=50 
        disp ('D') 
    case examGrade <=49 && examGrade >=45 
        disp('E') 
    otherwise  
        disp('F') 
end 
end
