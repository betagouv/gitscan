## Changelog : conseillers-entreprises (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la qualité des données, la correction de bugs et l'optimisation des performances. Des améliorations ont été apportées au suivi des statistiques, à la gestion des logs et à l'expérience utilisateur, notamment concernant la recherche d'entreprises et la gestion des enquêtes de satisfaction. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- **Recherche d'entreprises :** La recherche d'entreprises a été améliorée avec une limitation à 3 caractères pour éviter les requêtes inutiles et améliorer la performance.
- **Enquêtes de satisfaction :** Ajout d'une nouvelle question sur les résultats obtenus suite à l'accompagnement, avec une interface utilisateur et des exports CSV améliorés.
- **Questionnaire :** Intégration d'un questionnaire accessible via une nouvelle entrée de navigation.
- **Statistiques :** Ajout de nouvelles statistiques concernant les acquisitions et les prises en charge rapides.
- **Informations utilisateur :** Possibilité de visualiser et modifier les flags `app_info` des utilisateurs dans l'interface d'administration.
- **Suivi Google Ads :** Correction de l'envoi des événements de conversion à Google Ads.
- **Gestion des experts :** Amélioration de la gestion des zones géographiques des experts.

### Évolutions techniques
- **Logs :** Amélioration de la journalisation des tentatives d'authentification, incluant l'adresse IP et les en-têtes `X-Forwarded-For`. Suppression de la journalisation des redirections d'accès non autorisées.
- **Base de données :** Ajout d'index pour optimiser les requêtes et améliorer les performances.
- **Dépendances :** Mise à jour de plusieurs dépendances, notamment Ruby (4.0.3), Stimulus (3.2.2), ERB (6.0.4) et Devise (5.0.4).
- **Architecture :** Refactorisation du code pour supprimer des méthodes inutilisées et simplifier la logique existante.
- **SEO :** Amélioration des données structurées pour le SEO, notamment en utilisant le type `ImageObject` pour le logo de l'organisation.
- **Sécurité :** Correction d'une validation manquante pour les droits d'utilisateur "sponsor".
- **Navbar :** Refonte de la navbar avec l'utilisation de Turbo et une simplification de la logique.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les changements de nom des institutions (Baleen remplacé par Ubika).
- **Nettoyage de code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Tests :** Ajout de tests unitaires et d'intégration pour valider les nouvelles fonctionnalités et les corrections de bugs.
- **Configuration :** Mise à jour de la configuration pour gérer correctement les URL HTTPS en développement.
- **Wording :** Modification du libellé "Taux de prise en charge" en "taux d'échange" dans les statistiques.
