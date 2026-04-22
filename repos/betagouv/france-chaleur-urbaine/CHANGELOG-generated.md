## Changelog : france-chaleur-urbaine (30 derniers jours, au 16 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec la refonte de la page "Qui sommes-nous", l'ajout d'informations sur les éco-réseaux et l'amélioration de la gestion des filtres dans l'interface d'administration. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Page "Qui sommes-nous" :** Refonte complète de la page avec suppression des icônes de l'équipe et clarification de la formulation concernant le budget [#1232](https://github.com/betagouv/france-chaleur-urbaine/pull/1232).
- **Éco-réseaux :** Ajout d'une fonctionnalité permettant d'importer et d'afficher les informations sur les éco-réseaux, incluant une colonne dédiée dans la liste des réseaux de chaleur et une source d'information pour ces données [#1224](https://github.com/betagouv/france-chaleur-urbaine/pull/1224), [#1227](https://github.com/betagouv/france-chaleur-urbaine/pull/1227).
- **Filtres :** Amélioration de la gestion des filtres dans l'interface d'administration, notamment pour les valeurs vides et les filtres de type texte [#1223](https://github.com/betagouv/france-chaleur-urbaine/pull/1223).
- **Formulaire de contact :** Ajout de liens vers les adresses email dans le formulaire de contact [#1228](https://github.com/betagouv/france-chaleur-urbaine/pull/1228).
- **Simulateur simplifié :** Amélioration de la landing page du simulateur simplifié avec de nouveaux visuels, des CTA améliorés et une meilleure gestion des variables [#1215](https://github.com/betagouv/france-chaleur-urbaine/pull/1215).
- **Affichage des réseaux :** Amélioration de l'affichage des réseaux de chaleur, de froid et en construction, avec ajout de colonnes et de filtres [#1224](https://github.com/betagouv/france-chaleur-urbaine/pull/1224).

### Évolutions techniques
- **Dépendances :** Mise à jour des dépendances du projet [#1229](https://github.com/betagouv/france-chaleur-urbaine/pull/1229).
- **Emails :** Envoi des emails depuis une adresse no-reply beta.gouv pour une meilleure gestion de la délivrabilité.
- **Admin Events :** Refonte de l'écran d'événements dans l'administration avec une interface de type tableau de bord Grafana.
- **Typage :** Amélioration du typage de certaines variables pour une meilleure robustesse du code.
- **Refactoring :** Refactoring de certains composants pour améliorer la lisibilité et la maintenabilité du code.
- **Images :** Conversion des images au format WebP pour optimiser la performance.

### Autres changements
- **Documentation :** Mise à jour de la documentation.
- **Tests :** Correction de tests suite à des modifications du code.
- **Linting :** Amélioration du linting et de la conformité aux standards de codage.
- **Configuration :** Mise à jour de la configuration du projet.
- **Nettoyage de code :** Suppression de code inutile et amélioration de la structure du code.
