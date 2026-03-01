## Changelog : france-chaleur-urbaine (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées au site france-chaleur-urbaine au cours du dernier mois. Les principales évolutions concernent la mise à jour des données réseaux de chaleur, l'intégration d'un outil d'analyse (PostHog) pour mieux comprendre l'utilisation du site, et une refactorisation du code pour une meilleure maintenabilité. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été réalisées.

### Évolutions fonctionnelles
- Mise à jour des données réseaux de chaleur avec les DLE 2024. [#1207](https://github.com/betagouv/france-chaleur-urbaine/pull/1207)
- Ajout d'un CTA (Call To Action) spécifique pour les utilisateurs non raccordables. [#1199](https://github.com/betagouv/france-chaleur-urbaine/pull/1199)
- Correction d'un bug dans le test d'adresse, notamment pour la ville de Bordeaux. [#1203](https://github.com/betagouv/france-chaleur-urbaine/pull/1203)
- Suppression de la bannière du comparateur de coûts.
- Ajout d'un commentaire pour les statistiques par tag. [#1196](https://github.com/betagouv/france-chaleur-urbaine/pull/1196)
- Intégration du suivi analytics via PostHog pour une meilleure compréhension de l'utilisation du site. [#1203](https://github.com/betagouv/france-chaleur-urbaine/pull/1203)
- Ajout d'événements Matomo pour le CTA vers le comparateur et pour l'analyse des données.

### Évolutions techniques
- Refactorisation du code lié aux données open data, avec déplacement des fichiers dans un module dédié. [#1205](https://github.com/betagouv/france-chaleur-urbaine/pull/1205)
- Suppression de composants et fichiers inutilisés dans le code frontend.
- Utilisation de `cx` pour la gestion des classes CSS.
- Passage de TypeScript en dépendances.
- Correction d'un bug lié à la réaffection des gestionnaires. [#1197](https://github.com/betagouv/france-chaleur-urbaine/pull/1197)
- Suppression du markdown au profit du HTML pour certains éléments de l'interface utilisateur. [#1201](https://github.com/betagouv/france-chaleur-urbaine/pull/1201)

### Autres changements
- Mise à jour des textes et des labels pour l'année 2024.
- Ajout d'un script pour la mise à jour des données avec la bibliothèque fedene.
- Ajout d'un fichier `.editorconfig` pour la configuration de l'éditeur de code VSCode.
- Mise à jour de la version de Publicodes.
- Mise à jour de la documentation avec les étapes de développement et de lancement du serveur.
- Suppression d'informations MO inutilisées (adresse, code postal, ville).
- Suppression de la doc obsolète.
- Ajout d'une ancre sur les Headings pour faciliter la navigation.
- Suppression d'un localhost utilisé pour les tests.
- Ajout d'un événement à la configuration analytics.
- Correction de la syntaxe et mise à jour de l'adresse dans un cas de test.
