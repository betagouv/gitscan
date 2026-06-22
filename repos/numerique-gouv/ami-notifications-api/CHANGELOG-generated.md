## Changelog : ami-notifications-api (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de la gestion d'archivage des suivis et l'implémentation d'un nouveau processus d'authentification via FranceConnect et une application dédiée (FI). Des corrections ont également été apportées pour améliorer la stabilité et la sécurité de l'API.

### Évolutions fonctionnelles
- **Gestion des suivis :** Ajout de la fonctionnalité d'archivage des suivis, incluant une page dédiée pour les consulter, un bouton d'archivage et une mise à jour de l'API pour gérer l'état archivé des éléments. [#776](https://github.com/numerique-gouv/ami-notifications-api/issues/776)
- **Authentification FranceConnect et FI :** Implémentation d'un nouveau flux d'authentification via FranceConnect et une application dédiée (FI), incluant la gestion des sessions, des tokens, des informations utilisateur et la redirection après authentification. [#917](https://github.com/numerique-gouv/ami-notifications-api/issues/917), [#907](https://github.com/numerique-gouv/ami-notifications-api/issues/907), [#708](https://github.com/numerique-gouv/ami-notifications-api/issues/708)
- **Gestion des adresses :** Amélioration de la gestion des adresses utilisateur avec la possibilité de les supprimer, de les rechercher et de les associer à des zones géographiques. [#789](https://github.com/numerique-gouv/ami-notifications-api/issues/789)
- **Notifications :**  Ajout d'un champ `valid_until` pour les notifications et mise à jour de l'API pour exclure les notifications expirées. [#674](https://github.com/numerique-gouv/ami-notifications-api/issues/674)
- **Lien notification/suivi :** Mise à jour du lien dans les notifications pour rediriger vers la page de suivi correspondante. [#794](https://github.com/numerique-gouv/ami-notifications-api/issues/794)

### Évolutions techniques
- **Réplication base de données :** Amélioration de la réplication des accès à la base de données vers l'entrepôt de données. [#904](https://github.com/numerique-gouv/ami-notifications-api/issues/904)
- **Gestion des registrations push :**  Optimisation de la gestion des registrations push pour ne stocker que la dernière registration pour un appareil mobile donné. [#893](https://github.com/numerique-gouv/ami-notifications-api/issues/893)
- **Configuration :** Amélioration de la gestion des variables d'environnement, notamment pour l'intégration avec Scalingo. [#905](https://github.com/numerique-gouv/ami-notifications-api/issues/905)
- **Sécurité :** Correction d'une erreur d'intégrité lors de la déconnexion et ajout de la paramétrisation des scopes d'authentification. [#971](https://github.com/numerique-gouv/ami-notifications-api/issues/971), [#907](https://github.com/numerique-gouv/ami-notifications-api/issues/907)

### Autres changements
- Mise à jour de la configuration Vite pour LightningCSS.
- Amélioration de la gestion des zones et des compteurs sur l'interface utilisateur.
- Correction de bugs mineurs sur l'interface utilisateur (défilement, affichage).
- Mise à jour de plusieurs dépendances (uv, webob, esbuild, etc.).
- Nettoyage du code et suppression de fichiers inutiles.
- Amélioration de la documentation et des messages d'aide pour les notifications planifiées.
