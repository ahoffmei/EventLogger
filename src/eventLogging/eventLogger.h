#pragma once 

#include <string> 
#include <cstdint>
#include <fstream>
#include <string>
#include <iostream>

// Customize based on preference 
enum class LogType {
    INFO = 0, 
    WARNING, 
    ERROR
}; 

// Customize based on expected events
enum class LogEvent {
    TRANSITION_HAPPENED = 0, 
    RECORDED_VALUE, 
    RECORDED_MEASUREMENT
};

class EventLogger {
private:
    static std::ofstream m_file;

    // Maybe just use a map for both of these???
    static std::string getLogTypeName(LogType type) {
        std::string name = ""; 
        switch(type) {
            case LogType::ERROR:    name = "ERROR"; break; 
            case LogType::INFO:     name = "INFO"; break; 
            case LogType::WARNING:  name = "WARNING"; break; 
        }

        return name; 
    }

    static std::string getLogEventName(LogEvent event) {
        std::string name = ""; 
        switch(event) {
            case LogEvent::TRANSITION_HAPPENED: name = "TRANSITION_HAPPENED"; break;
            case LogEvent::RECORDED_VALUE: name = "RECORDED_VALUE"; break; 
            case LogEvent::RECORDED_MEASUREMENT: name = "RECORDED_MEASUREMENT"; break; 
        }

        return name; 
    }

public:
    static void LogEvent(LogType type, LogEvent event, float value, std::string timestamp) {
        m_file  << timestamp                            << " "
                << EventLogger::getLogTypeName(type)    << " " 
                << EventLogger::getLogEventName(event)  << " " 
                << value                                << '\n'; 
    }

};