## Changelog : st-home (30 derniers jours, au 19 juin 2026)

### Résumé
Cette mise à jour apporte des améliorations à la gestion des tâches asynchrones, corrige des bugs liés à l'affichage de la carte et des données, et améliore l'intégration avec certains services externes. Des ajustements ont également été faits pour une meilleure expérience utilisateur, notamment concernant la recherche de communes et l'accès à l'aide en ligne.

### Évolutions fonctionnelles
- Amélioration de la recherche de communes : la recherche inclut désormais les organisations avec un nom exact. [#69](https://github.com/suitenumerique/st-home/issues/69)
- Affichage amélioré de la carte de déploiement (deploymap) : correction de l'affichage des seuils et des régions/départements. [#65](https://github.com/suitenumerique/st-home/issues/65)
- Intégration RPNT : autorise certains redirections vers des sites gouv.fr dans le cadre de la version 1.6 du Répertoire des Points de Contact Numériques (RPNT). [#69](https://github.com/suitenumerique/st-home/issues/69)
- Mise à jour du lien vers le centre d'aide. [#67](https://github.com/suitenumerique/st-home/issues/67)
- Ajout des Messages et Fichiers aux seuils ANCT (Agence Nationale de la Cohésion des Territoires). [#69](https://github.com/suitenumerique/st-home/issues/69)

### Évolutions techniques
- Remplacement de Celery par Dramatiq pour la gestion des tâches asynchrones. [#70](https://github.com/suitenumerique/st-home/issues/70)
- Amélioration de la gestion des retries et mise à jour du tableau de bord associé aux workers.
- Mise à jour de l'URL de la source de données Banatic.

### Autres changements
- Correction d'un bug affichant en double les services ProConnect dans la liste.
- Correction de l'affichage de la carte de déploiement pour le seuil ANCT.
