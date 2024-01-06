import customtkinter as ctk


class ViewButtons:
    @staticmethod
    def show_component(parent, views, view_class, text, padx, pady):
        button = ctk.CTkButton(
            parent,
            text=text,
            command=lambda: ViewButtons.view_button_activate(views, view_class),
        )
        button.pack(padx=padx, pady=pady)

    @staticmethod
    def view_button_activate(views, view_class):
        for view_instance in views.values():
            view_instance.pack_forget()

        view = views[view_class]
        view.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        view.tkraise()
