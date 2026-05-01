## Changelog : territoires-en-transitions (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des fiches d'actions, notamment la migration des étapes vers des sous-actions, l'intégration de la personnalisation des référentiels et l'optimisation des performances. Des améliorations ont également été apportées à l'interface utilisateur et à l'expérience utilisateur, ainsi qu'à l'infrastructure et aux tests.

### Évolutions fonctionnelles
- **Fiches d'actions :** Transformation des étapes d'une fiche en sous-actions, offrant une granularité accrue dans le suivi des actions [#1760794](https://github.com/incubateur-ademe/territoires-en-transitions/commit/1760794).
- **Personnalisation des référentiels :** Implémentation de la personnalisation des référentiels avec un lien entre les questions et une interface dédiée, permettant une adaptation plus fine aux besoins des collectivités [#c5a5e91](https://github.com/incubateur-ademe/territoires-en-transitions/commit/c5a5e91).
- **Rapports :** Ajout de la possibilité d'inclure la dernière note dans les rapports [#6f4471d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/6f4471d).
- **Indicateurs :** Préservation des favoris et de la confidentialité lors de la mise à jour partielle d'un indicateur [#16f2830](https://github.com/incubateur-ademe/territoires-en-transitions/commit/16f2830).
- **Notifications :** Affichage du prénom plutôt que du nom dans les emails de notification aux pilotes [#bf25b94](https://github.com/incubateur-ademe/territoires-en-transitions/commit/bf25b94).
- **Pages :** Correction de la pagination de la page Actualités [#bc04d44](https://github.com/incubateur-ademe/territoires-en-transitions/commit/bc04d44).
- **Plans :** Possibilité pour les contributeurs pilotes de créer, modifier et supprimer des sous-actions [#e2e6673](https://github.com/incubateur-ademe/territoires-en-transitions/commit/e2e6673).
- **Export PDF :** Mise à jour du style et du wording des tags dans l'export PDF des fiches d'actions [#c3aea8a](https://github.com/incubateur-ademe/territoires-en-transitions/commit/c3aea8a).

### Évolutions techniques
- **API :** Migration des mutations de fiche de Supabase vers tRPC [#0ec6066](https://github.com/incubateur-ademe/territoires-en-transitions/commit/0ec6066).
- **Base de données :** Ajout d'index sur les tables d'historique pour améliorer les performances [#b9d106d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/b9d106d).
- **Tests :** Amélioration de l'isolation des tests et parallélisation pour une exécution plus rapide [#952f739](https://github.com/incubateur-ademe/territoires-en-transitions/commit/952f739).
- **CI/CD :** Mise à jour des actions GitHub pour utiliser des versions compatibles avec Node.js 24 [#37fd5a9](https://github.com/incubateur-ademe/territoires-en-transitions/commit/37fd5a9).
- **Infrastructure :** Ajout d'un dashboard privé Streamlit dans le healthcheck et mise à jour du checker Streamlit [#1b92c46](https://github.com/incubateur-ademe/territoires-en-transitions/commit/1b92c46), [#79207a7](https://github.com/incubateur-ademe/territoires-en-transitions/commit/79207a7).
- **Refactoring :** Mutualisation de `use-get-fiche` et suppression de code legacy [#b244791](https://github.com/incubateur-ademe/territoires-en-transitions/commit/b244791).
- **Performance :** Ajout d'un debounce sur les RichTextEditor pour alléger les appels au serveur de la FA [#d084f6b](https://github.com/incubateur-ademe/territoires-en-transitions/commit/d084f6b).

### Autres changements
- **Documentation :** Mise à jour du texte de description des rôles des membres [#a002502](https://github.com/incubateur-ademe/territoires-en-transitions/commit/a002502).
- **Interface utilisateur :** Corrections de la hiérarchie des titres sur différentes pages du site [#eeca70c](https://github.com/incubateur-ademe/territoires-en-transitions/commit/eeca70c), [#c411c83](https://github.com/incubateur-ademe/territoires-en-transitions/commit/c411c83), [#2153825](https://github.com/incubateur-ademe/territoires-en-transitions/commit/2153825), [#0b1801b](https://github.com/incubateur-ademe/territoires-en-transitions/commit/0b1801b), [#fed9bfa](https://github.com/incubateur-ademe/territoires-en-transitions/commit/fed9bfa).
- **Configuration :** Mise à jour de l'adresse d'envoi d'email [#1e2a780](https://github.com/incubateur-ademe/territoires-en-transitions/commit/1e2a780).
- **Suppression de code :** Suppression de vues et fonctions sur les questions/réponses/thématiques de personnalisation [#4258d03](https://github.com/incubateur-ademe/territoires-en-transitions/commit/4258d03), d'une fonction inutilisée [#bb61d02](https://github.com/incubateur-ademe/territoires-en-transitions/commit/bb61d02) et de certaines vues SQL obsolètes [#ca24423](https://github.com/incubateur-ademe/territoires-en-transitions/commit/ca24423).
