## Changelog : code-du-travail-numerique (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées au site code-du-travail-numerique au cours des 30 derniers jours. Les mises à jour incluent des améliorations de la recherche, des corrections de bugs sur les modèles de documents et les tests, ainsi que des améliorations de l'interface utilisateur et de l'accessibilité. De nouvelles fonctionnalités ont également été ajoutées, notamment des widgets et des informations JSON-LD pour améliorer le référencement.

### Évolutions fonctionnelles
- **Recherche :** Amélioration de la recherche, notamment en utilisant la version 2 par défaut et en améliorant l'accessibilité (#7061, #7077, #7107, #7115).
- **Modèles de documents :** Correction de la gestion des listes et des informations dans la page des modèles de documents (#7117).
- **Page d'accueil :** Changement de l'interface utilisateur dans la section des modèles et ajout de nouvelles icônes pour les thèmes (#7093, #7094).
- **Outils :** Suppression des questions "cul de sac" dans les outils, améliorant l'expérience utilisateur (#7079).
- **Thèmes :** Nouveau design des pages thèmes (#7073).
- **Intégration de widgets :** Ajout de widgets en mode legacy et de nouveaux widgets (#7096).
- **JSON-LD :** Ajout du support pour les balises JSON-LD `GovernmentOrganization`, `Website`, `Breadcrumbs` et `Legislation` pour améliorer le référencement (#7071).

### Évolutions techniques
- **Next.js :** Mise à jour vers la dernière version (#7095).
- **CI/CD :** Ajout d'un CI manuel pour lancer des audits Lighthouse (#7074).
- **Tests E2E :** Amélioration et correction des tests E2E pour assurer une couverture complète et une exécution réussie (#7111, #7114, #7078).
- **Utilitaires partagés :** Ajout du `naf` et des redirections `idcc` dans le package partagé (#7075).
- **Suppression :** Suppression du fichier de workflow d'analyse CodeQL.

### Autres changements
- **Mattermost :** Ajout d'un message dans Mattermost après une release (#7080).
- **Accessibilité :** Amélioration de l'accessibilité de la popup de recherche (#7089).
- **Redirections :** Suppression de la redirection pour les conventions collectives 1031 et 3203 (#7109).
- **Corrections diverses :** Correction de la zone de clic sur "La hiérarchie des textes" (#7090) et fermeture de la popup de recherche lors du changement de lien (#7083).
