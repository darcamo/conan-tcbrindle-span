import os

from conans import ConanFile, tools


class TcbrindlespanConan(ConanFile):
    name = "tcbrindle-span"
    version = "2020-01-07-f17749c88cca9a3455cfdc9d907cc84850fd2423"
    license = "Boost Software License 1.0"
    author = "Darlan Cavalcante Moreira (darcamo@gmail.com)"
    url = "https://github.com/darcamo/conan-tcbrindle-span"
    description = "Implementation of C++20's std::span for older compilers"
    topics = ("C++", "C++20", "span")
    no_copy_source = True
    homepage = "https://github.com/tcbrindle/span"

    # No settings/options are necessary, this is header only

    def source(self):
        '''retrieval of the source code here. Remember you can also put the code
        in the folder and use exports instead of retrieving it with this
        source() method
        '''
        git = tools.Git(folder="tcbrindle-span")
        commit_sha1 = self.version.split("-")[-1]
        git.clone(self.homepage)
        git.checkout(commit_sha1)

    def package(self):
        self.copy("include/*.hpp", src="tcbrindle-span")

    def package_id(self):
        self.info.header_only()
