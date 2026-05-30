## Changelog : vizeau (30 derniers jours, au 29 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'interface utilisateur, notamment concernant la visualisation des données de qualité de l'eau et la gestion des substances. Des fonctionnalités importantes ont également été ajoutées pour la gestion des projets et des territoires, ainsi que pour l'export de données. Plusieurs corrections de bugs et optimisations ont été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'une vue synthétique de la qualité de l'eau, incluant un indicateur CTA sur les cartes récapitulatives. [#428](https://github.com/MTES-MCT/vizeau/issues/428)
- Amélioration de la visualisation du suivi des substances avec l'introduction d'un nouveau composant de sélection `<SingleSelectMenu/>`. [#409](https://github.com/MTES-MCT/vizeau/issues/409)
- Possibilité d'attacher des exploitations, parcelles et captages aux projets. [#425](https://github.com/MTES-MCT/vizeau/issues/425) et [#433b818](https://github.com/MTES-MCT/vizeau/commit/433b818)
- Ajout de commandes de seeding pour les utilisateurs et territoires, facilitant la mise en place d'environnements de test. [#422](https://github.com/MTES-MCT/vizeau/issues/422)
- Implémentation de la création de nouveaux territoires depuis la ligne de commande. [#410](https://github.com/MTES-MCT/vizeau/issues/410)
- Ajout de l'export des données AAC (Agences de l'Eau) au format CSV, avec des améliorations de robustesse et de formatage des données. [#386](https://github.com/MTES-MCT/vizeau/issues/386)
- Ajout d'analyses pour les installations de captage. [#393](https://github.com/MTES-MCT/vizeau/issues/393)
- Affichage d'un toaster de confirmation lors de l'attribution des parcelles. [#403](https://github.com/MTES-MCT/vizeau/issues/403)
- Amélioration de l'affichage des parcelles sur la carte, avec un z-index augmenté pour une meilleure visibilité. [#401](https://github.com/MTES-MCT/vizeau/issues/401)
- Correction de l'import d'un graphique. [#400](https://github.com/MTES-MCT/vizeau/issues/400)
- Correction d'un bug sur l'info-bulle du Design System Français (DSFR). [#395](https://github.com/MTES-MCT/vizeau/issues/395)
- Correction de l'affichage de l'évolution des parcelles bio (passage de % à ha). [#428](https://github.com/MTES-MCT/vizeau/issues/428)
- Tri des substances affichées dans la liste déroulante. [#407](https://github.com/MTES-MCT/vizeau/issues/407)

### Évolutions techniques
- Mise à jour du service de recherche d'exploitations. [#404](https://github.com/MTES-MCT/vizeau/issues/404)
- Implémentation du module CRUD (Create, Read, Update, Delete) pour la gestion des projets. [#405](https://github.com/MTES-MCT/vizeau/issues/405)
- Remplacement du composant `<Select/>` du DSFR par `<SingleSelectMenu/>` pour une meilleure gestion et personnalisation. [#409](https://github.com/MTES-MCT/vizeau/issues/409)
- Correction d'une mauvaise requête SQL. [#0c98a5b](https://github.com/MTES-MCT/vizeau/commit/0c98a5b)

### Autres changements
- Mise à jour du fichier `.gitignore`. [#399](https://github.com/MTES-MCT/vizeau/issues/399)
- Diverses corrections et améliorations apportées suite aux suggestions de Copilot.
