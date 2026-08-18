## Changelog : playground (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante dans l'automatisation et la personnalisation du workflow éditorial. Les utilisateurs bénéficient désormais d'un système de notifications (internes et Slack), d'une meilleure gestion des profils et d'outils de traduction assistés par IA plus flexibles. L'interface a également été largement modernisée pour faciliter la gestion des métadonnées et la navigation grâce à de nouveaux filtres et composants visuels.

### Évolutions fonctionnelles
- **Notifications & Communication** : Mise en place du système de notifications internes [#314](https://github.com/refugies-info/playground/issues/1415) et ajout de la possibilité d'envoyer des notifications vers Slack.
- **Gestion des traductions** : Ajout d'un bouton pour régénérer une traduction via l'IA [#306](https://github.com/refugies-info/playground/issues/1378) et intégration de métadonnées dans le workflow de traduction [#313](https://github.com/refugies-info/playground/issues/1379).
- **Profil utilisateur** : Possibilité d'importer une photo de profil (avatar) pour les utilisateurs [#307](https://github.com/refugies-info/playground/issues/1203).
- **Métadonnées & Contenu** : Refonte complète de l'interface de la page des métadonnées [#302](https://github.com/refugies-info/playground/issues/1387), ajout de champs pour les "informations pratiques" [#308](https://github.com/refugies-info/playground/issues/1224) et pour les descriptions de points d'intérêt (POI).
- **Navigation & Filtres** : Introduction de nouveaux filtres par date (date picker) sur la page de workflow [#309](https://github.com/refugies-info/playground/issues/1371) et sur l'onglet d'importation [#310](https://github.com/refugies-info/playground/issues/1421).
- **Interface (UI/UX)** : 
    - Amélioration de la visibilité du statut de publication dans le header des fiches [#312](https://github.com/refugies-info/playground/issues/1423).
    - Ajout de nouvelles fenêtres surgissantes (pop-ups) pour la publication [#305](https://github.com/refugies-info/playground/issues/1383) et pour signaler la modification d'une fiche [#303](https://github.com/refugies-info/playground/issues/1381).
- **Gestion des statuts** : Correction du comportement de changement automatique de statut [#311](https://github.com/refugies-info/playground/issues/1422) et levée des restrictions sur le changement de conformité [#298](https://github.com/refugies-info/playground/issues/1341).

### Évolutions techniques
- **Architecture & Données** : 
    - Refactorisation de la gestion des rôles utilisateurs [#316](https://github.com/refugies-info/playground/issues/316).
    - Renforcement du typage des données, notamment pour les champs email de contact [#315](https://github.com/refugies-info/playground/issues/1424).
- **Qualité & IA** : Investigation et correction de bugs liés au module de "langage clair" [#319](https://github.com/refugies-info/playground/issues/1436).
- **Design System** : Mise à jour majeure de l'interface utilisateur avec l'intégration de nouveaux composants (inputs DSFR, gestion des bordures et des couleurs de thèmes).

### Autres changements
- Nettoyage régulier du code (suppression de code mort et de commentaires inutiles).
- Corrections de linting et de formatage.
