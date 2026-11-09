# Roteiro para iniciar qualquer projeto

**Regra central:** não abra o editor antes de responder, no papel, o que você vai construir. Quem trava em código geralmente não travou na sintaxe, e sim em não saber o que quer que o programa faça.

---

## Fase 1: Entender o problema (10 a 15 min, sem código)

Escreva com suas palavras:

1. **O que o programa faz?** Uma frase só.
2. **Quem usa e como?** Qual é a entrada e qual é a saída?
3. **O que ele precisa fazer, no mínimo?** Liste as funcionalidades.
4. **O que fica de fora por enquanto?** Evita que o projeto cresça e seja abandonado.

Se não consegue explicar em voz alta para um leigo, ainda não está pronto para codar.

---

## Fase 2: Quebrar em pedaços pequenos

Para cada funcionalidade, pergunte: **"qual é o menor passo que eu consigo testar?"**

Cada item vira uma mini-meta. Riscar itens da lista mantém a motivação.

---

## Fase 3: Pensar antes de escrever (pseudocódigo)

Para cada função, escreva o passo a passo em português:

```
função adicionar_tarefa:
    pedir o título
    criar a tarefa com título e status "pendente"
    colocar na lista
    salvar
```

Depois traduza linha por linha para Python. Se travar, você sabe exatamente qual linha é o problema.

Perguntas antes de cada função:
- O que entra (parâmetros) e o que sai (retorno)?
- Que dado preciso guardar? Lista, dicionário, conjunto?
- O que pode dar errado? (entrada vazia, arquivo inexistente, número no lugar de texto)

---

## Fase 4: Construir em ciclos curtos

1. Faça a **versão mais simples possível** funcionar, mesmo feia.
2. Rode e teste a cada pedaço pequeno, não só no final.
3. Use `print()` à vontade para ver o que acontece dentro do código.
4. Só depois que funciona, melhore: nomes, funções menores, tratamento de erros.
5. Faça commit no Git a cada etapa que funciona.

**Lema: primeiro funciona, depois fica bonito.**

---

## Fase 5: Quando travar (siga a escada em ordem)

| Degrau | O que fazer | Tempo |
|---|---|---|
| 1 | Ler a mensagem de erro inteira (arquivo, linha, tipo de erro) | 2 min |
| 2 | Colocar `print()` nas variáveis para ver os valores reais | 5 min |
| 3 | Explicar o problema em voz alta (patinho de borracha) | 5 min |
| 4 | Consultar a documentação oficial (docs.python.org/pt-br) | 10 min |
| 5 | Pesquisar a mensagem de erro no Google ou Stack Overflow | 10 min |
| 6 | Perguntar à IA, pedindo **dica e não solução** | só aqui |

**Como pesquisar:** copie a mensagem de erro exata + "python" + nome da biblioteca. Ex.: `python KeyError dictionary`.

**Como pedir ajuda à IA sem se prejudicar:**
- Ruim: "Faz um gerenciador de tarefas em Python."
- Bom: "Estou tentando remover um item de uma lista de dicionários pelo id, mas recebo este erro: [erro]. Meu código: [trecho]. Pode me explicar o que está errado sem reescrever tudo?"

**Regra de ouro:** se algo foi ajudado pela IA, você precisa conseguir explicar linha por linha sem olhar.

---

## Fontes confiáveis

- **Documentação oficial do Python:** docs.python.org/pt-br
- **Real Python:** realpython.com (tutoriais detalhados)
- **Stack Overflow:** erros específicos
- **Python Tutor:** pythontutor.com (mostra o código rodando passo a passo)
- **GitHub:** ler projetos simples de outras pessoas

---

## Fase 6: Fechar o projeto

Só vale para portfólio se estiver **terminado**:
- [] README (o que faz, como rodar, exemplo de uso)
- [] Nomes de variáveis e funções revisados
- [] Testes básicos com `pytest` (a partir do nível 2)
- [] 3 respostas de entrevista: *qual problema resolvia, que decisão técnica tomei e por quê, o que faria diferente*

---

## Checklist rápido

- [] Consigo explicar o projeto em uma frase?
- [] Listei o que entra, o que sai e o que fica de fora?
- [] Quebrei em passos pequenos e testáveis?
- [] Escrevi o pseudocódigo antes de codar?
- [] Tentei sozinho por 15 a 20 min antes de pedir ajuda?
- [] Fiz commit do que funciona?