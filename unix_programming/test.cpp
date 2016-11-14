#include <iostream>
#include <queue>

int main(){
	std::cout << "Hello, World\n";

	std::queue<int> my_queue;
	my_queue.push(1);
	my_queue.push(2);
	my_queue.push(3);

	std::cout << "my_queue:\n";

	while (!my_queue.empty()){
		std::cout << my_queue.front() << " ";
		my_queue.pop();
	}

	std::cout << "\n";

	return 0;
}