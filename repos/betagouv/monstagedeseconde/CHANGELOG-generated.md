## Changelog : monstagedeseconde (30 derniers jours, au 17 août 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'améliorations significatives pour la gestion des élèves et l'affichage des partenaires. Nous avons également procédé à un nettoyage technique important en supprimant des modules obsolètes et en renforçant la stabilité de nos processus de déploiement et de tests automatisés.

### Évolutions fonctionnelles
- **Gestion des élèves** : Mise en place d'une nouvelle interface de gestion des élèves [#914](https://github.com/betagouv/monstagedeseconde/pull/914) et mise à jour de la page profil élève [#941](https://github.com/betagouv/monstagedeseconde/pull/941).
- **Partenaires** : Ajout d'un carrousel pour l'affichage des logos des partenaires [#944](https://github.com/betagouv/monstagedeseconde/pull/944).
- **Accessibilité** : Correction de plusieurs problèmes d'accessibilité, notamment des liens morts et des images sans description textuelle (alt), afin de garantir une meilleure expérience utilisateur.

### Évolutions techniques
- **Nettoyage du code** : Suppression complète du module Tally et de ses liens associés [#950](https://github.com/betagouv/monstagedeseconde/pull/950).
- **Fiabilité des tests** : Correction de nombreux tests automatisés "instables" (flaky tests) concernant les candidatures d'équipe, la recherche d'établissements et la signature de groupe [#940](https://github.com/betagouv/monstagedeseconde/pull/940).
- **Déploiement et CI/CD** : Optimisation du processus de déploiement sur l'environnement de staging (rendu non-bloquant) et mise à jour du client SSH pour les déploiements vers Clever Cloud.
- **Mode maintenance** : Amélioration de la gestion du mode maintenance, permettant de maintenir l'accès aux administrateurs et de normaliser la recherche par email.
