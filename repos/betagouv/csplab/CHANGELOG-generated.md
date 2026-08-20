## Changelog : csplab (30 derniers jours, au 19 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante dans la précision de la recherche d'offres et la gestion des processus de recrutement. Les utilisateurs bénéficient désormais de filtres de recherche beaucoup plus riches (géographie, domaine, type de contrat, etc.) et d'outils de gestion de pipeline plus fluides. Parallèlement, la sécurité et la fiabilité du système ont été renforcées par une gestion fine des droits d'accès et une optimisation des performances de l'API.

### Évolutions fonctionnelles
- **Recherche et filtrage des offres** : Ajout massif de nouveaux critères de recherche pour les offres d'emploi, incluant la zone géographique (région, département, pays, rayon), les mots-clés, le domaine, l'organisme, le type de contrat, le niveau d'expérience et le lieu de travail [#1136](https://github.com/betagouv/csplab/issues/1136), [#1125](https://github.com/betagouv/csplab/issues/1125), [#1100](https://github.com/betagouv/csplab/issues/1100), [#1077](https://github.com/betagouv/csplab/issues/1077).
- **Gestion du recrutement et des candidatures** : 
    - Amélioration du suivi des étapes de recrutement avec la possibilité de changer les étapes des candidatures par lots [#948](https://github.com/betagouv/csplab/issues/948), [#1154](https://github.com/betagouv/csplab/issues/1154).
    - Optimisation de l'interface de gestion (Kanban avec autoscroll, clarification des modales de traitement par lot) [#1107](https://github.com/betagouv/csplab/issues/1107), [#1105](https://github.com/betagouv/csplab/issues/1105).
    - Meilleure distinction des dates de mise à jour entre les recruteurs et les candidats [#1156](https://github.com/betagouv/csplab/issues/1156).
- **Gestion des organismes** : Ajout de nouvelles vues pour la création d'organismes et enrichissement des informations affichées [#1178](https://github.com/betagouv/csplab/issues/1178), [#1182](https://github.com/betagouv/csplab/issues/1182).

### Évolutions techniques
- **Sécurité et gestion des accès (RBAC)** : Mise en place d'un système complet de contrôle d'accès basé sur les rôles (RBAC) pour sécuriser les actions et la consultation des données selon le profil de l'agent (recruteur, agent, etc.) [#1054](https://github.com/betagouv/csplab/issues/1054), [#1030](https://github.com/betagouv/csplab/issues/1030), [#1025](https://github.com/betagouv/csplab/issues/1025).
- **Optimisation de l'API** : 
    - Amélioration de la gestion de la charge via l'utilisation de Redis pour le *throttling* (limitation de débit) et ajout d'en-têtes d'information sur les limites d'utilisation [#1086](https://github.com/betagouv/csplab/issues/1086), [#1068](https://github.com/betagouv/csplab/issues/1068).
    - Mise en place de limites quotidiennes pour les clés d'API [#1061](https://github.com/betagouv/csplab/issues/1061).
- **Modernisation du Frontend** : Migration de la gestion des données vers Pinia Colada pour améliorer la réactivité et la gestion de l'état de l'application [#1022](https://github.com/betagouv/csplab/issues/1022), [#1011](https://github.com/betagouv/csplab/issues/1011).
- **Architecture Backend** : Refactorisation de plusieurs composants métier (Organisme, Candidature) et nettoyage des contextes délimités pour une meilleure maintenabilité [#1155](https://github.com/betagouv/csplab/issues/1155), [#1073](https://github.com/betagouv/csplab/issues/1073).

### Autres changements
- **Documentation** : Mise à jour du guide de l'API et de la documentation des filtres [#1137](https://github.com/betagouv/csplab/issues/1137), [#1108](https://github.com/betagouv/csplab/issues/1108).
- **Corrections (Bugfixes)** : Divers correctifs sur l'interface utilisateur (largeur des barres de recherche, affichage des composants) et sur le processus d'ingestion des données (mapping des niveaux d'études et des types de contrats) [#1104](https://github.com/betagouv/csplab/issues/1104), [#1049](https://github.com/betagouv/csplab/issues/1049), [#1028](https://github.com/betagouv/csplab/issues/1028).
