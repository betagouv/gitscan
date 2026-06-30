## Changelog : sylvasan (30 derniers jours, au 29 juin 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'application mobile (Android et iOS), notamment des corrections de bugs, des améliorations de l'expérience utilisateur (gestion des cartes, affichage des données, validation des formulaires) et des mises à jour de l'interface utilisateur. Des efforts ont également été déployés pour améliorer la robustesse de l'application et la gestion des données, avec notamment l'ajout de mécanismes de synchronisation et de sauvegarde automatique. Enfin, de nombreuses dépendances ont été mises à jour pour bénéficier des dernières corrections de sécurité et améliorations de performance.

### Évolutions fonctionnelles
- **Gestion des données :** Ajout d'un mécanisme automatique de mise à jour des données et d'un indicateur visuel pour signaler leur fraîcheur. Possibilité de synchroniser toutes les données.
- **Géolocalisation :** Amélioration de la géolocalisation avec l'utilisation des services natifs de l'appareil, permettant une sélection plus précise de la position sur la carte. Affichage des coordonnées et possibilité de les modifier directement.
- **Formulaires :** Amélioration de la validation des formulaires, notamment pour les champs conditionnels et les sous-champs. Ajout de la validation du type de champ lors de l'édition.
- **Vocabulaires :** Amélioration de la gestion des vocabulaires, avec un chargement plus fiable et une meilleure intégration dans les formulaires.
- **Suppression :** Ajout d'un modal de confirmation pour la suppression d'enquêtes et de réponses.
- **Authentification :** Amélioration du processus de connexion avec la gestion des erreurs et des flux OAuth. Ajout d'un email de confirmation après l'inscription.
- **Interface utilisateur :** Amélioration de l'interface utilisateur mobile avec des ajustements de marges, de hauteurs et d'icônes. Ajout d'indicateurs de chargement (spinners) pour améliorer l'expérience utilisateur.
- **Pôles :** Ajout de la gestion des pôles, permettant de filtrer et d'organiser les enquêtes par pôle.

### Évolutions techniques
- **Mises à jour des dépendances :** De nombreuses dépendances ont été mises à jour (Django, React, Vite, Capacitor, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- **Refactoring :** Refactoring du code pour améliorer la lisibilité et la maintenabilité.
- **Tests :** Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- **CI/CD :** Amélioration du pipeline CI/CD pour automatiser les tests et le déploiement.
- **Optimisations :** Optimisation des performances de l'application, notamment en réduisant le nombre de requêtes API et en améliorant la gestion de la mémoire.
- **Architecture :** Amélioration de l'architecture de l'application pour faciliter l'ajout de nouvelles fonctionnalités et la maintenance du code.
- **Gestion des erreurs :** Amélioration de la gestion des erreurs pour fournir des messages plus informatifs aux utilisateurs.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les dernières modifications de l'application.
- **Nettoyage du code :** Suppression du code mort et des commentaires inutiles.
- **Configuration :** Mise à jour de la configuration de l'application.
- **Ajout d'un ADR (Architecture Decision Record) :** Documentation d'une décision architecturale concernant le "prop-drilling".
- **Correction de coquilles et de fautes de frappe.**
- **Mise à jour des icônes et des images pour le store.**
