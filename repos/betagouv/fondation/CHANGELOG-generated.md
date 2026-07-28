## Changelog : fondation (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a continué à améliorer la plateforme, en se concentrant sur la refactorisation du code pour une meilleure maintenabilité et performance, l'ajout de nouvelles fonctionnalités pour la gestion des nominations et des rapports, et la correction de bugs pour une expérience utilisateur plus fluide. Une migration vers des outils de test plus modernes a également été initiée.

### Évolutions fonctionnelles
- Ajout d'un lien vers le rapport du membre concerné dans l'en-tête Magistrat [#500](https://github.com/betagouv/fondation/issues/500).
- Possibilité de sauvegarder les éditions des rapports officiels [#510](https://github.com/betagouv/fondation/issues/510).
- Ajout de la possibilité de joindre des fichiers à une nomination [#407](https://github.com/betagouv/fondation/issues/407).
- Ajout d'une date d'audition pour les nominations [#463](https://github.com/betagouv/fondation/issues/463).
- Amélioration de la sélection des fichiers d'agenda [#451](https://github.com/betagouv/fondation/issues/451).
- Ajout d'un point d'autorisation M2M pour Magistrat [#502](https://github.com/betagouv/fondation/issues/502).
- Ajout d'un bouton "+" sur la ligne de titre de la liste des observations pour faciliter l'ajout de nouvelles observations [#497](https://github.com/betagouv/fondation/issues/497).
- Refonte de la modale d'observation et affichage des observations dans un panneau latéral [#474](https://github.com/betagouv/fondation/issues/474) et [#484](https://github.com/betagouv/fondation/issues/484).
- Affichage d'un message de statut lors de la sauvegarde de la date d'audition et possibilité de modifier les dates passées après confirmation [#508](https://github.com/betagouv/fondation/issues/508).
- Ajout d'étiquettes de statut des fichiers de nomination à partir de l'API [#473](https://github.com/betagouv/fondation/issues/473).

### Évolutions techniques
- Migration vers Vitest pour les tests unitaires [#437](https://github.com/betagouv/fondation/issues/437).
- Refactorisation du code pour adopter une architecture orientée fonctionnalités (feature-first) dans plusieurs modules (auth, reports, admin, summary, hooks, layout, secretariat-general) [#427](https://github.com/betagouv/fondation/issues/427), [#428](https://github.com/betagouv/fondation/issues/428), [#429](https://github.com/betagouv/fondation/issues/429), [#430](https://github.com/betagouv/fondation/issues/430), [#431](https://github.com/betagouv/fondation/issues/431), [#432](https://github.com/betagouv/fondation/issues/432), [#433](https://github.com/betagouv/fondation/issues/433).
- Internalisation de plusieurs enums et types (Role, Gender, Magistrat.Formation, Magistrat.Grade) pour une meilleure cohérence et maintenabilité [#480](https://github.com/betagouv/fondation/issues/480), [#481](https://github.com/betagouv/fondation/issues/481), [#483](https://github.com/betagouv/fondation/issues/483), [#485](https://github.com/betagouv/fondation/issues/485), [#486](https://github.com/betagouv/fondation/issues/486), [#490](https://github.com/betagouv/fondation/issues/490), [#491](https://github.com/betagouv/fondation/issues/491).
- Suppression des modèles partagés (shared-models) et refactorisation du code associé [#495](https://github.com/betagouv/fondation/issues/495), [#496](https://github.com/betagouv/fondation/issues/496), [#499](https://github.com/betagouv/fondation/issues/499), [#494](https://github.com/betagouv/fondation/issues/494).
- Mise à jour de plusieurs dépendances (NestJS, Prisma, S3) [#452](https://github.com/betagouv/fondation/issues/452), [#454](https://github.com/betagouv/fondation/issues/454), [#481](https://github.com/betagouv/fondation/issues/481).
- Utilisation des tokens de couleurs DSFR au lieu des couleurs Tailwind natives [#418](https://github.com/betagouv/fondation/issues/418).

### Autres changements
- Correction de la documentation concernant le rôle de relais SDV et ajout de Scaleway au diagramme d'architecture [#509](https://github.com/betagouv/fondation/issues/509).
- Ajout de guides Storybook et mise à jour du fichier README principal [#507](https://github.com/betagouv/fondation/issues/507).
- Suppression d'un appel supprimé à sheetjs.sh du build Scalingo [#501](https://github.com/betagouv/fondation/issues/501).
- Suppression de la modale de rappel de suivi des observations lors de la définition du résultat [#493](https://github.com/betagouv/fondation/issues/493).
- Correction du cache Vite pour éviter les problèmes de mise à jour des icônes DSFR [#487](https://github.com/betagouv/fondation/issues/487) et [#489](https://github.com/betagouv/fondation/issues/489).
- Amélioration de la gestion des fichiers agenda [#465](https://github.com/betagouv/fondation/issues/465), [#478](https://github.com/betagouv/fondation/issues/478).
- Correction de l'affichage du titre du président [#466](https://github.com/betagouv/fondation/issues/466).
- Correction de la numérotation des rapports [#480](https://github.com/betagouv/fondation/issues/480).
- Mise en place de tests pour vérifier la cohérence entre l'API et les clients OpenAPI [#472](https://github.com/betagouv/fondation/issues/472).
- Déploiement de Storybook sur Scalingo [#477](https://github.com/betagouv/fondation/issues/477).
- Amélioration de la gestion des erreurs et des dépendances.
- Diverses corrections de bugs et améliorations de la qualité du code.
