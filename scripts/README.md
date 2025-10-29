# Scripts Directory

Python scripts organized by functionality for use with n8n workflows.

## Directory Structure

- **camera/** - Camera feed processing, motion detection, image analysis
- **solar/** - Solar panel monitoring, energy tracking, optimization
- **devices/** - Device control scripts (lights, locks, sensors, IoT)
- **automation/** - Automation logic and rule processing
- **ai/** - AI/ML models, LLM integration, vision processing

## Usage

Scripts in these directories are called by n8n workflows using Execute Command or Python Function nodes. Each script should:

- Accept input via command-line arguments or stdin (JSON)
- Return output as JSON to stdout
- Log errors to stderr
- Exit with appropriate status codes (0 = success, non-zero = error)
