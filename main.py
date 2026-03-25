import tkinter as tk
from tkinter import messagebox
import math
import platform
import os
import sys
import datetime
import json
import sqlite3

def resource_path(relative_path):   
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(__file__), relative_path)

APP_DIR      = os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")), "Survivalcalc")
SETTINGS_FILE = os.path.join(APP_DIR, "settings.json")
DB_FILE       = os.path.join(APP_DIR, "history.db")
os.makedirs(APP_DIR, exist_ok=True)

LANG = {
    "DE": {
        "menu":          "Menü",
        "info":          "Info",
        "calculator":    "Rechner",
        "shape":         "Formen",
        "area":          "Fläche",
        "volume":        "Volumen",
        "settings":      "Einstellungen",
        "exit":          "Beenden",
        "history":       "Verlauf",
        "appearance":    "Darstellung",
        "dark_mode":     "Dark Mode",
        "toggle":        "Wechseln",
        "on":            "Ein ✓",
        "off":           "Aus",
        "rounding":      "Rundung",
        "rounding_active":"Rundung aktiv",
        "decimal_places":"Nachkommastellen",
        "units":         "Einheiten",
        "default_unit":  "Standardeinheit",
        "language":      "Sprache",
        "delete_history":"Verlauf löschen",
        "reset_settings":"Einstellungen zurücksetzen",
        "confirm_del_h": "Verlauf wirklich löschen?",
        "confirm_reset": "Einstellungen wirklich zurücksetzen?",
        "yes":           "Ja",
        "no":            "Nein",
        "app_info":      "App",
        "support":       "Support",
        "system":        "System",
        "version":       "Version",
        "release":       "Release",
        "status":        "Status",
        "license":       "Lizenz",
        "installed":     "Installiert am",
        "website":       "Website",
        "email":         "E-Mail",
        "os":            "Betriebssystem",
        "os_version":    "Version",
        "arch":          "Architektur",
        "python":        "Python-Version",
        "error":         "Bitte eine gültige Zahl eingeben.",
        "area_square":   "Fläche – Quadrat",
        "area_rect":     "Fläche – Rechteck",
        "area_circle":   "Fläche – Kreis",
        "area_tri":      "Fläche – Dreieck",
        "area_trap":     "Fläche – Trapez",
        "area_cyl":      "Fläche – Zylinder",
        "area_sphere":   "Fläche – Kugel",
        "area_cone":     "Fläche – Kegel",
        "vol_cube":      "Volumen – Würfel",
        "vol_rect":      "Volumen – Quader",
        "vol_cyl":       "Volumen – Zylinder",
        "vol_cone":      "Volumen – Kegel",
        "vol_sphere":    "Volumen – Kugel",
        "vol_tetra":     "Volumen – Tetraeder",
        "vol_trap":      "Volumen – Trapezprisma",
        "side":          "Seite",
        "radius":        "Radius r:",
        "diameter":      "Durchmesser d:",
        "height":        "Höhe h:",
        "width":         "Breite w:",
        "length":        "Länge l:",
        "base":          "Grundlinie g:",
        "slant":         "Mantellinie l:",
        "depth":         "Tiefe i:",
        "with_radius":   "Mit Radius",
        "with_diameter": "Mit Durchmesser",
        "result_area":   "A",
        "result_vol":    "V",
        "cube":          "Würfel",
        "rect_prism":    "Quader",
        "cylinder":      "Zylinder",
        "cone":          "Kegel",
        "sphere":        "Kugel",
        "tetrahedron":   "Tetraeder",
        "trap_prism":    "Trapezprisma",
        "square":        "Quadrat",
        "rectangle":     "Rechteck",
        "circle":        "Kreis",
        "triangle":      "Dreieck",
        "trapezoid":     "Trapez",
    },
    "EN": {
        "menu":          "Menu",
        "info":          "Info",
        "calculator":    "Calculator",
        "shape":         "Shapes",
        "area":          "Area",
        "volume":        "Volume",
        "settings":      "Settings",
        "exit":          "Exit",
        "history":       "History",
        "appearance":    "Appearance",
        "dark_mode":     "Dark Mode",
        "toggle":        "Toggle",
        "on":            "On ✓",
        "off":           "Off",
        "rounding":      "Rounding",
        "rounding_active":"Rounding active",
        "decimal_places":"Decimal places",
        "units":         "Units",
        "default_unit":  "Default unit",
        "language":      "Language",
        "delete_history":"Delete history",
        "reset_settings":"Reset settings",
        "confirm_del_h": "Really delete history?",
        "confirm_reset": "Really reset settings?",
        "yes":           "Yes",
        "no":            "No",
        "app_info":      "App",
        "support":       "Support",
        "system":        "System",
        "version":       "Version",
        "release":       "Release",
        "status":        "Status",
        "license":       "License",
        "installed":     "Installed on",
        "website":       "Website",
        "email":         "E-Mail",
        "os":            "Operating system",
        "os_version":    "Version",
        "arch":          "Architecture",
        "python":        "Python version",
        "error":         "Please enter a valid number.",
        "area_square":   "Area – Square",
        "area_rect":     "Area – Rectangle",
        "area_circle":   "Area – Circle",
        "area_tri":      "Area – Triangle",
        "area_trap":     "Area – Trapezoid",
        "area_cyl":      "Area – Cylinder",
        "area_sphere":   "Area – Sphere",
        "area_cone":     "Area – Cone",
        "vol_cube":      "Volume – Cube",
        "vol_rect":      "Volume – Rectangular prism",
        "vol_cyl":       "Volume – Cylinder",
        "vol_cone":      "Volume – Cone",
        "vol_sphere":    "Volume – Sphere",
        "vol_tetra":     "Volume – Tetrahedron",
        "vol_trap":      "Volume – Trapezoidal prism",
        "side":          "Side",
        "radius":        "Radius r:",
        "diameter":      "Diameter d:",
        "height":        "Height h:",
        "width":         "Width w:",
        "length":        "Length l:",
        "base":          "Base g:",
        "slant":         "Slant l:",
        "depth":         "Depth i:",
        "with_radius":   "With radius",
        "with_diameter": "With diameter",
        "result_area":   "A",
        "result_vol":    "V",
        "cube":          "Cube",
        "rect_prism":    "Rect. prism",
        "cylinder":      "Cylinder",
        "cone":          "Cone",
        "sphere":        "Sphere",
        "tetrahedron":   "Tetrahedron",
        "trap_prism":    "Trapezoidal prism",
        "square":        "Square",
        "rectangle":     "Rectangle",
        "circle":        "Circle",
        "triangle":      "Triangle",
        "trapezoid":     "Trapezoid",
    }
}

