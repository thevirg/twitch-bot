class Theme:
    "Default dark theme"
    # Shared colors
    BG = '#3A393A'
    BAR_BG = '#1F1E1F'
    FG = '#FFFFFF'

    # Buttons
    BUTTON_BG = '#3A393A'
    BUTTON_FG = '#FFFFFF'

    # Slider
    SLIDER_ACTIVE_BG = '#3A393A'  # Mouse hover
    SLIDER_BG = '#1F1E1F'  # Shares color with button
    SLIDER_HL_BG = '#3A393A'  # Border
    SLIDER_SLIDE_BG = '#18181B'  # Throughcolor
    SLIDER_FG = '#FFFFFF'  # Text color

    # Console
    CONSOLE_BG = '#1F1E1F'
    CONSOLE_BG_ALT = '#2B2A2B'
    CONSOLE_TEXT = '#E5E5E5'

    # Log colors
    LOG_DEBUG = '#D6F0DA'
    LOG_INFO = '#F6F7F1'
    LOG_ERROR = '#E46C6D'
    LOG_WARNING = '#E49C6D'
    LOG_CRITICAL = '#E46C6D'

    # https://icon-icons.com/icon/volume-up-interface-symbol/73337 (28px)
    VOL_ICON = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAABmJLR0QAAAAAAAD5Q7t/AAAACXBIWXMAAA3XAAAN1wFCKJt4AAACfElEQVRIx+2WOWhUURSGv/cco+CCokcUkRkQxAUkqEQRsZAIYiwCRkGJjVvlUii44IIB9wWXwiIBrQyIRAuREBQ3CIQUg0UQTGEigssvEhEhJpqxOSPjmJl5M6OV3ua/nHO4/zv7g/8n4pE0U9JLSXclLcxlFxb5aELShBzq8cB0oAbolHROUkXJhJLWA93Ag+H0ZpYEqoA2IAD2AG2SxmbaBRHJ6oBmIAZ8MDMrYL8VuOr2T4BqMxuM5GEWWS6bdkk9krZICsysCVgHfAWWA2cihTQiWQBMAuJAE9AiabSZ3QF2udluSVV5CaOQee5SwBLgCpACaoFm/5BG4L6n7jRAICkBLMrKZxw4mYPslxx6CFN+rweuAyOA7WbWKGk+8MzN5wWS3gFTiuiOn4SSjgAHgQvAYTP7LukssBd4AyTMbEBSEqgEGsIiybJPDBgFHPCIADQAX4BpwCqX3XRcGpY5YI46WbowpprZZ+Cey5Y5djvOLovQzFJmdgroASqAxa564TjD8ZXj5PAvj9iU44DjUKzMgR0A+4GEN3mHq2Y5vnZM18nHcj08Bpzw+0UzeytpHLDaZU8dKx2fh8D7MggHgX7guLdHupDGeFu0uqzGsf1PN/4m4FpW488Buvz9uUEJo+23bSFpood3hz98G1jr6jagGnhoZivCPCV/C9gAfItQOB3ATidrATa619ucLAXsK7gtMkgHCwxvAb3AZqDOzPol1QKX3eySmXUWu4BvACNLWMCPgZWRF3CGp/Ue3t48RJWSWn0txYBHwJo0WWQPMx6MA31m9mkY3QLPZQwYAs4Dh8xsIHvaFzM7e/Oo+3yydPmqSv6bP8w/AJoKDZrJk8cHAAAAAElFTkSuQmCC'
    # https://icon-icons.com/icon/dog-pet-animal-japanese-shiba-inu-japan/127300 (96px)
    WM_ICON = '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luqJHhLnfZjDb/yi57ackchx5OjihyksUxvHJXedvCDmy9qqjrwMyC7dhH3K5nkSqY/lSEzYi/FcJ2MV5pAkF+5COFLJrLJc0HXzeRy8zMqtyTw3IAXg4o1njJpAvXletQIlo2K1asjLgORZ7yG54d1L0qsvrzFpJRMm8gcRI0sn4RxMVdzJSAD3oGDLzIJsRRFEs6nriDjz1wzbSy+YnH4SwpQ7G4/fkDvssBVRq6o6WAowQEK1YAWXZJZvtjIrXuNf5xljwjNKoXPU/1+Z53WHgGerPRmAeY1xJBwDZb2QWb4Z+6TzmGDUiL7ASg1Hs58bi6g8Su6yMyuA60AC1dwFhepxgUgLVpj06W8ks3IrEjTHrBKIOHlqLeQ7hz1MaTH6ykH0oxKJJVJnXj1h7F7D0k2JV37wZamz3+U3VP2Ywqq5cDWoS4GqiaJijlgQBAlESa+9EqdlHVaqF69+4Zre5RusI29O6BKzxZoxUdGjVZlFbjyCyAMSiW9NnfE2nNYzsdL9uHNPbfBiC94P1tPrkO4de/eBKVR4JVMTkBuBmwBbhLu2P7aD9plHaiegmBk6um8RK4TTsg77lAtx5666qGEgsTpH+3y29zpMcpVVbaUGYyVkksAdiGSwgjgt67GXvRov3gqoS0A+Dcxdu2wpGP/kZnKHL5YCX1SK86phPxRjwL4Jf4lfMVdkKfAe0Uod6Z9w+JRvhVuY79893pe+78TktPpZ2d6oVaQw5vKnLKVq5pnC3D/AXMvKhZOBa6qhD4ox4GfkV54nKUsmi7C7CrQ/rveSxu2CfwZ+mqN/hfm+nPltzc1gIqifIX/aTUbljx2VjWIMeBZTDvgPGCU67P88D9wGOGOJtwKieBrzJTX3YHZDr/+zH/iCCIeOJxt8JuwHrsHI8uf9cXVhDIM7GDOnBUuCDwBvw+iEA+PGfz9ws4CudPyq4OlrZ/8wogXLUnMx9vPoiu9CODD5tuDdj+xAW6BMeeGFHAvGDWNSCb0qBuDywheTQUxovB6z8DI+E+zxc/BFTATzFY5xTFS0U0G/ACdi/LOYxSxmMYtZzKIK+F+Ix06jqtbtCAAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxOS0xMC0yNVQxMTo0OToyMSswMTowME+rYI8AAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTktMTAtMjVUMTE6NDk6MjErMDE6MDA+9tgzAAAARnRFWHRzb2Z0d2FyZQBJbWFnZU1hZ2ljayA2LjcuOC05IDIwMTktMDItMDEgUTE2IGh0dHA6Ly93d3cuaW1hZ2VtYWdpY2sub3JnQXviyAAAABh0RVh0VGh1bWI6OkRvY3VtZW50OjpQYWdlcwAxp/+7LwAAABh0RVh0VGh1bWI6OkltYWdlOjpoZWlnaHQANTEywNBQUQAAABd0RVh0VGh1bWI6OkltYWdlOjpXaWR0aAA1MTIcfAPcAAAAGXRFWHRUaHVtYjo6TWltZXR5cGUAaW1hZ2UvcG5nP7JWTgAAABd0RVh0VGh1bWI6Ok1UaW1lADE1NzIwMDA1NjGBTg5tAAAAE3RFWHRUaHVtYjo6U2l6ZQAzMS4yS0JCZKfAvgAAAGN0RVh0VGh1bWI6OlVSSQBmaWxlOi8vLi91cGxvYWRzLzU2L2ZIaDNJaUsvMjA3OS9kb2dfcGV0X2FuaW1hbF9qYXBhbmVzZV9zaGliYV9pbnVfamFwYW5faWNvbl8xMjczMDAucG5nOLvfBAAAAABJRU5ErkJggg=='
    # https://icon-icons.com/icon/menu/71858
    # https://icon-icons.com/icon/cog/125323
    SETTINGS_ICON = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADdYAAA3WAZBveZwAAAAYdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjEuNv1OCegAAAD7SURBVEhLxdU9igJBEIZhFVZBg0VYZCNN9AaGJoqwgbGYbOYVPIF7As+gB/EQegN/EgVDEWR8S7FpnDKxt9oPHuj5kpoZpnsySZJEpZaW1NKSWlpSS0tqaemxaGKMjtflUUXtRSW4GW6BBo6QnNGCDFtKEZA95IZTAwfwM0L9tgxOH6mBX1hBcoA8cRZTbAPM8YnUQFFGD99e96/U0pJ/kcMEG8xQgPRdyJf796JfuDlugR/4GaKC0/UqLG28f2D0VxrFYxF1W8jGX0MSZeNHP9qeHd4LKQKyg3p4i/vvyX3G+EDI76kIN8MtYlFLS2ppSS0tqaUltbSTZC4ImONmwXngJQAAAABJRU5ErkJggg=='
