## Changelog : euphrosyne (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des certifications, l'ajout de nouvelles fonctionnalités pour la gestion des projets et des participations, ainsi que des corrections de bugs et des mises à jour de sécurité. Plusieurs améliorations techniques ont également été apportées, notamment des mises à jour de dépendances et des optimisations du code.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité d'export CSV pour les utilisateurs ayant réussi une certification [#6600b34](https://github.com/betagouv/euphrosyne/commit/6600b34).
- Implémentation d'un interrupteur pour activer/désactiver le type de participation sur la table des participations, offrant plus de flexibilité dans la gestion des workflows [#f6e6c7e](https://github.com/betagouv/euphrosyne/commit/f6e6c7e).
- Possibilité pour les administrateurs de rendre le workflow d'employeur non bloquant, améliorant l'efficacité des processus [#2016953](https://github.com/betagouv/euphrosyne/commit/2016953).
- Ajout d'une période de grâce avant de pouvoir "re-refroidir" un projet, offrant plus de contrôle sur le cycle de vie des projets [#98a6c35](https://github.com/betagouv/euphrosyne/commit/98a6c35).
- Correction de l'alignement des colonnes de participation dans l'interface utilisateur [#0d639ae](https://github.com/betagouv/euphrosyne/commit/0d639ae).
- Correction d'un bug lié à l'analyse incorrecte de l'ID d'exécution dans le middleware [#a0c5653](https://github.com/betagouv/euphrosyne/commit/a0c5653).
- Ajout d'une action permettant à un administrateur de se faire passer pour un autre utilisateur [#be2f0fd](https://github.com/betagouv/euphrosyne/commit/be2f0fd).
- Correction pour utiliser le slug pour le renommage du répertoire du projet [#ba6440d](https://github.com/betagouv/euphrosyne/commit/ba6440d).
- Correction pour placer le décorateur `api_view` en haut de la fonction, assurant son application correcte [#ff5c7fb](https://github.com/betagouv/euphrosyne/commit/ff5c7fb).
- Correction pour empêcher la soumission du formulaire modal de planification lors de la fermeture via le bouton "Annuler" [#65914ad](https://github.com/betagouv/euphrosyne/commit/65914ad).

### Évolutions techniques
- Ajout d'une protection contre les origines non autorisées pour les requêtes de données [#8ec9518](https://github.com/betagouv/euphrosyne/commit/8ec9518).
- Correction d'une potentielle injection dans l'export CSV des certifications [#11f152e](https://github.com/betagouv/euphrosyne/commit/11f152e).
- Mise à jour de plusieurs dépendances, incluant Django, React, TypeScript, webpack, et divers paquets npm et pip.
- Suppression de `downlevelIteration` dans le `tsconfig.json` pour une meilleure compatibilité et performance [#89fbd72](https://github.com/betagouv/euphrosyne/commit/89fbd72).
- Application de corrections npm audit fix pour améliorer la sécurité des dépendances front-end [#6851436](https://github.com/betagouv/euphrosyne/commit/6851436).

### Autres changements
- Documentation mise à jour et améliorations générales du code.
- Ajout de type ignore pour certaines parties du code [#5b1a602](https://github.com/betagouv/euphrosyne/commit/5b1a602).
- Mise à jour des types de requêtes [#a3a4ba1](https://github.com/betagouv/euphrosyne/commit/a3a4ba1).
