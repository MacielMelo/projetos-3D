# Configuração do VS Code para Modelagem 3D Paramétrica com Python

Guia completo para configurar o ambiente de desenvolvimento para criação de modelos 3D paramétricos em Python com visualização e exportação para impressão 3D.

## 📋 Índice

- [Instalação do Python](#instalação-do-python)
- [Configuração do VS Code](#configuração-do-vs-code)
- [Bibliotecas Python](#bibliotecas-python)
- [Fluxo de Trabalho](#fluxo-de-trabalho)
- [Exemplo Básico](#exemplo-básico)
- [Recursos e Documentação](#recursos-e-documentação)

## 🐍 Instalação do Python com pyenv

### 1. Instalar pyenv (se ainda não tiver)

**Linux/Mac:**
```bash
# Instalar pyenv
curl https://pyenv.run | bash

# Adicionar ao ~/.bashrc ou ~/.zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# Recarregar o shell
exec $SHELL
```

**Windows (PowerShell como Administrador):**
```powershell
# Instalar pyenv-win via PowerShell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"

# Ou via Git (se tiver Git instalado)
git clone https://github.com/pyenv-win/pyenv-win.git "$HOME\.pyenv"

# Adicionar ao PATH (executar no PowerShell)
[System.Environment]::SetEnvironmentVariable('PYENV','$HOME\.pyenv\pyenv-win\','User')
[System.Environment]::SetEnvironmentVariable('PYENV_ROOT','$HOME\.pyenv\pyenv-win\','User')
[System.Environment]::SetEnvironmentVariable('PYENV_HOME','$HOME\.pyenv\pyenv-win\','User')

# Adicionar ao PATH
[System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")

# Reiniciar o PowerShell
```

**Dependências necessárias:**

*Ubuntu/Debian:*
```bash
sudo apt update
sudo apt install -y build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

*Fedora/CentOS/RHEL:*
```bash
sudo dnf install -y gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite \
sqlite-devel openssl-devel tk-devel libffi-devel xz-devel
```

*macOS:*
```bash
brew install openssl readline sqlite3 xz zlib
```

*Windows:*
- Nenhuma dependência adicional necessária (pyenv-win usa instaladores oficiais do Python)

### 2. Instalar Python via pyenv

**Linux/Mac:**
```bash
# Listar versões disponíveis
pyenv install --list | grep " 3\."

# Instalar Python 3.12 (recomendado)
pyenv install 3.12.2

# Definir como versão global
pyenv global 3.12.2

# Verificar instalação
python --version
```

**Windows (PowerShell):**
```powershell
# Listar versões disponíveis
pyenv install --list

# Instalar Python 3.12 (recomendado)
pyenv install 3.12.2

# Definir como versão global
pyenv global 3.12.2

# Verificar instalação
python --version

# Se python não funcionar, use:
pyenv rehash
```

### 3. Criar ambiente virtual para o projeto

**Opção A: Usando pyenv-virtualenv (Linux/Mac)**

```bash
# Instalar plugin pyenv-virtualenv (se necessário)
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

# Criar ambiente virtual
pyenv virtualenv 3.12.2 cadquery-env

# Ativar automaticamente no diretório do projeto
cd /caminho/do/projeto
pyenv local cadquery-env

# O ambiente será ativado automaticamente ao entrar no diretório
```

**Opção B: Usando venv padrão (Recomendado para Windows)**

*Linux/Mac:*
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
source venv/bin/activate
```

*Windows (PowerShell):*
```powershell
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
.\venv\Scripts\Activate.ps1

# Se houver erro de política de execução, execute:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

*Windows (CMD):*
```cmd
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
venv\Scripts\activate.bat
```

## 🔧 Configuração do VS Code

### Extensões Necessárias

Instale as seguintes extensões no VS Code:

1. **Python** (Microsoft)
   - ID: `ms-python.python`
   - Para desenvolvimento Python

2. **OCP CAD Viewer** (Roipoussiere)
   - ID: `roipoussiere.cadquery-viewer`
   - Para visualização de modelos CadQuery diretamente no VS Code

3. **3D Viewer for VS Code** (Tatsuya Nakamori) ou **STL Viewer**
   - ID: `tatsy.vscode-3d-preview` ou similar
   - Para visualizar arquivos STL exportados

4. **Jupyter** (Microsoft) - Opcional
   - ID: `ms-toolsai.jupyter`
   - Se você preferir trabalhar com notebooks

### Instalação via Terminal

**Linux/Mac:**
```bash
code --install-extension ms-python.python
code --install-extension roipoussiere.cadquery-viewer
code --install-extension tatsy.vscode-3d-preview
```

**Windows (PowerShell ou CMD):**
```powershell
code --install-extension ms-python.python
code --install-extension roipoussiere.cadquery-viewer
code --install-extension tatsy.vscode-3d-preview
```

**Ou instale manualmente:**
1. Abra o VS Code
2. Pressione `Ctrl+Shift+X` (Windows/Linux) ou `Cmd+Shift+X` (Mac)
3. Busque e instale cada extensão

## 📦 Bibliotecas Python

### Instalação das Bibliotecas Principais

```bash
# CadQuery - Biblioteca principal para modelagem CAD paramétrica
pip install cadquery

# OCP (OpenCascade) - Motor CAD usado pelo CadQuery
pip install ocp

# Bibliotecas auxiliares
pip install numpy
pip install matplotlib  # Para visualizações 2D adicionais
```

### Instalação para Jupyter Notebook (Opcional)

Se você preferir trabalhar com notebooks:

```bash
pip install jupyter
pip install jupyter-cadquery
pip install cadquery-massembly
```

### Bibliotecas Alternativas/Complementares

```bash
# Trimesh - Para manipulação de meshes
pip install trimesh

# numpy-stl - Para trabalhar com arquivos STL
pip install numpy-stl

# SolidPython - Interface Python para OpenSCAD
pip install solidpython
```

## 🔄 Fluxo de Trabalho

### Opção 1: Script Python + OCP CAD Viewer (Recomendado)

1. Crie um arquivo `.py`
2. Desenvolva seu modelo usando CadQuery
3. Use `show_object()` para visualizar no VS Code
4. Execute o script
5. Visualize o modelo 3D no painel lateral
6. Exporte para STL quando satisfeito

### Opção 2: Jupyter Notebook

1. Crie um arquivo `.ipynb`
2. Desenvolva em células
3. Use `jupyter_cadquery.show()` para visualizar inline
4. Execute célula por célula
5. Exporte para STL

### Opção 3: Exportar e Visualizar STL

1. Desenvolva o modelo
2. Exporte para STL
3. Abra o arquivo STL com a extensão 3D Viewer
4. Itere conforme necessário

## 💡 Exemplo Básico

### Script Python com Visualização

```python
import cadquery as cq

# Parâmetros ajustáveis
altura = 50
largura = 30
espessura = 10
diametro_furo = 5

# Construção do modelo
resultado = (
    cq.Workplane("XY")
    .box(largura, altura, espessura)
    .faces(">Z")
    .workplane()
    .hole(diametro_furo)
    .edges("|Z")
    .fillet(2)
)

# Visualizar no VS Code (requer OCP CAD Viewer)
show_object(resultado)

# Exportar para STL
cq.exporters.export(resultado, "modelo.stl")
```

### Exemplo com Jupyter Notebook

```python
import cadquery as cq
from jupyter_cadquery import show

# Parâmetros
raio = 10
altura = 20

# Modelo
cilindro = cq.Workplane("XY").cylinder(altura, raio)

# Visualizar
show(cilindro)

# Exportar
cq.exporters.export(cilindro, "cilindro.stl")
```

### Exemplo de Forma Mais Complexa

```python
import cadquery as cq

def criar_caixa_parametrica(
    largura=50,
    profundidade=30,
    altura=20,
    espessura_parede=2,
    raio_cantos=3
):
    """Cria uma caixa paramétrica com tampa."""
    
    # Corpo da caixa
    caixa = (
        cq.Workplane("XY")
        .box(largura, profundidade, altura)
        .faces(">Z")
        .shell(-espessura_parede)
        .edges("|Z")
        .fillet(raio_cantos)
    )
    
    return caixa

# Criar modelo
minha_caixa = criar_caixa_parametrica(
    largura=60,
    profundidade=40,
    altura=25,
    espessura_parede=2.5,
    raio_cantos=4
)

# Visualizar
show_object(minha_caixa)

# Exportar
cq.exporters.export(minha_caixa, "caixa.stl")
```

## 📚 Recursos e Documentação

### Documentação Oficial

- **CadQuery Documentation**
  - https://cadquery.readthedocs.io/
  - Tutorial completo, API reference, exemplos

- **CadQuery Examples Gallery**
  - https://cadquery.readthedocs.io/en/latest/examples.html
  - Galeria de exemplos práticos

- **Build123d** (Sucessor do CadQuery)
  - https://build123d.readthedocs.io/
  - Versão mais moderna com sintaxe melhorada

### Tutoriais e Cursos

- **CadQuery Tutorial for Beginners**
  - https://cadquery.readthedocs.io/en/latest/intro.html
  
- **YouTube - CadQuery Tutorials**
  - Canal "3D Printing Professor"
  - Tutoriais práticos de CadQuery

### Comunidades

- **CadQuery Discord**
  - Comunidade ativa para tirar dúvidas
  - https://discord.gg/Bj9AQPsCfx

- **CadQuery Google Group**
  - https://groups.google.com/g/cadquery

- **Reddit - r/CadQuery**
  - https://www.reddit.com/r/cadquery/

### Bibliotecas Alternativas

- **OpenSCAD + SolidPython**
  - https://github.com/SolidCode/SolidPython
  - Gera código OpenSCAD via Python

- **Trimesh**
  - https://trimsh.org/
  - Manipulação de meshes 3D

- **PyMesh**
  - https://pymesh.readthedocs.io/
  - Processamento de geometria

- **FreeCAD Python API**
  - https://wiki.freecad.org/Python_scripting_tutorial
  - Scripting em FreeCAD

### Artigos e Guias

- **"Parametric 3D Modeling with Python"**
  - https://www.openbookproject.net/books/

- **CadQuery Cheat Sheet**
  - https://github.com/CadQuery/cadquery/wiki

### Ferramentas Complementares

- **pyenv**
  - https://github.com/pyenv/pyenv (Linux/Mac)
  - https://github.com/pyenv-win/pyenv-win (Windows)
  - Gerenciador de versões Python
  - https://github.com/pyenv/pyenv-virtualenv (plugin virtualenv para Linux/Mac)

- **OCP CAD Viewer**
  - https://github.com/roipoussiere/cadquery-viewer
  - Documentação da extensão

- **Jupyter-CadQuery**
  - https://github.com/bernhard-42/jupyter-cadquery
  - Visualização em notebooks

## 🎯 Dicas de Boas Práticas

1. **Use pyenv**: Gerenciar versões Python facilita compatibilidade
2. **Ambiente virtual por projeto**: Isola dependências e evita conflitos
3. **Parametrize tudo**: Use variáveis para todos os valores
4. **Funções reutilizáveis**: Crie funções para formas comuns
5. **Documente**: Adicione comentários explicando cada etapa
6. **Versione**: Use git para versionar seus modelos
7. **Teste incrementalmente**: Visualize frequentemente durante o desenvolvimento
8. **Tolerâncias**: Considere tolerâncias de impressão (0.1-0.2mm)
9. **Orientação**: Pense na orientação de impressão ao modelar

## 🔍 Troubleshooting

### Problema: `show_object()` não funciona

- Certifique-se de ter a extensão OCP CAD Viewer instalada
- Verifique se a extensão está habilitada

### Problema: Importação lenta do CadQuery

- O CadQuery carrega o OpenCascade, que é pesado
- Primeira importação pode demorar 5-10 segundos

### Problema: Erros ao exportar STL

- Verifique se o modelo é sólido (não tem superfícies abertas)
- Use `.val()` para verificar se o objeto é válido

### Problema: Visualização não aparece

- Reinicie o VS Code
- Verifique se o terminal não tem erros de importação

### Problema: VS Code não reconhece o Python do pyenv

**Linux/Mac:**
- Verifique se o pyenv está no PATH:
  ```bash
  which python
  ```
- Selecione o interpretador manualmente no VS Code:
  - `Ctrl+Shift+P` → "Python: Select Interpreter"
  - Escolha o interpretador do pyenv (ex: `~/.pyenv/versions/3.12.2/bin/python`)

**Windows:**
- Verifique se o pyenv está no PATH:
  ```powershell
  where.exe python
  ```
- Selecione o interpretador manualmente no VS Code:
  - `Ctrl+Shift+P` → "Python: Select Interpreter"
  - Escolha o interpretador do pyenv (ex: `C:\Users\SeuUsuario\.pyenv\pyenv-win\versions\3.12.2\python.exe`)

### Problema: ModuleNotFoundError após instalar pacotes

**Linux/Mac:**
- Certifique-se de que o ambiente virtual está ativado
- Verifique qual Python está sendo usado:
  ```bash
  which python
  pip --version
  ```
- Reinstale os pacotes no ambiente correto

**Windows:**
- Certifique-se de que o ambiente virtual está ativado
- Verifique qual Python está sendo usado:
  ```powershell
  where.exe python
  pip --version
  ```
- Reinstale os pacotes no ambiente correto

### Problema: Erro de política de execução no Windows PowerShell

- Execute como Administrador:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
- Ou use CMD em vez de PowerShell

### Problema: pyenv-win não encontrado no Windows

- Verifique se foi adicionado ao PATH corretamente
- Reinicie o terminal/PowerShell
- Adicione manualmente ao PATH do sistema:
  - `Painel de Controle` → `Sistema` → `Configurações Avançadas` → `Variáveis de Ambiente`
  - Adicione `%USERPROFILE%\.pyenv\pyenv-win\bin` e `%USERPROFILE%\.pyenv\pyenv-win\shims` ao PATH

## 📝 Licença e Contribuição

Este guia é de domínio público. Sinta-se livre para contribuir e melhorar!

---

**Data de criação:** Dezembro 2025  
**Última atualização:** 12/12/2025
