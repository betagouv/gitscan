## Changelog : monstagedeseconde (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'une refonte de la gestion des élèves et d'une amélioration de son interface visuelle, notamment avec l'ajout de carrousels pour les partenaires professionnels. Des travaux importants ont également été menés pour préparer la maintenance estivale et stabiliser les processus de déploiement et de tests.

### Évolutions fonctionnelles
- **Gestion des élèves** : Refonte de l'interface de gestion des élèves [#914](https://github.com/betagouv/monstagedeseconde/pull/914) et mise à jour de la page de profil élève [#941](https://github.com/betagouv/monstagedeseconde/pull/941).
- **Interface utilisateur** : Ajout de carrousels de logos pour mettre en avant les partenaires professionnels [#944](https://github.com/betagouv/monstagedeseconde/pull/944).
- **Accessibilité** : Correction de plusieurs problèmes d'accessibilité, notamment des ancres mortes et des textes alternatifs manquants sur les images.

### Évolutions techniques
- **Maintenance et disponibilité** : 
    - Mise en place d'un mode maintenance adapté pour la période estivale 2026 [#943](https://github.com/betagouv/monstagedeseconde/pull/943).
    - Amélioration de la gestion des accès administrateur durant les phases de maintenance.
- **CI/CD et Déploiement** : 
    - Optimisation du déploiement sur l'environnement de staging pour le rendre non bloquant dans la CI.
    - Mise à jour du client SSH pour les déploiements vers Clever Cloud.
- **Fiabilité et Tests** : 
    - Stabilisation des tests automatisés (correction de tests instables sur les candidatures d'équipe et la recherche d'établissements) [#940](https://github.com/betagouv/monstagedeseconde/pull/940).
- **Système** : Mise à jour de la tâche de fond dédiée à l'archivage des élèves.

### Autres changements
- **Nettoyage** : Suppression de l'intégration Tally et de certains blocs de code obsolètes.
