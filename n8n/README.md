# n8n Directory

n8n workflow configurations and custom nodes.

## Directory Structure

- **workflows/** - Exported n8n workflow JSON files
- **credentials/** - Credential templates (actual credentials should not be committed)
- **nodes/** - Custom n8n nodes specific to LocalNest

## Workflow Organization

Workflows should be exported from n8n and committed here for version control and sharing. Name workflows descriptively:

- `camera_motion_detection.json`
- `solar_monitoring.json`
- `evening_automation.json`

## Custom Nodes

Custom n8n nodes can be developed here to extend functionality specific to LocalNest integrations.
