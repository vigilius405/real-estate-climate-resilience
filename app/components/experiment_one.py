import reflex as rx
from app.states.experiment_state import ExperimentState


def sparkline_svg() -> rx.Component:
    return rx.el.svg(
        rx.el.path(
            d="M0 20 L10 18 L20 22 L30 15 L40 12 L50 14 L60 5",
            stroke="currentColor",
            stroke_width="2",
            fill="none",
            class_name="text-emerald-500",
        ),
        rx.el.circle(cx="60", cy="5", r="3", class_name="fill-emerald-500"),
        view_box="0 0 65 25",
        class_name="h-8 w-24",
    )


def card_a_static() -> rx.Component:
    return rx.el.button(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "NEIGHBORHOOD A",
                    class_name="text-xs font-bold tracking-wider text-gray-500 mb-1 block",
                ),
                rx.el.h3(
                    "Current Risk Assessment",
                    class_name="text-xl font-bold text-gray-800 leading-tight",
                ),
                class_name="mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.span("63", class_name="text-5xl font-black text-orange-500"),
                    rx.el.span(
                        "/100", class_name="text-lg text-gray-400 font-medium ml-1"
                    ),
                    class_name="flex items-baseline mb-2",
                ),
                rx.el.div(
                    rx.icon(
                        "triangle-alert", class_name="w-5 h-5 text-orange-500 mr-2"
                    ),
                    rx.el.span(
                        "Moderate Climate Risk",
                        class_name="text-orange-600 font-semibold",
                    ),
                    class_name="flex items-center bg-orange-50 px-3 py-1.5 rounded-lg w-fit mb-6",
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("waves", class_name="w-6 h-6 text-gray-400 mb-1"),
                    rx.el.span(
                        "Flood Zone", class_name="text-xs font-medium text-gray-500"
                    ),
                    class_name="flex flex-col items-center justify-center p-3 bg-gray-50 rounded-xl",
                ),
                rx.el.div(
                    rx.icon("sun", class_name="w-6 h-6 text-gray-400 mb-1"),
                    rx.el.span(
                        "Heat Island", class_name="text-xs font-medium text-gray-500"
                    ),
                    class_name="flex flex-col items-center justify-center p-3 bg-gray-50 rounded-xl",
                ),
                class_name="grid grid-cols-2 gap-3",
            ),
            class_name="p-6 h-full flex flex-col justify-between",
        ),
        on_click=lambda: ExperimentState.select_card("Static (Card A)"),
        class_name="group relative w-full md:w-96 h-[400px] bg-white rounded-3xl border border-gray-200 shadow-sm hover:shadow-xl hover:border-violet-200 hover:-translate-y-1 transition-all duration-300 text-left overflow-hidden",
    )


def card_b_trend() -> rx.Component:
    return rx.el.button(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "NEIGHBORHOOD B",
                    class_name="text-xs font-bold tracking-wider text-violet-600 mb-1 block",
                ),
                rx.el.h3(
                    "Resilience Projection",
                    class_name="text-xl font-bold text-gray-800 leading-tight",
                ),
                class_name="mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.span("72", class_name="text-5xl font-black text-violet-600"),
                    rx.el.span(
                        "/100", class_name="text-lg text-gray-400 font-medium ml-1"
                    ),
                    class_name="flex items-baseline mb-2",
                ),
                rx.el.div(
                    rx.icon("trending-up", class_name="w-5 h-5 text-emerald-500 mr-2"),
                    rx.el.span("Rising Score", class_name="text-emerald-700 font-bold"),
                    sparkline_svg(),
                    class_name="flex items-center gap-2 bg-emerald-50 px-3 py-1.5 rounded-lg w-fit mb-6 border border-emerald-100",
                ),
            ),
            rx.el.div(
                rx.el.ul(
                    rx.el.li(
                        rx.icon(
                            "square_check",
                            class_name="w-4 h-4 text-violet-500 mr-2 mt-0.5 shrink-0",
                        ),
                        rx.el.span(
                            "Flood barriers installed 2023",
                            class_name="text-sm text-gray-600",
                        ),
                        class_name="flex items-start mb-3",
                    ),
                    rx.el.li(
                        rx.icon(
                            "square_check",
                            class_name="w-4 h-4 text-violet-500 mr-2 mt-0.5 shrink-0",
                        ),
                        rx.el.span(
                            "Heat-reflective pavement planned",
                            class_name="text-sm text-gray-600",
                        ),
                        class_name="flex items-start",
                    ),
                    class_name="bg-violet-50/50 rounded-xl p-4 border border-violet-100",
                )
            ),
            class_name="p-6 h-full flex flex-col justify-between",
        ),
        on_click=lambda: ExperimentState.select_card("Trend (Card B)"),
        class_name="group relative w-full md:w-96 h-[400px] bg-white rounded-3xl border-2 border-violet-100 shadow-md hover:shadow-2xl hover:border-violet-400 hover:-translate-y-1 transition-all duration-300 text-left overflow-hidden",
    )


