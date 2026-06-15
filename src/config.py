from dataclasses import dataclass

@dataclass
class PipelineConfig:
    raw_file_path: str
    cleaned_file_path: str
    summary_report_path: str
