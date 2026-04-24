## Changelog : france-chaleur-urbaine (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec la refonte de la landing page du simulateur simplifié et l'ajout de nouvelles informations sur les écoréseaux. Des améliorations techniques ont également été apportées, notamment des mises à jour de dépendances et des corrections de bugs.

### Évolutions fonctionnelles
- **Simulateur simplifié :** Refonte complète de la landing page avec de nouveaux visuels, des CTA améliorés et une meilleure intégration du carrousel. [#1215](https://github.com/betagouv/france-chaleur-urbaine/pull/1215)
- **Écoréseaux :** Ajout d'une nouvelle colonne et d'un filtre pour les écoréseaux dans la liste des réseaux de chaleur/froid.  Intégration des données des écoréseaux avec l'ajout de leur source et d'un label spécifique. [#1224](https://github.com/betagouv/france-chaleur-urbaine/pull/1224)
- **Page "Qui sommes-nous" :** Mise à jour des textes et suppression de la section "équipe" ainsi que correction du wording concernant le budget. [#1232](https://github.com/betagouv/france-chaleur-urbaine/pull/1232)
- **Formulaire de contact :** Ajout de liens vers les formulaires de contact dans les emails. [#1228](https://github.com/betagouv/france-chaleur-urbaine/pull/1228)
- **Gestion des utilisateurs :** Ajout d'une structure pour la gestion des utilisateurs dans l'administration. [#1226](https://github.com/betagouv/france-chaleur-urbaine/pull/1226)
- **Affichage des réseaux :** Le label des réseaux est maintenant affiché sur la carte, la page réseau et la liste des réseaux.
- **Tableau des réseaux :** Ajout de filtres textuels sur les colonnes du tableau des réseaux de chaleur.

### Évolutions techniques
- **Mise à jour des dépendances :** Mise à jour des dépendances du projet, incluant TypeScript et remark-directive-rehype. [#1229](https://github.com/betagouv/france-chaleur-urbaine/pull/1229)
- **Envoi d'emails :** Configuration de l'envoi d'emails depuis une adresse no-reply beta.gouv.
- **Tests :** Correction d'un bug dans les tests concernant l'import en masse d'adresses. [#1230](https://github.com/betagouv/france-chaleur-urbaine/pull/1230)
- **Admin Events :** Refonte de l'écran d'administration des événements pour ressembler à un tableau de bord de type Grafana.
- **Linting & Styling :** Amélioration du linting et du style avec des classes Tailwind CSS canoniques.
- **Typage :** Amélioration du typage de certaines variables et réponses API.

### Autres changements
- Mise à jour des statistiques d'avril.
- Procédure de mise à jour des statistiques mensuelles documentée.
- Correction de coquilles et d'erreurs typographiques.
- Conversion d'images au format WebP pour optimiser les performances.
- Suppression de code inutile et amélioration de la structure du code.
- Ajout d'images pour les articles et la nouvelle landing du simulateur simplifié.
- Amélioration du nommage du tracking pour le simulateur simplifié.
- Correction d'un problème d'affichage initial des réseaux dans les iframes.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