def facilitator_modal() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(
                class_name="fixed inset-0 bg-gray-900/40 backdrop-blur-sm z-40 animate-fade-in"
            ),
            rx.radix.primitives.dialog.content(
                rx.radix.primitives.dialog.title(
                    "Facilitator Check",
                    class_name="text-xl font-bold text-gray-800 mb-1",
                ),
                rx.radix.primitives.dialog.description(
                    f"Record participant response for {ExperimentState.participant_label}",
                    class_name="text-sm text-gray-500 mb-6",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "Participant chose:",
                            class_name="text-sm font-medium text-gray-500",
                        ),
                        rx.el.p(
                            ExperimentState.selected_card,
                            class_name="text-lg font-bold text-violet-700",
                        ),
                        class_name="bg-violet-50 p-4 rounded-xl mb-6 border border-violet-100",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Did the participant understand the 'Rising' trend indicator?",
                            class_name="block text-sm font-bold text-gray-700 mb-3",
                        ),
                        rx.el.div(
                            rx.el.button(
                                "Yes, Understood",
                                on_click=lambda: ExperimentState.set_understood("Yes"),
                                class_name=rx.cond(
                                    ExperimentState.temp_understood == "Yes",
                                    "flex-1 py-3 px-4 rounded-lg bg-emerald-600 text-white font-semibold shadow-md transition-all",
                                    "flex-1 py-3 px-4 rounded-lg bg-gray-100 text-gray-600 font-medium hover:bg-gray-200 transition-all",
                                ),
                            ),
                            rx.el.button(
                                "No / Unsure",
                                on_click=lambda: ExperimentState.set_understood("No"),
                                class_name=rx.cond(
                                    ExperimentState.temp_understood == "No",
                                    "flex-1 py-3 px-4 rounded-lg bg-rose-600 text-white font-semibold shadow-md transition-all",
                                    "flex-1 py-3 px-4 rounded-lg bg-gray-100 text-gray-600 font-medium hover:bg-gray-200 transition-all",
                                ),
                            ),
                            class_name="flex gap-3",
                        ),
                        class_name="mb-8",
                    ),
                    rx.el.div(
                        rx.radix.primitives.dialog.close(
                            rx.el.button(
                                "Cancel",
                                class_name="px-5 py-2.5 rounded-lg text-gray-600 font-medium hover:bg-gray-100 transition-colors",
                            )
                        ),
                        rx.el.button(
                            "Save Result",
                            on_click=ExperimentState.save_result,
                            class_name="px-6 py-2.5 rounded-lg bg-violet-600 text-white font-bold hover:bg-violet-700 shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-0.5",
                        ),
                        class_name="flex justify-end gap-2 pt-4 border-t border-gray-100",
                    ),
                ),
                class_name="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white rounded-2xl shadow-2xl p-8 w-full max-w-md z-50 focus:outline-none animate-scale-in",
            ),
        ),
        open=ExperimentState.show_modal,
        on_open_change=ExperimentState.toggle_modal,
    )


