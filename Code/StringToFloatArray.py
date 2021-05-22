data1="33.1111111,33.222222,33.3333333,33.4444444,"
data2="116.1111111,116.222222,116.3333333,116.4444444,"

#合并成 
# new_data= [
# [116.1111111,33.1111111]，
# [116.222222,33.222222]，
# [16.3333333,33.3333333]，
# [116.4444444,33.4444444]
# ]

class Solution:
    def __init__(self) -> None:
        import json;
        self.json = json;
    def to_float_array(self, data1:str, data2:str):
        data1 = data1.split(",");
        data2 = data2.split(",");
        array1 = {};
        array2 = {};
        new_data = [];
        for s in data1:
            if s:
                s = s.split(".")
                array1[s[1]] = s[0];
        for s in data2:
            if s:
                s = s.split(".")
                array2[s[1]] = s[0];
        print(array1);
        print(array2)
        for d in array1:
            if d in array2:
                new_data.append([array1[d]+"."+d, array2[d]+"."+d])
        return new_data
                

            


        
        
import datetime

def main():
    solution = Solution();
    print(solution.to_float_array(data1, data2));

if __name__ == '__main__':
    start = datetime.datetime.now()
    main()
    print(datetime.datetime.now() - start)