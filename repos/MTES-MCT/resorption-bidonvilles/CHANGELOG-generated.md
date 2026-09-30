## Changelog : resorption-bidonvilles (30 derniers jours, au 24/09/2026)

### Résumé
Les récentes évolutions se concentrent sur trois axes majeurs : le renforcement de la sécurité des données et des accès, l'amélioration de l'ergonomie via l'intégration de nouveaux composants de design (DSFR) et l'optimisation des performances de la plateforme (base de données et requêtes API).

### Évolutions fonctionnelles
- **Gestion des communications** : Ajout de la possibilité de filtrer les destinataires des messages lors des actions, harmonisant ainsi le fonctionnement avec la gestion des sites [#1537](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2737).
- **Sécurité et accès** : Renforcement des contrôles de permissions pour empêcher l'accès non autorisé aux données cadastrales ou territoriales et sécuriser la gestion des comptes [#2772](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2772).
- **Interface et Ergonomie (UI/UX)** :
    - Intégration de nouveaux composants de filtrage (`DsfrFiltre`) et de tri (`DsfrSort`) conformes au design system pour améliorer l'accessibilité et la cohérence visuelle [#2745](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2745).
    - Amélioration de la cartographie avec le passage à OpenStreetMap et l'activation du zoom à la molette [#2758](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2758) [#2760](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2760).
    - Uniformisation des indicateurs de chargement (spinners) sur l'ensemble de l'application [#2750](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2750).
    - Correction de l'affichage des dates pour éviter l'apparition de dates erronées (1970) lors de champs non renseignés [#2764](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2764).

### Évolutions techniques
- **Sécurité de l'API** : Refonte majeure de la construction des requêtes SQL pour prévenir les injections et sécuriser l'utilisation de paramètres dynamiques dans l'ensemble des modèles [#2763](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2763).
- **Performances** :
    - Optimisation des requêtes d'historique et de statistiques pour réduire la charge serveur [#2763](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2763).
    - Ajout d'index de base de données sur les tables de villes, départements et logs de navigation pour accélérer les recherches et les calculs [#2774](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2774).
- **Qualité et Build** :
    - Modernisation du code frontend par la migration de composants vers la syntaxe `<script setup>` de Vue 3.
    - Correction de divers problèmes liés au processus de build (Vite, LightningCSS) et à la gestion des variables d'environnement.
    - Amélioration de la robustesse des tests et du typage TypeScript.

### Autres changements
- Configuration de Renovate pour la gestion automatisée des dépendances dans le monorepo.
- Nettoyage du code (suppression de fichiers et d'imports inutilisés) et corrections de linting.