def results_table() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3("Session Results", class_name="text-lg font-bold text-gray-800"),
            rx.el.div(
                rx.el.button(
                    rx.icon("copy", class_name="w-4 h-4 mr-2"),
                    "Copy CSV",
                    on_click=ExperimentState.copy_csv,
                    class_name="flex items-center px-3 py-1.5 text-sm font-medium text-violet-700 bg-violet-50 hover:bg-violet-100 rounded-lg transition-colors",
                ),
                class_name="flex gap-2",
            ),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "ID",
                            class_name="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider bg-gray-50 rounded-tl-lg",
                        ),
                        rx.el.th(
                            "Choice",
                            class_name="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider bg-gray-50",
                        ),
                        rx.el.th(
                            "Understood Rising",
                            class_name="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider bg-gray-50",
                        ),
                        rx.el.th(
                            "Time",
                            class_name="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider bg-gray-50 rounded-tr-lg",
                        ),
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        ExperimentState.results,
                        lambda row: rx.el.tr(
                            rx.el.td(
                                row["participant_id"],
                                class_name="px-4 py-3 text-sm font-medium text-gray-900 border-b border-gray-100",
                            ),
                            rx.el.td(
                                row["choice"],
                                class_name="px-4 py-3 text-sm text-gray-600 border-b border-gray-100",
                            ),
                            rx.el.td(
                                rx.el.span(
                                    row["understood_rising"],
                                    class_name=rx.cond(
                                        row["understood_rising"] == "Yes",
                                        "inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800",
                                        "inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800",
                                    ),
                                ),
                                class_name="px-4 py-3 border-b border-gray-100",
                            ),
                            rx.el.td(
                                row["timestamp"],
                                class_name="px-4 py-3 text-sm text-gray-400 border-b border-gray-100 font-mono",
                            ),
                        ),
                    )
                ),
                class_name="min-w-full",
            ),
            class_name="overflow-hidden rounded-xl border border-gray-200 bg-white",
        ),
        class_name="mt-8 w-full max-w-4xl mx-auto",
    )


def experiment_one_view() -> rx.Component:
    return rx.el.div(
        facilitator_modal(),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "EXPERIMENT 1",
                        class_name="text-violet-600 font-bold tracking-widest text-xs mb-2 block",
                    ),
                    rx.el.h1(
                        "Trend vs. Static Choice",
                        class_name="text-3xl md:text-4xl font-bold text-gray-900 mb-4 font-heading",
                    ),
                    rx.el.p(
                        "Scenario: You are looking to buy a home for the next 10 years. Compare these two neighborhoods based on their climate resilience data.",
                        class_name="text-lg text-gray-600 max-w-2xl mx-auto leading-relaxed",
                    ),
                    class_name="text-center mb-12",
                ),
                rx.el.div(
                    card_a_static(),
                    rx.el.div(
                        "OR",
                        class_name="flex items-center justify-center text-gray-400 font-bold text-xl bg-white w-12 h-12 rounded-full shadow-sm border border-gray-200 z-10 md:my-auto my-4",
                    ),
                    card_b_trend(),
                    class_name="flex flex-col md:flex-row gap-6 md:gap-8 justify-center items-center md:items-stretch relative",
                ),
                class_name="max-w-5xl mx-auto mb-16",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        f"Current Participant: {ExperimentState.participant_label}",
                        class_name="text-sm font-bold text-gray-500 uppercase tracking-wider mr-4",
                    ),
                    rx.el.button(
                        "Next Participant (Reset View)",
                        on_click=ExperimentState.reset_view,
                        class_name="text-sm font-semibold text-violet-600 hover:text-violet-800 hover:underline transition-all",
                    ),
                    class_name="flex items-center justify-center mb-6 bg-gray-50 py-3 rounded-lg border border-gray-200 w-fit mx-auto px-6",
                ),
                results_table(),
                class_name="border-t border-gray-200 pt-12",
            ),
            class_name="px-6 py-12 md:py-20 max-w-7xl mx-auto",
        ),
        class_name="min-h-full bg-gray-50/50",
    )