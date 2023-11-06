# ADA – Engenharia de dados


## Git & Github

	Git – sist. de versionamento de código, que guarda os registros de versão como snapshots do estado do projeto, além da referencia/caminha para essa foto.
	Salva localmente. 

		Estados 
Unmodified: o arquivo já está no git, já foi commitado e está salvo, sem novas alterações.
Modified: Arquivo com alterações não salvas no git ainda.
Staged: Preparatória para o commit – git add 
depois do git commit, o arquivo volta para o status unmodified


		Principais Comandos 
git diff : mostra exatamente as linhas que foram modificadas no terminal
git diff --staged : mostra exatamente as linhas que foram modificadas no terminal, mas que já estão no git (pós git add)
git log : histórico de commits com branch, autor, data e mensagem do commit, com hash do commit

git restore nomeDoArq : restaura as atualizações, antes de ir para a áea do staged (git add)
git restore --staged nomeDoArquivo restaura as atualizações, que já estão na áea do staged (git add)
git remote : ver o repo remoto
git fetch : verificar antes de dar um git pull as infos do repositório remoto que estão diferentes do repo local. Depois de do git fetch, dar um git diff com o nome da branch,para saber quais as linhas estão diferentes

		Branches
git branch nomeDaBranch – criar nova branch
gi tlog --oneline decorate : mostra pra onde o ponteiro HEAD está apontado, pu seja, em qual branch se está
git checkout nomeDaBranch : entra na branch


		Merge
git merge  e o nome da branch q qr trazer pra master