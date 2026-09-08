cmake -S . -B build -G "MinGW Makefiles"
cmake --build ./build 
./build/eventLogger.exe