## Changelog : ami-notifications-api (30 derniers jours, au 30 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des notifications et des préférences de localisation. Des corrections et des améliorations ont également été apportées à l'API et à l'interface d'administration, ainsi qu'à la gestion des identifiants et de l'authentification.

### Évolutions fonctionnelles
- **Gestion des notifications :** Amélioration de l'affichage des icônes de notification, avec récupération depuis l'API et gestion des cas où l'icône n'est pas disponible. Ajout de la possibilité d'archiver les notifications et les éléments associés.
- **Préférences de localisation :** Refonte de la page de gestion des zones de notification, avec la possibilité de sélectionner une zone en fonction de la ville. Ajout d'une fonctionnalité pour effacer les adresses enregistrées.
- **Authentification :** Implémentation d'une procédure de "silent login" avec FranceConnect pour une expérience utilisateur plus fluide. Amélioration de la gestion des tokens et des sessions.
- **API :** Ajout d'un endpoint pour la gestion des événements v2 et amélioration de la gestion des champs liés aux items.
- **Interface d'administration :** Amélioration de l'envoi de notifications depuis l'interface d'administration.

### Évolutions techniques
- **Infrastructure :** Mise à jour de plusieurs dépendances, notamment `uv`, `js-yaml`, `pyjwt`, `cryptography`, `esbuild`, `svelte`, `vitest`, `ws`, `idna` et `ujson`.
- **Architecture :** Refactorisation de certains composants de l'interface utilisateur pour améliorer la maintenabilité et la performance.
- **Tests :** Amélioration des tests unitaires, notamment pour la page de préférences de zone.
- **Réplication :** Amélioration de la réplication des données, notamment pour la gestion des abonnements et l'accès aux données depuis le datawarehouse.
- **Outils :** Configuration de Vite avec LightningCSS.
- **Gestion des tâches :** Utilisation de `django-tasks-db` pour la gestion des tâches asynchrones.

### Autres changements
- Amélioration de la documentation et des commentaires dans le code.
- Correction de problèmes de RGAA (accessibilité).
- Nettoyage du code et suppression de fichiers inutiles.
- Ajout de meta tags pour la compatibilité avec certains outils.
- Correction de bugs mineurs et amélioration de la stabilité de l'application.
- Suppression des valeurs par défaut pour certains champs dans l'API d'administration.
- Ajout d'un mécanisme pour éviter de retourner des notifications expirées.
- Amélioration de la gestion des erreurs et des logs.
- Correction d'un bug lié à la gestion des cookies lors du login avec FranceConnect.
