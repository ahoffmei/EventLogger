#include "eventLogger.h"

#include <chrono>
#include <ctime>
#include <iomanip>
#include <sstream>
#include <string> 

std::string getTime(int offset_ms = 0) {
    auto now = std::chrono::system_clock::now() + std::chrono::milliseconds(offset_ms); 
    std::time_t time = std::chrono::system_clock::to_time_t(now);

    std::tm utc_time{};
    gmtime_s(&utc_time, &time); 

    std::ostringstream oss;
    oss << std::put_time(&utc_time, "%Y-%m-%dT%H:%M:%SZ");

    return oss.str();
}

void BasicTest() {
    EventLogger::LogEvent(LogType::INFO, LogEvent::RECORDED_MEASUREMENT, 1.23, getTime());    
    EventLogger::LogEvent(LogType::INFO, LogEvent::RECORDED_MEASUREMENT, 1.25, getTime(500));    
    EventLogger::LogEvent(LogType::INFO, LogEvent::RECORDED_MEASUREMENT, 1.29, getTime(1000));    
}