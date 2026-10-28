## Changelog : complements-alimentaires (30 derniers jours, au 27 octobre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur la fiabilisation des données saisies, notamment via une meilleure validation des entreprises (SIRET), et sur l'amélioration des outils de gestion pour l'administration. Les formulaires ont également été renforcés pour garantir la complétude des dossiers soumis.

### Évolutions fonctionnelles
- **Validation des entreprises** : amélioration de la vérification des SIRET via l'API "recherche entreprises", incluant une gestion spécifique pour les entreprises fermées ou introuvables [#3153](https://github.com/betagouv/complements-alimentaires/issues/3153).
- **Gestion des formulaires** : les champs "populations" et "effets" sont désormais obligatoires pour permettre la soumission d'une déclaration.
- **Interface d'administration** : 
    - Ajout de la possibilité de modifier la date de retrait des déclarations [#3175](https://github.com/betagouv/complements-alimentaires/issues/3175).
    - Intégration d'une colonne "date de création" pour le suivi des dossiers (SD) [#3127](https://github.com/betagouv/complements-alimentaires/issues/3127).
- **FAQ** : mise à jour du contenu avec l'ajout de nouvelles questions [#3181](https://github.com/betagouv/complements-alimentaires/issues/3181).
- **Corrections** : résolution d'un bug concernant la gestion des champs multi-valeurs obligatoires [#3125](https://github.com/betagouv/complements-alimentaires/issues/3125).

### Évolutions techniques
- **Authentification** : refonte du flux de déconnexion (ProConnect) pour améliorer la gestion des redirections et la robustesse du processus [#3165](https://github.com/betagouv/complements-alimentaires/issues/3165).
- **Sécurité** : renforcement de la désinfection des données utilisateurs et correction de vulnérabilités potentielles liées à l'injection de logs.
- **Optimisation UX** : intégration de la validation du SIRET côté client avant l'envoi des requêtes à l'API [#3153](https://github.com/betagouv/complements-alimentaires/issues/3153).

### Autres changements
- **Nettoyage** : simplification du fichier `requirements.txt` par la suppression de `pre_commit` et `virtualenv`.
