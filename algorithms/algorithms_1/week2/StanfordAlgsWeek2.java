import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Arrays;

public class StanfordAlgsWeek2 {
    public static int choosePivot(int[] nums, int l, int r){
        int median, middle = (r - l)%2 == 0 ? l + (r - l - 1)/2 : l + (r - l)/2; //(!) watch the offset!
        int[] pivotCandidates = {nums[l], nums[middle], nums[r - 1]};
        Arrays.sort(pivotCandidates);
        if (nums[l] == pivotCandidates[1]){
            median = l;
        }
        else if (nums[r - 1] == pivotCandidates[1]){
            median = r - 1;
        }
        else {
            median = middle;
        }
        return median;
    }
    
    public static int partition(int[] nums, int l, int r){
        int pivot = nums[l], temp, i, j;
        i = j = l + 1;
        for (; j < r; j++){
            if (nums[j] < pivot){
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
            }
        }
        
        // put the pivot where it belongs
        temp = nums[i - 1];
        nums[i - 1] = nums[l];
        nums[l] = temp;

        return i - 1; // location of pivot in partitioned array
    }
    
    public static int quicksortComparisons(int[] nums, int l, int r){
        if (r - l < 1){
            return 0;
        }
        
        int temp, comparisons = r - l - 1;
        int p = StanfordAlgsWeek2.choosePivot(nums, l, r);
        temp = nums[l];
        nums[l] = nums[p];
        nums[p] = temp;
        int boundary = StanfordAlgsWeek2.partition(nums, l, r);
        comparisons += StanfordAlgsWeek2.quicksortComparisons(nums, l, boundary);
        comparisons += StanfordAlgsWeek2.quicksortComparisons(nums, boundary + 1, r);
        return comparisons;
    }
  
    public static void main(String[] args) throws IOException {
        int[] nums = new int[10000];
        try {
            BufferedReader br = new BufferedReader(new FileReader("nums.txt"));
            String line;
            for (int i = 0; (line = br.readLine()) != null; i++) {
                nums[i] = Integer.parseInt(line, 10);
            }    
        } catch(FileNotFoundException e){
         e.printStackTrace();
        }
        StanfordAlgsWeek2 algs = new StanfordAlgsWeek2();
        int c = StanfordAlgsWeek2.quicksortComparisons(nums, 0, nums.length);
        System.out.println(c);
    }
}
