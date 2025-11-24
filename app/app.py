import reflex as rx
from app.components.experiment_one import experiment_one_view
from app.components.experiment_two import experiment_two_view


def index() -> rx.Component:
    return rx.el.div(
        rx.el.header(
            rx.el.div(
                rx.el.div(
                    rx.icon("shield-check", class_name="w-8 h-8 text-white"),
                    rx.el.h1(
                        "Resilience Index Lab",
                        class_name="text-xl font-bold text-white tracking-tight",
                    ),
                    class_name="flex items-center gap-3",
                ),
                rx.el.div(
                    rx.el.span(
                        "Internal Testing Tool",
                        class_name="text-xs font-semibold text-violet-200 bg-violet-800/50 px-3 py-1 rounded-full border border-violet-700",
                    )
                ),
                class_name="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between",
            ),
            class_name="bg-gray-900 shadow-lg sticky top-0 z-30",
        ),
        rx.el.main(
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger(
                        "Trend vs Static",
                        value="exp1",
                        class_name="flex-1 px-4 py-3 text-sm font-medium text-gray-500 hover:text-gray-700 border-b-2 border-transparent data-[state=active]:border-violet-600 data-[state=active]:text-violet-600 transition-all outline-none cursor-pointer",
                    ),
                    rx.tabs.trigger(
                        "Map Interaction",
                        value="exp2",
                        class_name="flex-1 px-4 py-3 text-sm font-medium text-gray-500 hover:text-gray-700 border-b-2 border-transparent data-[state=active]:border-violet-600 data-[state=active]:text-violet-600 transition-all outline-none cursor-pointer",
                    ),
                    class_name="flex w-full border-b border-gray-200 bg-white sticky top-16 z-20",
                ),
                rx.tabs.content(
                    experiment_one_view(),
                    value="exp1",
                    class_name="outline-none animate-fade-in",
                ),
                rx.tabs.content(
                    experiment_two_view(),
                    value="exp2",
                    class_name="outline-none animate-fade-in",
                ),
                default_value="exp1",
                class_name="w-full",
            ),
            class_name="flex-1 w-full",
        ),
        class_name="font-sans min-h-screen bg-gray-50 flex flex-col text-gray-900",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
        rx.el.style("""
            .font-sans { font-family: 'Montserrat', sans-serif; }
            @keyframes fade-in {
                from { opacity: 0; transform: translateY(5px); }
                to { opacity: 1; transform: translateY(0); }
            }
            .animate-fade-in {
                animation: fade-in 0.3s ease-out forwards;
            }
             @keyframes scale-in {
                from { opacity: 0; transform: translate(-50%, -48%) scale(0.96); }
                to { opacity: 1; transform: translate(-50%, -50%) scale(1); }
            }
            .animate-scale-in {
                animation: scale-in 0.2s ease-out forwards;
            }
            """),
    ],
)
app.add_page(index, route="/")