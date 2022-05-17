#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <libgen.h>
#include <sys/acl.h>
#include <unistd.h>

const char* acl_logic = "u::---,g::---,g:root:rwx,g:users:rw-,o::---,m::rwx";

int main(int argc, char *argv[]) {
	acl_t acl;

	acl = acl_from_text(acl_logic);

	if (!acl) {
		perror(argv[0]);
		return 1;
	}

	if (acl_valid(acl) != 0) {
        perror(argv[0]);
		acl_free(acl);
		return 1;
	}

	chown(argv[1], 0, 0);
    if (acl_set_file(argv[1], ACL_TYPE_ACCESS, acl) != 0) {
        perror(argv[0]);
        acl_free(acl);
        return 1;
    }

	acl_free(acl);
	return 0;
}
