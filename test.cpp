#include <iostream>
#include <ctime>

using namespace std;

int main() {
  time_t now = time(0);

  char* dt = ctime(&now);

  cout << "The local date is : " << dt << endl;

  tm *gmtm = gmtime(&now);
  dt = asctime(gmtm);
  cout << "The UTC date is : " << dt << endl;
}
