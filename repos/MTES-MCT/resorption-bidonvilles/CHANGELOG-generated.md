## Changelog : resorption-bidonvilles (30 derniers jours, au 2026-06-18)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur, notamment au niveau de la gestion des actions et des indicateurs, ainsi que par des corrections de bugs et des optimisations de performance. Des efforts ont également été déployés pour renforcer la sécurité et la robustesse de l'application, notamment en matière de gestion des permissions et de validation des données.

### Évolutions fonctionnelles
*   Amélioration de l'affichage des indicateurs de scolarisation et ajout de nouvelles données (mineurs scolarisés, etc.).
*   Ajout de la possibilité de filtrer les actions par structure pour les opérateurs.
*   Affichage des actions de la structure connectée dans un onglet dédié.
*   Ajout d'un bouton pour mettre à jour les sites sans modification des données.
*   Amélioration de l'export Excel, incluant des informations plus détaillées et une meilleure mise en forme.
*   Possibilité de masquer le filtre "Financement DIHAL" en fonction des permissions de l'utilisateur.
*   Ajout de la gestion de l'opérateur principal pour chaque action, avec des restrictions d'accès en fonction des rôles.
*   Amélioration de l'affichage et de la gestion des indicateurs d'action.
*   Ajout de la possibilité de trier les actions par plusieurs critères.
*   Ajout d'un bandeau d'information en cas de canicule.

### Évolutions techniques
*   Refactorings importants du code, notamment au niveau de l'API et du frontend, pour améliorer la lisibilité, la maintenabilité et la performance.
*   Mise à jour des dépendances et correction de problèmes de linting.
*   Amélioration de la gestion des transactions en base de données pour garantir la cohérence des données.
*   Utilisation de types plus précis et de validations plus robustes pour améliorer la qualité du code.
*   Optimisation des requêtes SQL et des performances globales de l'application.
*   Implémentation de tests unitaires pour garantir la fiabilité des nouvelles fonctionnalités et des corrections de bugs.
*   Migration vers l'utilisation de `structuredClone` pour la copie d'objets, améliorant ainsi la performance et la sécurité.
*   Utilisation de l'ISOString pour la gestion des dates.

### Autres changements
*   Mise à jour de la documentation et des commentaires du code.
*   Correction de problèmes d'affichage et d'ergonomie de l'interface utilisateur.
*   Amélioration de la gestion des erreurs et des messages d'alerte.
*   DSFRisation du header et du footer.
*   Suppression de la page 404, gérée par le LayoutError.
*   Correction de la popup de nouveautés.
*   Correction du lien LinkedIn.
*   Amélioration de la dette technique.
*   Mise à jour de la date de PROD et de la date limite du questionnaire.
