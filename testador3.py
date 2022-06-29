from testador2 import run2
from testador import get_git
from datetime import *
from entrada import *


dia = date.today().strftime("%d/%m/%y")
hora = datetime.now().strftime("%H:%M:%S")
cf, cp = cf_auto()

print("% % % % % % % % % % % % % % % % % % %\n"
        "\n\\version \"2.22.2\" \n\\language \"portugues\" \n"
        "\n\\header {"
        f"\n    title = \"{dia}, {hora}\""
        f"\n    subtitle = \"Contrapontos de primeira espécie gerados por computador\""
        f"\n    composer = \"Versão git: {get_git()}\""
        "\n}"
    )

for i in range(5):
    run2(cf, cp)