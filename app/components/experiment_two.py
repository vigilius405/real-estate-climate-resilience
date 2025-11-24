import reflex as rx


def experiment_two_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("flask-conical", class_name="w-16 h-16 text-violet-200 mb-6"),
            rx.el.h2(
                "Experiment 2", class_name="text-3xl font-bold text-gray-800 mb-4"
            ),
            rx.el.p(
                "This module is currently under development.",
                class_name="text-xl text-gray-500 font-medium mb-8",
            ),
            rx.el.div(
                rx.el.span(
                    "Planned Feature:", class_name="font-bold text-gray-700 mr-2"
                ),
                "Interactive Resilience Map Testing",
                class_name="inline-block px-4 py-2 bg-white rounded-full border border-gray-200 text-gray-600 shadow-sm",
            ),
            class_name="flex flex-col items-center justify-center h-[60vh] text-center",
        ),
        class_name="w-full h-full p-12",
    )