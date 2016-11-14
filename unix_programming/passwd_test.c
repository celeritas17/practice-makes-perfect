#include <stdio.h>
#include <pwd.h>

char *uid_to_name(uid_t);
struct passwd *getpwuid(uid_t);

int main(int ac, char *av[]){
	printf("%s\n", uid_to_name(55));
	return 0;
}

// (!) Not robust 
// (!) What if uid has no corresponding username 
char *uid_to_name(uid_t uid){
	return getpwuid(uid)->pw_name;
}