def t(key):
    return LANG[language].get(key, key)

app_version  = "1.0.0"
app_release  = "24.3.2026"
app_status   = "Stable"
dev_e_mail   = "team@survivalful.de"
dev_website  = "https://Survivalful.de/"
app_license  = "MIT License © 2026 Survivalful"
sys_system   = platform.system()
sys_version  = platform.release()
sys_machine  = platform.machine()
sys_python   = platform.python_version()
install_date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

DEFAULT_SETTINGS = {
    "bg_dark":      True,
    "round_num":    2,
    "round_en":     True,
    "default_unit": "m",
    "language":     "EN",
}

def load_settings():
    global bg_dark, round_num, round_en, default_unit, language, bg, fg
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            s = json.load(f)
    else:
        s = DEFAULT_SETTINGS.copy()
    bg_dark      = s.get("bg_dark",      DEFAULT_SETTINGS["bg_dark"])
    round_num    = s.get("round_num",    DEFAULT_SETTINGS["round_num"])
    round_en     = s.get("round_en",     DEFAULT_SETTINGS["round_en"])
    default_unit = s.get("default_unit", DEFAULT_SETTINGS["default_unit"])
    language     = s.get("language",     DEFAULT_SETTINGS["language"])
    bg = 'black' if bg_dark else 'white'
    fg = 'white' if bg_dark else 'black'

def save_settings():
    with open(SETTINGS_FILE, "w") as f:
        json.dump({
            "bg_dark":      bg_dark,
            "round_num":    round_num,
            "round_en":     round_en,
            "default_unit": default_unit,
            "language":     language,
        }, f, indent=2)

def init_db():
    con = sqlite3.connect(DB_FILE)
    con.execute("""CREATE TABLE IF NOT EXISTS history (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        expr      TEXT,
        result    TEXT,
        timestamp TEXT
    )""")
    con.commit()
    con.close()

