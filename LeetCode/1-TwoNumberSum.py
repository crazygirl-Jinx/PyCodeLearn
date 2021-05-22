class Solution:
    
    def two_number(self, number_array:list[int], target:int) -> list[int]:
        

        # res_array = []; 
        # for i in range(len(number_array)):
        #     for n in range(i+1, len(number_array)):
        #         print(i,n)
        #         if number_array[i] + number_array[n] == target:
        #             res_array.append(i);
        #             res_array.append(n);
        #             break;

        # return res_array;
        karray= {};
        for index, number in enumerate(number_array):
            d = target - number;
            if d in karray:
                return [karray[d], index];
            karray[d] = index;
            

def main():
    solution = Solution();
    res = solution.two_number([3,3],6)
    print(res);

if __name__ == '__main__':
    
    main();

