# Déploiement facile de Sites Conformes 

Ce repo permet de facilement déployer et maintenir à jour des instances de 
https://github.com/numerique-gouv/sites-conformes.

Il contient 2 branches:
- La branche `production` qui est synchronisée sur des releases de
  `sites-conformes` et qui nous sert à déployer nos instances.
- La branche `main` contient une action github qui vérifie tous les jours si un
  nouveau tag existe sur `sites-conforme`, et le cas échéant ouvre une PR pour
  mettre à jour la branche `production`.
