import java.util.Arrays;
import java.util.Random;

public class StanfordAlgsWeek3{
	public int choosePivot(int left, int right){
		return (new Random()).nextInt(right - left) + left;
	}

	public static int partition(int[] nums, int left, int right){
		int i, j, temp, pivot = nums[left];
		i = j = left + 1;

		for (; j < right; j++){
			if (nums[j] < pivot){
				temp = nums[i];
				nums[i] = nums[j];
				nums[j] = temp;
				i++;
			}
		}

		temp = nums[i - 1];
		nums[i - 1] = nums[left];
		nums[left] = temp;
		return i - 1;
	}

	public int Rselect(int[] nums, int left, int right, int order){
		if (right - left < 1){
			System.out.println("You dumbass, nothing there.");
			return -1;
		}

		if (right - left == 1){
			return nums[left];
		}

		int temp, boundary, p = choosePivot(left, right);

		// swap pivot into position 0
		temp = nums[left];
		nums[left] = nums[p];
		nums[p] = temp;

		boundary = partition(nums, left, right);

		// boundary is an array index, order is an order statistic
		if ((boundary + 1) == order){
			return nums[boundary];
		}
		if ((boundary + 1) > order){
			return Rselect(nums, left, boundary, order);
		}
		return Rselect(nums, boundary + 1, right, order);
	}

	public static void main(String[] args){
		StanfordAlgsWeek3 algs = new StanfordAlgsWeek3();
		int[] nums = {4, 8, 6, 1, 3, 5, 9, 2};
		System.out.println(Arrays.toString(nums));
		System.out.println(algs.Rselect(nums, 0, nums.length, 5));
	}
}
