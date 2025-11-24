import reflex as rx
from typing import TypedDict
from datetime import datetime


class ResultEntry(TypedDict):
    participant_id: str
    choice: str
    understood_rising: str
    timestamp: str


class ExperimentState(rx.State):
    results: list[ResultEntry] = []
    current_participant_idx: int = 1
    selected_card: str = ""
    show_modal: bool = False
    temp_understood: str = "No"

    @rx.var
    def participant_label(self) -> str:
        return f"P{self.current_participant_idx}"

    @rx.var
    def csv_data(self) -> str:
        header = """Participant ID,Choice,Understood Rising,Timestamp
"""
        rows = [
            f"{r['participant_id']},{r['choice']},{r['understood_rising']},{r['timestamp']}"
            for r in self.results
        ]
        return (
            header
            + """
""".join(rows)
        )

    @rx.event
    def select_card(self, card_name: str):
        self.selected_card = card_name
        self.temp_understood = "No"
        self.show_modal = True

    @rx.event
    def set_understood(self, value: str):
        self.temp_understood = value

    @rx.event
    def toggle_modal(self):
        self.show_modal = not self.show_modal

    @rx.event
    def save_result(self):
        new_entry: ResultEntry = {
            "participant_id": self.participant_label,
            "choice": self.selected_card,
            "understood_rising": self.temp_understood,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
        }
        self.results.insert(0, new_entry)
        self.current_participant_idx += 1
        self.show_modal = False
        self.selected_card = ""
        return rx.toast("Result saved successfully.")

    @rx.event
    def copy_csv(self):
        yield rx.set_clipboard(ExperimentState.csv_data)
        yield rx.toast("CSV copied to clipboard!")

    @rx.event
    def reset_view(self):
        self.selected_card = ""
        self.show_modal = False
        return rx.toast("View reset for next participant.")