def db_add(expr, result):
    con = sqlite3.connect(DB_FILE)
    con.execute("INSERT INTO history (expr, result, timestamp) VALUES (?,?,?)",
                (expr, str(result), datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")))
    con.commit()
    con.close()

def db_get_last(n=3):
    con = sqlite3.connect(DB_FILE)
    rows = con.execute(
        "SELECT expr, result FROM history ORDER BY id DESC LIMIT ?", (n,)
    ).fetchall()
    con.close()
    return rows

def db_clear():
    con = sqlite3.connect(DB_FILE)
    con.execute("DELETE FROM history")
    con.commit()
    con.close()

load_settings()
init_db()

UNIT_FACTORS = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0}
UNITS = list(UNIT_FACTORS.keys())

def half(first, last):
    return first / last

def make_section(parent, title, row):
    parent.rowconfigure(row, weight=0)
    f = tk.Frame(parent, bg=bg)
    f.grid(row=row, column=0, columnspan=3, sticky="ew", padx=12, pady=(16, 4))
    tk.Label(f, text=title, bg=bg, fg="#7c5cbf",
             font=("Arial", 10, "bold"), anchor="w").pack(side="left")
    tk.Frame(f, bg="#333333" if bg_dark else "#cccccc",
             height=1).pack(side="left", fill="x", expand=True, padx=(8, 0))

def make_input_row(parent, label_text, var, row, unit_var=None):
    parent.rowconfigure(row, weight=0)
    parent.rowconfigure(row + 1, weight=0)
    tk.Label(parent, text=label_text, bg=bg, fg=fg,
             font=("Arial", 11), anchor="w").grid(
        row=row, column=0, sticky="nw", padx=16, pady=(8, 0))
    row_frame = tk.Frame(parent, bg=bg)
    row_frame.grid(row=row+1, column=0, sticky="ew", padx=16, pady=(2, 4))
    row_frame.columnconfigure(0, weight=1)
    entry = tk.Entry(row_frame, textvariable=var,
                     bg="#2c2c2e" if bg_dark else "#f0f0f0",
                     fg=fg, insertbackground=fg,
                     font=("Arial", 14), relief="flat", bd=0,
                     highlightthickness=1,
                     highlightbackground="#444" if bg_dark else "#ccc",
                     highlightcolor="#7c5cbf")
    entry.grid(row=0, column=0, sticky="ew", ipady=6)
    if unit_var is not None:
        um = tk.OptionMenu(row_frame, unit_var, *UNITS)
        um.config(bg="#2c2c2e" if bg_dark else "#f0f0f0", fg=fg,
                  activebackground="#3a3a3c", activeforeground=fg,
                  relief="flat", highlightthickness=0,
                  font=("Arial", 11), width=3)
        um["menu"].config(bg="#2c2c2e" if bg_dark else "#f0f0f0", fg=fg)
        um.grid(row=0, column=1, padx=(4, 0), ipady=3)
    return entry

def make_result_label(parent, row):
    parent.rowconfigure(row, weight=0)
    r = tk.Label(parent, text="", bg=bg,
                 fg="#bf9fff" if bg_dark else "#7c5cbf",
                 font=("Arial", 16, "bold"), anchor="w")
    r.grid(row=row, column=0, sticky="nw", padx=16, pady=(4, 12))
    return r

def make_title_label(parent, text, symbol, row):
    parent.rowconfigure(row, weight=0)
    frame = tk.Frame(parent, bg=bg)
    frame.grid(row=row, column=0, sticky="nw", padx=16, pady=(12, 2))
    tk.Label(frame, text=text, bg=bg, fg=fg,
             font=("Arial", 13, "bold"), anchor="w").pack(side="left")
    tk.Label(frame, text=f"  {symbol}", bg=bg,
             fg="#888888" if bg_dark else "#aaaaaa",
             font=("Arial", 11), anchor="w").pack(side="left")
    return frame

def get_m(var, unit_var):
    return float(var.get()) * UNIT_FACTORS[unit_var.get()]

def format_result(val, unit_var):
    return val / (UNIT_FACTORS[unit_var.get()] ** 2)

def format_vol(val, unit_var):
    return val / (UNIT_FACTORS[unit_var.get()] ** 3)

def clear_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()
    for i in range(20):
        content_frame.rowconfigure(i, weight=0)
    content_frame.columnconfigure(0, weight=1)

def make_scroll_frame(parent):
    canvas = tk.Canvas(parent, bg=bg, highlightthickness=0)
    scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    inner = tk.Frame(canvas, bg=bg)
    inner.bind("<Configure>",
               lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=inner, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind_all("<MouseWheel>", on_mousewheel)
    return inner

def rebuild_menu():
    menubar.delete(0, "end")
    menu.delete(0, "end")
    shape_area.delete(0, "end")
    shape_volume.delete(0, "end")
    shape.delete(0, "end")
    areacircle.delete(0, "end")
    areacylinder.delete(0, "end")
    areasphere.delete(0, "end")
    areacone.delete(0, "end")
    volumeclinder.delete(0, "end")
    volumecone.delete(0, "end")
    volumesphere.delete(0, "end")
    areacircle.add_command(label=t("with_radius"),   command=area_circle_radius)
    areacircle.add_command(label=t("with_diameter"), command=area_circle_diameter)
    areacylinder.add_command(label=t("with_radius"),   command=area_cylinder_radius)
    areacylinder.add_command(label=t("with_diameter"), command=area_cylinder_diameter)
    areasphere.add_command(label=t("with_radius"),   command=area_sphere_radius)
    areasphere.add_command(label=t("with_diameter"), command=area_sphere_diameter)
    areacone.add_command(label=t("with_radius"),   command=area_cone_radius)
    areacone.add_command(label=t("with_diameter"), command=area_cone_diameter)
    volumeclinder.add_command(label=t("with_radius"),   command=volume_cylinder_radius)
    volumeclinder.add_command(label=t("with_diameter"), command=volume_cylinder_diameter)
    volumecone.add_command(label=t("with_radius"),   command=volume_cone_radius)
    volumecone.add_command(label=t("with_diameter"), command=volume_cone_diameter)
    volumesphere.add_command(label=t("with_radius"),   command=volume_sphere_radius)
    volumesphere.add_command(label=t("with_diameter"), command=volume_sphere_diameter)
    shape_area.add_command(label=t("square"),    command=area_square)
    shape_area.add_command(label=t("rectangle"), command=area_rectangle)
    shape_area.add_cascade(label=t("circle"),    menu=areacircle)
    shape_area.add_command(label=t("triangle"),  command=area_triangle)
    shape_area.add_command(label=t("trapezoid"), command=area_trapezoid)
    shape_area.add_cascade(label=t("cylinder"),  menu=areacylinder)
    shape_area.add_cascade(label=t("sphere"),    menu=areasphere)
    shape_area.add_cascade(label=t("cone"),      menu=areacone)
    shape_volume.add_command(label=t("cube"),        command=volume_cube)
    shape_volume.add_command(label=t("rect_prism"),  command=volume_rectangular_prism)
    shape_volume.add_cascade(label=t("cylinder"),    menu=volumeclinder)
    shape_volume.add_cascade(label=t("cone"),        menu=volumecone)
    shape_volume.add_cascade(label=t("sphere"),      menu=volumesphere)
    shape_volume.add_command(label=t("tetrahedron"), command=volume_tetrahedron)
    shape_volume.add_command(label=t("trap_prism"),  command=volume_trapezoidal_prism)
    shape.add_cascade(label=t("area"),   menu=shape_area)
    shape.add_cascade(label=t("volume"), menu=shape_volume)
    menu.add_command(label=t("info"),       command=info)
    menu.add_command(label=t("calculator"), command=calculator)
    menu.add_cascade(label=t("shape"),      menu=shape)
    menu.add_command(label=t("settings"),   command=settings)
    menu.add_command(label=t("exit"),       command=do_exit)
    menubar.add_cascade(label=t("menu"),    menu=menu)

def info():
    clear_frame()
    content_frame.rowconfigure(0, weight=1)
    content_frame.columnconfigure(0, weight=1)
    inner = make_scroll_frame(content_frame)
    inner.columnconfigure(0, weight=1)
    def info_row(parent, label, value, r):
        tk.Label(parent, text=label,
                 bg="#1e1e1e" if bg_dark else "#f5f5f5",
                 fg="#888888" if bg_dark else "#777777",
                 font=("Arial", 10), anchor="w").grid(
            row=r, column=0, sticky="w", padx=14, pady=(5, 0))
        tk.Label(parent, text=value,
                 bg="#1e1e1e" if bg_dark else "#f5f5f5",
                 fg=fg, font=("Arial", 11), anchor="w").grid(
            row=r+1, column=0, sticky="w", padx=14, pady=(0, 5))
    def card(title, items, row):
        inner.rowconfigure(row, weight=0)
        outer = tk.Frame(inner, bg="#7c5cbf")
        outer.grid(row=row, column=0, sticky="ew", padx=16, pady=(10, 0))
        outer.columnconfigure(0, weight=1)
        tk.Label(outer, text=title, bg="#7c5cbf", fg="#ece8ff",
                 font=("Arial", 11, "bold"), anchor="w",
                 padx=10, pady=6).grid(row=0, column=0, sticky="w")
        body = tk.Frame(outer, bg="#1e1e1e" if bg_dark else "#f5f5f5")
        body.grid(row=1, column=0, sticky="ew", padx=1, pady=(0, 1))
        body.columnconfigure(0, weight=1)
        for i, (lbl, val) in enumerate(items):
            info_row(body, lbl, val, i*2)
    card(t("app_info"), [
        (t("version"),   app_version),
        (t("release"),   app_release),
        (t("status"),    app_status),
        (t("license"),   app_license),
        (t("installed"), install_date),
        ("App-Ordner",   APP_DIR),
    ], 0)
    card(t("support"), [
        (t("website"), dev_website),
        (t("email"),   dev_e_mail),
    ], 1)
    card(t("system"), [
        (t("os"),         sys_system),
        (t("os_version"), sys_version),
        (t("arch"),       sys_machine),
        (t("python"),     sys_python),
    ], 2)

def do_exit():
    root.quit()

def settings():
    clear_frame()
    content_frame.rowconfigure(0, weight=1)
    content_frame.columnconfigure(0, weight=1)
    inner = make_scroll_frame(content_frame)
    inner.columnconfigure(0, weight=1)
    inner.columnconfigure(1, weight=1)
    inner.columnconfigure(2, weight=0)
    make_section(inner, t("appearance"), 0)
    def bg_toggle():
        global bg_dark, bg, fg
        bg_dark = not bg_dark
        bg = 'black' if bg_dark else 'white'
        fg = 'white' if bg_dark else 'black'
        root.config(bg=bg)
        content_frame.config(bg=bg)
        creator.config(bg=bg, fg=fg)
        save_settings()
        settings()
    inner.rowconfigure(1, weight=0)
    tk.Label(inner, text=t("dark_mode"), bg=bg, fg=fg,
             font=("Arial", 11), anchor="w").grid(
        row=1, column=0, sticky="w", padx=16, pady=8)
    tk.Label(inner, text=t("on") if bg_dark else t("off"),
             bg=bg, fg="#bf9fff" if bg_dark else "#7c5cbf",
             font=("Arial", 11)).grid(row=1, column=1, sticky="w")
    tk.Button(inner, text=t("toggle"), command=bg_toggle,
              bg="#2c2c2e" if bg_dark else "#eeeeee", fg=fg,
              relief="flat", padx=10, pady=4, cursor="hand2").grid(
        row=1, column=2, padx=16, pady=8, sticky="e")
    make_section(inner, t("rounding"), 2)
    def round_toggle():
        global round_en
        round_en = not round_en
        round_lbl.config(text=t("on") if round_en else t("off"),
                         fg="#bf9fff" if round_en else "#888888")
        save_settings()
    inner.rowconfigure(3, weight=0)
    tk.Label(inner, text=t("rounding_active"), bg=bg, fg=fg,
             font=("Arial", 11), anchor="w").grid(
        row=3, column=0, sticky="w", padx=16, pady=8)
    round_lbl = tk.Label(inner,
                         text=t("on") if round_en else t("off"),
                         bg=bg,
                         fg="#bf9fff" if round_en else "#888888",
                         font=("Arial", 11))
    round_lbl.grid(row=3, column=1, sticky="w")
    tk.Button(inner, text=t("toggle"), command=round_toggle,
              bg="#2c2c2e" if bg_dark else "#eeeeee", fg=fg,
              relief="flat", padx=10, pady=4, cursor="hand2").grid(
        row=3, column=2, padx=16, pady=8, sticky="e")
    inner.rowconfigure(4, weight=0)
    inner.rowconfigure(5, weight=0)
    tk.Label(inner, text=t("decimal_places"), bg=bg, fg=fg,
             font=("Arial", 11), anchor="w").grid(
        row=4, column=0, sticky="w", padx=16, pady=(8, 0))
    slider_val = tk.Label(inner, text=str(round_num),
                          bg=bg, fg="#bf9fff" if bg_dark else "#7c5cbf",
                          font=("Arial", 11, "bold"))
    slider_val.grid(row=4, column=1, sticky="w")
    def on_slider(val):
        global round_num
        round_num = int(float(val))
        slider_val.config(text=str(round_num))
        save_settings()
    tk.Scale(inner, from_=0, to=20, orient="horizontal",
             command=on_slider,
             bg=bg, fg=fg,
             troughcolor="#2c2c2e" if bg_dark else "#dddddd",
             highlightthickness=0, showvalue=False,
             relief="flat", sliderrelief="flat",
             activebackground="#7c5cbf").grid(
        row=5, column=0, columnspan=3, sticky="ew", padx=16, pady=(0, 8))
    make_section(inner, t("units"), 6)
    inner.rowconfigure(7, weight=0)
    tk.Label(inner, text=t("default_unit"), bg=bg, fg=fg,
             font=("Arial", 11), anchor="w").grid(
        row=7, column=0, sticky="w", padx=16, pady=8)
    unit_var = tk.StringVar(value=default_unit)
    def on_unit(*args):
        global default_unit
        default_unit = unit_var.get()
        save_settings()
    unit_var.trace_add("write", on_unit)
    um = tk.OptionMenu(inner, unit_var, *UNITS)
    um.config(bg="#2c2c2e" if bg_dark else "#f0f0f0", fg=fg,
              activebackground="#3a3a3c", activeforeground=fg,
              relief="flat", highlightthickness=0,
              font=("Arial", 11), width=4)
    um["menu"].config(bg="#2c2c2e" if bg_dark else "#f0f0f0", fg=fg)
    um.grid(row=7, column=1, columnspan=2, sticky="w", padx=4, pady=8)
    make_section(inner, t("language"), 8)
    inner.rowconfigure(9, weight=0)
    tk.Label(inner, text=t("language"), bg=bg, fg=fg,
             font=("Arial", 11), anchor="w").grid(
        row=9, column=0, sticky="w", padx=16, pady=8)
    lang_var = tk.StringVar(value=language)
    def on_lang(*args):
        global language
        language = lang_var.get()
        save_settings()
        rebuild_menu()
        settings()
    lang_var.trace_add("write", on_lang)
    for i, lang in enumerate(["DE", "EN"]):
        tk.Radiobutton(inner, text=lang, variable=lang_var, value=lang,
                       bg=bg, fg=fg,
                       selectcolor="#2c2c2e" if bg_dark else "#dddddd",
                       activebackground=bg, activeforeground=fg,
                       font=("Arial", 11)).grid(
            row=9, column=1+i, sticky="w",
            padx=(4 if i == 0 else 0, 0), pady=8)
    make_section(inner, "Datenverwaltung" if language == "DE" else "Data management", 10)
    def del_history():
        if messagebox.askyesno(t("delete_history"), t("confirm_del_h")):
            db_clear()
    def reset_s():
        if messagebox.askyesno(t("reset_settings"), t("confirm_reset")):
            global bg_dark, round_num, round_en, default_unit, language, bg, fg
            bg_dark      = DEFAULT_SETTINGS["bg_dark"]
            round_num    = DEFAULT_SETTINGS["round_num"]
            round_en     = DEFAULT_SETTINGS["round_en"]
            default_unit = DEFAULT_SETTINGS["default_unit"]
            language     = DEFAULT_SETTINGS["language"]
            bg = 'black' if bg_dark else 'white'
            fg = 'white' if bg_dark else 'black'
            save_settings()
            root.config(bg=bg)
            content_frame.config(bg=bg)
            creator.config(bg=bg, fg=fg)
            rebuild_menu()
            settings()
    inner.rowconfigure(11, weight=0)
    inner.rowconfigure(12, weight=0)
    tk.Button(inner, text=t("delete_history"), command=del_history,
              bg="#3a1a1a", fg="#ff8080",
              relief="flat", padx=10, pady=6, cursor="hand2",
              font=("Arial", 11)).grid(
        row=11, column=0, columnspan=3, sticky="ew", padx=16, pady=(8, 4))
    tk.Button(inner, text=t("reset_settings"), command=reset_s,
              bg="#2a1a3a", fg="#bf9fff",
              relief="flat", padx=10, pady=6, cursor="hand2",
              font=("Arial", 11)).grid(
        row=12, column=0, columnspan=3, sticky="ew", padx=16, pady=(0, 16))

def area_square():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var, unit_var = tk.StringVar(), tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            v = get_m(var, unit_var); s = format_result(v**2, unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_area')} = {s} {unit_var.get()}²")
        except: result.config(text="")
    var.trace_add("write", calc); unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("area_square"), "A = a²", 0)
    make_input_row(content_frame, f"{t('side')} a:", var, 1, unit_var)
    result = make_result_label(content_frame, 3)

def area_rectangle():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_a, var_b = tk.StringVar(), tk.StringVar()
    unit_var = tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            s = format_result(get_m(var_a, unit_var) * get_m(var_b, unit_var), unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_area')} = {s} {unit_var.get()}²")
        except: result.config(text="")
    var_a.trace_add("write", calc); var_b.trace_add("write", calc)
    unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("area_rect"), "A = a · b", 0)
    make_input_row(content_frame, f"{t('side')} a:", var_a, 1, unit_var)
    make_input_row(content_frame, f"{t('side')} b:", var_b, 3)
    result = make_result_label(content_frame, 5)

def area_circle_radius():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_r, unit_var = tk.StringVar(), tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            r = get_m(var_r, unit_var); s = format_result(math.pi * r**2, unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_area')} = {s} {unit_var.get()}²")
        except: result.config(text="")
    var_r.trace_add("write", calc); unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("area_circle"), "A = π · r²", 0)
    make_input_row(content_frame, t("radius"), var_r, 1, unit_var)
    result = make_result_label(content_frame, 3)

def area_circle_diameter():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_d, unit_var = tk.StringVar(), tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            r = get_m(var_d, unit_var)/2; s = format_result(math.pi * r**2, unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_area')} = {s} {unit_var.get()}²")
        except: result.config(text="")
    var_d.trace_add("write", calc); unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("area_circle"), "A = π · (d/2)²", 0)
    make_input_row(content_frame, t("diameter"), var_d, 1, unit_var)
    result = make_result_label(content_frame, 3)

def area_triangle():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_g, var_h = tk.StringVar(), tk.StringVar()
    unit_var = tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            s = format_result(0.5 * get_m(var_g, unit_var) * get_m(var_h, unit_var), unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_area')} = {s} {unit_var.get()}²")
        except: result.config(text="")
    var_g.trace_add("write", calc); var_h.trace_add("write", calc)
    unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("area_tri"), "A = g · h / 2", 0)
    make_input_row(content_frame, t("base"), var_g, 1, unit_var)
    make_input_row(content_frame, t("height"), var_h, 3)
    result = make_result_label(content_frame, 5)

def area_trapezoid():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_a, var_b, var_h = tk.StringVar(), tk.StringVar(), tk.StringVar()
    unit_var = tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            s = format_result(((get_m(var_a,unit_var)+get_m(var_b,unit_var))/2)*get_m(var_h,unit_var), unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_area')} = {s} {unit_var.get()}²")
        except: result.config(text="")
    var_a.trace_add("write", calc); var_b.trace_add("write", calc)
    var_h.trace_add("write", calc); unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("area_trap"), "A = (a+b)/2 · h", 0)
    make_input_row(content_frame, f"{t('side')} a:", var_a, 1, unit_var)
    make_input_row(content_frame, f"{t('side')} b:", var_b, 3)
    make_input_row(content_frame, t("height"), var_h, 5)
    result = make_result_label(content_frame, 7)

def area_cylinder_radius():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_r, var_h = tk.StringVar(), tk.StringVar()
    unit_var = tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            r, h = get_m(var_r,unit_var), get_m(var_h,unit_var)
            s = format_result(2*math.pi*r*h + 2*math.pi*r**2, unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_area')} = {s} {unit_var.get()}²")
        except: result.config(text="")
    var_r.trace_add("write", calc); var_h.trace_add("write", calc)
    unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("area_cyl"), "A = 2πr(r+h)", 0)
    make_input_row(content_frame, t("radius"), var_r, 1, unit_var)
    make_input_row(content_frame, t("height"), var_h, 3)
    result = make_result_label(content_frame, 5)

def area_cylinder_diameter():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_d, var_h = tk.StringVar(), tk.StringVar()
    unit_var = tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            r, h = get_m(var_d,unit_var)/2, get_m(var_h,unit_var)
            s = format_result(2*math.pi*r*h + 2*math.pi*r**2, unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_area')} = {s} {unit_var.get()}²")
        except: result.config(text="")
    var_d.trace_add("write", calc); var_h.trace_add("write", calc)
    unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("area_cyl"), "A = 2πr(r+h)", 0)
    make_input_row(content_frame, t("diameter"), var_d, 1, unit_var)
    make_input_row(content_frame, t("height"), var_h, 3)
    result = make_result_label(content_frame, 5)

def area_sphere_radius():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_r, unit_var = tk.StringVar(), tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            s = format_result(4*math.pi*get_m(var_r,unit_var)**2, unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_area')} = {s} {unit_var.get()}²")
        except: result.config(text="")
    var_r.trace_add("write", calc); unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("area_sphere"), "A = 4πr²", 0)
    make_input_row(content_frame, t("radius"), var_r, 1, unit_var)
    result = make_result_label(content_frame, 3)

def area_sphere_diameter():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_d, unit_var = tk.StringVar(), tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            s = format_result(4*math.pi*(get_m(var_d,unit_var)/2)**2, unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_area')} = {s} {unit_var.get()}²")
        except: result.config(text="")
    var_d.trace_add("write", calc); unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("area_sphere"), "A = 4π(d/2)²", 0)
    make_input_row(content_frame, t("diameter"), var_d, 1, unit_var)
    result = make_result_label(content_frame, 3)

def area_cone_radius():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_r, var_l = tk.StringVar(), tk.StringVar()
    unit_var = tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            r, l = get_m(var_r,unit_var), get_m(var_l,unit_var)
            s = format_result(math.pi*r*(r+l), unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_area')} = {s} {unit_var.get()}²")
        except: result.config(text="")
    var_r.trace_add("write", calc); var_l.trace_add("write", calc)
    unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("area_cone"), "A = πr(r+l)", 0)
    make_input_row(content_frame, t("radius"), var_r, 1, unit_var)
    make_input_row(content_frame, t("slant"), var_l, 3)
    result = make_result_label(content_frame, 5)

def area_cone_diameter():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_d, var_l = tk.StringVar(), tk.StringVar()
    unit_var = tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            r, l = get_m(var_d,unit_var)/2, get_m(var_l,unit_var)
            s = format_result(math.pi*r*(r+l), unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_area')} = {s} {unit_var.get()}²")
        except: result.config(text="")
    var_d.trace_add("write", calc); var_l.trace_add("write", calc)
    unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("area_cone"), "A = πr(r+l)", 0)
    make_input_row(content_frame, t("diameter"), var_d, 1, unit_var)
    make_input_row(content_frame, t("slant"), var_l, 3)
    result = make_result_label(content_frame, 5)

def volume_cube():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_a, unit_var = tk.StringVar(), tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            s = format_vol(get_m(var_a,unit_var)**3, unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_vol')} = {s} {unit_var.get()}³")
        except: result.config(text="")
    var_a.trace_add("write", calc); unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("vol_cube"), "V = a³", 0)
    make_input_row(content_frame, f"{t('side')} a:", var_a, 1, unit_var)
    result = make_result_label(content_frame, 3)

def volume_rectangular_prism():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_l, var_w, var_h = tk.StringVar(), tk.StringVar(), tk.StringVar()
    unit_var = tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            s = format_vol(get_m(var_l,unit_var)*get_m(var_w,unit_var)*get_m(var_h,unit_var), unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_vol')} = {s} {unit_var.get()}³")
        except: result.config(text="")
    var_l.trace_add("write", calc); var_w.trace_add("write", calc)
    var_h.trace_add("write", calc); unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("vol_rect"), "V = l · w · h", 0)
    make_input_row(content_frame, t("length"), var_l, 1, unit_var)
    make_input_row(content_frame, t("width"), var_w, 3)
    make_input_row(content_frame, t("height"), var_h, 5)
    result = make_result_label(content_frame, 7)

def volume_cylinder_radius():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_r, var_h = tk.StringVar(), tk.StringVar()
    unit_var = tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            r, h = get_m(var_r,unit_var), get_m(var_h,unit_var)
            s = format_vol(math.pi*r**2*h, unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_vol')} = {s} {unit_var.get()}³")
        except: result.config(text="")
    var_r.trace_add("write", calc); var_h.trace_add("write", calc)
    unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("vol_cyl"), "V = π · r² · h", 0)
    make_input_row(content_frame, t("radius"), var_r, 1, unit_var)
    make_input_row(content_frame, t("height"), var_h, 3)
    result = make_result_label(content_frame, 5)

def volume_cylinder_diameter():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_d, var_h = tk.StringVar(), tk.StringVar()
    unit_var = tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            r, h = get_m(var_d,unit_var)/2, get_m(var_h,unit_var)
            s = format_vol(math.pi*r**2*h, unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_vol')} = {s} {unit_var.get()}³")
        except: result.config(text="")
    var_d.trace_add("write", calc); var_h.trace_add("write", calc)
    unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("vol_cyl"), "V = π · (d/2)² · h", 0)
    make_input_row(content_frame, t("diameter"), var_d, 1, unit_var)
    make_input_row(content_frame, t("height"), var_h, 3)
    result = make_result_label(content_frame, 5)

def volume_cone_radius():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_r, var_h = tk.StringVar(), tk.StringVar()
    unit_var = tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            r, h = get_m(var_r,unit_var), get_m(var_h,unit_var)
            s = format_vol((1/3)*math.pi*r**2*h, unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_vol')} = {s} {unit_var.get()}³")
        except: result.config(text="")
    var_r.trace_add("write", calc); var_h.trace_add("write", calc)
    unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("vol_cone"), "V = π·r²·h / 3", 0)
    make_input_row(content_frame, t("radius"), var_r, 1, unit_var)
    make_input_row(content_frame, t("height"), var_h, 3)
    result = make_result_label(content_frame, 5)

def volume_cone_diameter():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_d, var_h = tk.StringVar(), tk.StringVar()
    unit_var = tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            r, h = get_m(var_d,unit_var)/2, get_m(var_h,unit_var)
            s = format_vol((1/3)*math.pi*r**2*h, unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_vol')} = {s} {unit_var.get()}³")
        except: result.config(text="")
    var_d.trace_add("write", calc); var_h.trace_add("write", calc)
    unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("vol_cone"), "V = π·r²·h / 3", 0)
    make_input_row(content_frame, t("diameter"), var_d, 1, unit_var)
    make_input_row(content_frame, t("height"), var_h, 3)
    result = make_result_label(content_frame, 5)

def volume_sphere_radius():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_r, unit_var = tk.StringVar(), tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            s = format_vol((4/3)*math.pi*get_m(var_r,unit_var)**3, unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_vol')} = {s} {unit_var.get()}³")
        except: result.config(text="")
    var_r.trace_add("write", calc); unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("vol_sphere"), "V = 4/3 · π · r³", 0)
    make_input_row(content_frame, t("radius"), var_r, 1, unit_var)
    result = make_result_label(content_frame, 3)

def volume_sphere_diameter():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_d, unit_var = tk.StringVar(), tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            s = format_vol((4/3)*math.pi*(get_m(var_d,unit_var)/2)**3, unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_vol')} = {s} {unit_var.get()}³")
        except: result.config(text="")
    var_d.trace_add("write", calc); unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("vol_sphere"), "V = 4/3 · π · (d/2)³", 0)
    make_input_row(content_frame, t("diameter"), var_d, 1, unit_var)
    result = make_result_label(content_frame, 3)

def volume_tetrahedron():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_a, unit_var = tk.StringVar(), tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            s = format_vol(get_m(var_a,unit_var)**3 / (6*2**0.5), unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_vol')} = {s} {unit_var.get()}³")
        except: result.config(text="")
    var_a.trace_add("write", calc); unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("vol_tetra"), "V = a³ / (6√2)", 0)
    make_input_row(content_frame, f"{t('side')} a:", var_a, 1, unit_var)
    result = make_result_label(content_frame, 3)

def volume_trapezoidal_prism():
    clear_frame(); content_frame.columnconfigure(0, weight=1)
    var_b, var_B, var_h, var_i = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
    unit_var = tk.StringVar(value=default_unit)
    def calc(*a):
        try:
            b=get_m(var_b,unit_var); B=get_m(var_B,unit_var)
            h=get_m(var_h,unit_var); i=get_m(var_i,unit_var)
            s = format_vol(((b+B)/2)*h*i, unit_var)
            if round_en: s = round(s, round_num)
            result.config(text=f"{t('result_vol')} = {s} {unit_var.get()}³")
        except: result.config(text="")
    for v in (var_b, var_B, var_h, var_i): v.trace_add("write", calc)
    unit_var.trace_add("write", calc)
    make_title_label(content_frame, t("vol_trap"), "V = (b+B)/2 · h · i", 0)
    make_input_row(content_frame, f"{t('side')} b:", var_b, 1, unit_var)
    make_input_row(content_frame, f"{t('side')} B:", var_B, 3)
    make_input_row(content_frame, t("height"), var_h, 5)
    make_input_row(content_frame, t("depth"), var_i, 7)
    result = make_result_label(content_frame, 9)

def calculator():
    clear_frame()
    display_var = tk.StringVar(value="0")
    expr_var    = tk.StringVar(value="")

    def button_click(z):
        c = display_var.get()
        display_var.set(str(z) if c in ("0", "Fehler", "Error") else c + str(z))

    def clear():
        display_var.set("0"); expr_var.set("")

    def backspace():
        c = display_var.get()
        display_var.set(c[:-1] if len(c) > 1 and c not in ("Fehler","Error") else "0")

    def toggle_sign():
        c = display_var.get()
        try:
            v = float(c)
            display_var.set(("-"+c) if v > 0 else (c[1:] if v < 0 else c))
        except: pass

    def percent():
        try:
            v = float(display_var.get()) / 100
            display_var.set(str(round(v, round_num) if round_en else v))
        except: pass

    def ausrechnen(event=None):
        try:
            ausdruck = display_var.get()
            expr_var.set(ausdruck + " =")
            ergebnis = eval(ausdruck)
            if round_en: ergebnis = round(ergebnis, round_num)
            display_var.set(str(ergebnis))
            db_add(ausdruck, ergebnis)
            update_history()
        except:
            expr_var.set(""); display_var.set("Fehler" if language=="DE" else "Error")

    def tastatur_input(event):
        if event.char in "0123456789+-*/.": button_click(event.char)
        elif event.keysym == "Return":      ausrechnen()
        elif event.keysym in ("Escape","c","C"): clear()
        elif event.keysym == "BackSpace":   backspace()

    content_frame.bind_all("<Key>", tastatur_input)

    wrapper = tk.Frame(content_frame, bg="#1c1c1e")
    wrapper.grid(row=0, column=0, sticky="nsew")
    content_frame.rowconfigure(0, weight=1)
    content_frame.columnconfigure(0, weight=1)
    wrapper.columnconfigure(0, weight=1)
    wrapper.rowconfigure(1, weight=1)

    display_frame = tk.Frame(wrapper, bg="#2c2c2e")
    display_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 6))
    tk.Label(display_frame, textvariable=expr_var,
             font=("Arial", 12), bg="#2c2c2e", fg="#888888",
             anchor="e", padx=12, pady=6).pack(fill="x", pady=(6, 0))
    tk.Label(display_frame, textvariable=display_var,
             font=("Arial", 34, "bold"), bg="#2c2c2e", fg="white",
             anchor="e", padx=12, pady=0).pack(fill="x", pady=(0, 10))

    STYLE = {
        "num": {"bg": "#2c2c2e", "fg": "white",   "abg": "#3a3a3c"},
        "op":  {"bg": "#3a3a3c", "fg": "#bf9fff", "abg": "#48484a"},
        "fn":  {"bg": "#3a3a3c", "fg": "#aaaaaa", "abg": "#48484a"},
        "eq":  {"bg": "#7c5cbf", "fg": "#ece8ff", "abg": "#5e42a0"},
    }
    grid = tk.Frame(wrapper, bg="#1c1c1e")
    grid.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 6))
    for c in range(4): grid.columnconfigure(c, weight=1)
    for r in range(5): grid.rowconfigure(r, weight=1)

    def make_btn(text, kind, cmd, row, col, colspan=1):
        s = STYLE[kind]
        tk.Button(grid, text=text, command=cmd,
                  bg=s["bg"], fg=s["fg"],
                  activebackground=s["abg"], activeforeground=s["fg"],
                  font=("Arial", 18), relief="flat", bd=0,
                  padx=0, pady=14, cursor="hand2").grid(
            row=row, column=col, columnspan=colspan,
            padx=4, pady=4, sticky="nsew")

    make_btn("AC",  "fn", clear,                        0, 0)
    make_btn("+/-", "fn", toggle_sign,                  0, 1)
    make_btn("%",   "fn", percent,                      0, 2)
    make_btn("÷",   "op", lambda: button_click("/"),    0, 3)
    make_btn("7",   "num", lambda: button_click("7"),   1, 0)
    make_btn("8",   "num", lambda: button_click("8"),   1, 1)
    make_btn("9",   "num", lambda: button_click("9"),   1, 2)
    make_btn("×",   "op",  lambda: button_click("*"),   1, 3)
    make_btn("4",   "num", lambda: button_click("4"),   2, 0)
    make_btn("5",   "num", lambda: button_click("5"),   2, 1)
    make_btn("6",   "num", lambda: button_click("6"),   2, 2)
    make_btn("−",   "op",  lambda: button_click("-"),   2, 3)
    make_btn("1",   "num", lambda: button_click("1"),   3, 0)
    make_btn("2",   "num", lambda: button_click("2"),   3, 1)
    make_btn("3",   "num", lambda: button_click("3"),   3, 2)
    make_btn("+",   "op",  lambda: button_click("+"),   3, 3)
    make_btn("⌫",   "fn",  backspace,                   4, 0)
    make_btn("0",   "num", lambda: button_click("0"),   4, 1)
    make_btn(".",   "num", lambda: button_click("."),   4, 2)
    make_btn("=",   "eq",  ausrechnen,                  4, 3)

    hist_frame = tk.Frame(wrapper, bg="#1c1c1e")
    hist_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=(0, 8))
    tk.Label(hist_frame, text=t("history"), bg="#1c1c1e", fg="#555555",
             font=("Arial", 10), anchor="w").pack(fill="x", padx=6)
    history_label = tk.Label(hist_frame, text="", bg="#1c1c1e",
                             fg="#666666", font=("Arial", 10),
                             anchor="e", justify="right")
    history_label.pack(fill="x", padx=6)

    def update_history():
        rows = db_get_last(3)
        lines = [f"{r[0]} = {r[1]}" for r in rows]
        history_label.config(text="\n".join(lines))

    update_history()

root = tk.Tk()
root.title("Calculator")
root.geometry("500x640")
root.resizable(False, False)
root.iconbitmap(default=resource_path("bilder/icon.ico"))

menubar       = tk.Menu(root)
menu          = tk.Menu(menubar, tearoff=0)
shape         = tk.Menu(menu, tearoff=0)
shape_volume  = tk.Menu(shape, tearoff=0)
shape_area    = tk.Menu(shape, tearoff=0)
areacircle    = tk.Menu(shape_area, tearoff=0)
areacylinder  = tk.Menu(shape_area, tearoff=0)
areasphere    = tk.Menu(shape_area, tearoff=0)
areacone      = tk.Menu(shape_area, tearoff=0)
volumeclinder = tk.Menu(shape_volume, tearoff=0)
volumecone    = tk.Menu(shape_volume, tearoff=0)
volumesphere  = tk.Menu(shape_volume, tearoff=0)

root.config(menu=menubar)

content_frame = tk.Frame(root)
content_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content_frame.columnconfigure(0, weight=1)
root.config(bg=bg)
content_frame.config(bg=bg)

creator = tk.Label(root, bg=bg, fg=fg)

rebuild_menu()
calculator()

root.mainloop()
